#!/usr/bin/env python3
"""Tests for this repository's .gitignore.

WHY THIS EXISTS. An ignore rule fails silently by construction: `git add`
succeeds, says nothing, and the file is simply not there. This scaffold ships
its .gitignore to every repository generated from it, so a pattern that is
wrong here is wrong everywhere, invisibly.

Two classes of bug have already been found in this file by hand - a duplicate
that silently revoked a negation fifty lines earlier, and directory names that
are SOURCE in mainstream ecosystems being ignored as though they were build
output. Both were invisible to every other check in the repository.

Each test runs the real .gitignore through `git check-ignore`, which is the
only authority on what git will actually do.

Run it:

    python3 .github/scripts/test_gitignore.py
"""

from __future__ import annotations

import pathlib
import shutil
import subprocess
import tempfile
import unittest

GITIGNORE = pathlib.Path(__file__).resolve().parents[2] / '.gitignore'


class GitignoreTestCase(unittest.TestCase):
    """A throwaway repository carrying nothing but the real .gitignore."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.root = pathlib.Path(tempfile.mkdtemp(prefix='gitignore-test-'))
        subprocess.run(['git', 'init', '-q', '.'], cwd=cls.root, check=True)
        shutil.copy(GITIGNORE, cls.root / '.gitignore')

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.root, ignore_errors=True)

    def ignored(self, path: str) -> bool:
        return subprocess.run(
            ['git', 'check-ignore', '-q', '--no-index', path],
            cwd=self.root, capture_output=True,
        ).returncode == 0

    def assertTracked(self, *paths: str) -> None:
        for p in paths:
            self.assertFalse(
                self.ignored(p),
                f'{p} is IGNORED - `git add` would silently drop it',
            )

    def assertIgnored(self, *paths: str) -> None:
        for p in paths:
            self.assertTrue(self.ignored(p), f'{p} is tracked but should be ignored')


class TestSourceDirectoriesAreNotSwallowed(GitignoreTestCase):
    """Names that are SOURCE in mainstream ecosystems, not build output.

    This scaffold imposes no directory structure - that is its entire premise -
    so it must not quietly decide that a whole tree is disposable.
    """

    def test_lib_is_source_in_ruby_elixir_and_javascript(self) -> None:
        # Ruby gems and Elixir applications keep ALL their source in lib/.
        self.assertTracked(
            'lib/my_gem.rb',
            'lib/my_app/application.ex',
            'lib/index.ts',
            'src/lib/Button.svelte',   # SvelteKit's $lib root
        )

    def test_pkg_is_source_under_the_standard_go_layout(self) -> None:
        self.assertTracked('pkg/service/main.go', 'pkg/api/handler.go')

    def test_bin_holds_committed_entry_points(self) -> None:
        # Rails ships bin/rails and bin/setup; npm packages ship bin/cli.js.
        self.assertTracked('bin/rails', 'bin/cli.js', 'bin/setup')

    def test_a_python_virtualenv_is_still_ignored_wholesale(self) -> None:
        # The reason lib/ and bin/ were ever listed. venv/ covers them, so
        # removing the bare names loses nothing.
        self.assertIgnored(
            'venv/lib/python3.12/site-packages/x.py',
            'venv/bin/activate',
            '.venv',
        )


class TestBuildOutputIsIgnoredAtAnyDepth(GitignoreTestCase):
    """Unanchored on purpose: monorepos and multi-module builds need depth."""

    def test_output_at_the_repository_root(self) -> None:
        self.assertIgnored('build/app.o', 'dist/bundle.js', 'out/x', 'target/x')

    def test_output_nested_in_a_monorepo_or_multi_module_build(self) -> None:
        # Anchoring these to the root would start committing build output for
        # Gradle multi-project, Maven multi-module, and every JS monorepo.
        self.assertIgnored(
            'sub/build/classes/Main.class',      # Gradle multi-project
            'module/target/app.jar',             # Maven multi-module
            'packages/ui/dist/index.js',         # JS monorepo
            'apps/web/.next/build-manifest.json',
        )

    def test_dependency_and_cache_directories(self) -> None:
        self.assertIgnored(
            'node_modules/react/index.js',
            'deep/node_modules/x/y.js',
            '.cache/x',
            'coverage/lcov.info',
        )


class TestTheJavaBuildNegation(GitignoreTestCase):
    """A Java package literally named `build` is source, not output."""

    def test_a_source_package_named_build_survives(self) -> None:
        self.assertTracked(
            'src/main/java/com/example/build/Builder.java',
            'src/test/java/com/example/build/BuilderTest.java',
        )

    def test_ordinary_build_output_is_still_ignored(self) -> None:
        self.assertIgnored('build/libs/app.jar')


class TestEnvironmentFiles(GitignoreTestCase):
    """Every .env variant is a credential file until proven otherwise."""

    def test_every_variant_is_ignored(self) -> None:
        self.assertIgnored(
            '.env', '.env.local', '.env.production', '.env.staging',
            '.env.development', '.env.test', '.env.prod.local',
        )

    def test_the_committed_example_is_not(self) -> None:
        self.assertTracked('.env.example')

    def test_key_material_is_ignored(self) -> None:
        self.assertIgnored('server.pem', 'id_rsa.key', 'certs/tls.pem')


class TestEditorConfiguration(GitignoreTestCase):
    """The four VS Code files a team shares, and nothing else."""

    def test_the_shared_four_are_tracked(self) -> None:
        self.assertTracked(
            '.vscode/settings.json',
            '.vscode/extensions.json',
            '.vscode/launch.json',
            '.vscode/tasks.json',
        )

    def test_everything_else_under_vscode_is_ignored(self) -> None:
        self.assertIgnored('.vscode/private.json', '.vscode/ipch/x')


class TestNoDuplicatePatterns(GitignoreTestCase):
    """A restated pattern silently revokes any negation between the two."""

    def test_every_pattern_appears_once(self) -> None:
        seen: dict[str, int] = {}
        duplicates = []
        for number, raw in enumerate(GITIGNORE.read_text(encoding='utf-8').splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            if line in seen:
                duplicates.append(f'{line!r} at lines {seen[line]} and {number}')
            else:
                seen[line] = number
        self.assertEqual(duplicates, [], 'duplicate patterns: ' + '; '.join(duplicates))


if __name__ == '__main__':
    unittest.main(verbosity=2)
