#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
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

    def assertTrackedWithoutCase(self, *paths: str) -> None:
        """Tracked on macOS and Windows too, where git matches without regard to case."""
        for p in paths:
            result = subprocess.run(
                ['git', '-c', 'core.ignorecase=true', 'check-ignore', '-q', '--no-index', p],
                cwd=self.root, capture_output=True,
            )
            self.assertNotEqual(result.returncode, 0, f'{p} is IGNORED where case does not matter')


class TestLeftoversDoNotReachIntoContent(GitignoreTestCase):
    """Python packaging leftovers, kept to the places they are leftovers."""

    def test_a_downloads_folder_below_the_root_is_content(self) -> None:
        """Unanchored, `downloads/` hid assets/downloads/ whole, re-includes and all."""
        self.assertTracked('assets/downloads/press-kit.zip', 'docs/downloads/guide.md')
        self.assertIgnored('downloads/setup.tar.gz')

    def test_an_env_folder_survives_where_case_does_not_matter(self) -> None:
        """`ENV/` matched every `env/` on macOS and Windows: Terraform's among them."""
        self.assertTrackedWithoutCase('env/prod/main.tf', 'src/env/index.ts')


class TestCredentialStores(GitignoreTestCase):
    def test_login_files_are_ignored(self) -> None:
        self.assertIgnored('.pypirc', '.netrc', '_netrc', '.git-credentials',
                           '.docker/config.json', 'tools/.docker/config.json')

    def test_a_docker_folder_that_is_not_dockers_own_is_left_alone(self) -> None:
        self.assertTracked('docker/config.json')


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

    def test_keystores_and_private_keys_are_ignored(self) -> None:
        self.assertIgnored(
            'app/release.keystore', 'keystore.jks', 'cert.p12', 'cert.pfx',
            'AuthKey_ABC123.p8', 'putty.ppk',
            'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519', 'deploy/id_ed25519',
        )

    def test_a_public_key_is_not(self) -> None:
        self.assertTracked('id_ed25519.pub', 'keys/id_rsa.pub')

    def test_infrastructure_state_and_variables_are_ignored(self) -> None:
        # Terraform state holds every secret a plan touched, in plain text.
        self.assertIgnored(
            'terraform.tfstate', 'terraform.tfstate.backup', 'infra/terraform.tfstate',
            'prod.tfvars', 'secrets.auto.tfvars', 'secrets.tfvars.json',
        )

    def test_the_provider_lock_is_not(self) -> None:
        # The lock pins providers, holds no secret, and is meant to be committed.
        self.assertTracked('.terraform.lock.hcl')

    def test_direnv_files_are_ignored(self) -> None:
        self.assertIgnored('.envrc', '.direnv/python-3.12/bin/python')


class TestFilesThatLookLikeOutputButAreSource(GitignoreTestCase):
    """A broad pattern must not swallow the files a project has to commit."""

    def test_the_build_wrappers_jars_are_tracked(self) -> None:
        # `./gradlew` and `./mvnw` cannot start without these.
        self.assertTracked(
            'gradle/wrapper/gradle-wrapper.jar',
            'services/api/gradle/wrapper/gradle-wrapper.jar',
            '.mvn/wrapper/maven-wrapper.jar',
        )

    def test_every_other_jar_is_still_ignored(self) -> None:
        self.assertIgnored('lib/vendor.jar', 'build/libs/app.jar', 'tools/helper.jar')

    def test_an_archive_in_assets_is_tracked(self) -> None:
        self.assertTracked('assets/fonts/inter.zip', 'assets/print/press-kit.tar.gz')

    def test_an_archive_anywhere_else_is_still_ignored(self) -> None:
        self.assertIgnored('dist/release.zip', 'release.tar.gz', 'out/bundle.rar')

    def test_a_keynote_deck_in_assets_is_tracked(self) -> None:
        self.assertTracked('assets/slides/launch-talk.key')


class TestToolOutputIsIgnored(GitignoreTestCase):
    """Caches and reports the common tools write beside the code."""

    def test_python_tool_caches(self) -> None:
        self.assertIgnored(
            '.pytest_cache/v/cache/lastfailed', '.mypy_cache/3.12/x.json',
            '.ruff_cache/0.6.0/x', '.tox/py312/x', '.nox/tests/x',
            '.ipynb_checkpoints/notebook-checkpoint.ipynb',
        )

    def test_coverage_output(self) -> None:
        self.assertIgnored('.coverage', '.coverage.host.1234', 'htmlcov/index.html')

    def test_compiled_classes_and_visual_studio_state(self) -> None:
        self.assertIgnored('Foo.class', 'obj/Debug/x', '.vs/x/v17/.suo', 'MyApp.csproj.user', 'MyApp.suo')

    def test_end_to_end_reports(self) -> None:
        self.assertIgnored('playwright-report/index.html', 'test-results/x/trace.zip', 'blob-report/x')

    def test_yarn_state_without_its_committed_folders(self) -> None:
        self.assertIgnored('.yarn/cache/x.zip', '.yarn/install-state.gz', '.pnp.cjs', '.pnp.loader.mjs')
        self.assertTracked('.yarn/releases/yarn-4.5.0.cjs', '.yarn/plugins/x.cjs', '.yarn/patches/x.patch')


class TestEditorConfiguration(GitignoreTestCase):
    """The four VS Code files a team shares, the README logging them, and nothing else."""

    def test_the_shared_four_are_tracked(self) -> None:
        self.assertTracked(
            '.vscode/settings.json',
            '.vscode/extensions.json',
            '.vscode/launch.json',
            '.vscode/tasks.json',
        )

    def test_the_folder_log_is_tracked(self) -> None:
        self.assertTracked('.vscode/README.md')

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
