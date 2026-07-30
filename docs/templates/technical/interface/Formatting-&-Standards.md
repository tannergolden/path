<!--
title: '📐 FORMATTING & STANDARDS'
description: 'Formatting standards for content in the interface layer.'
tags: [formatting, standards, style, interface]
category: docs
-->

<div align="center">

# 📐 FORMATTING & STANDARDS

<a name="top"></a>

**Formatting standards for content in the interface layer.**

_Standardized syntax. Predictable structure. Automated enforcement._

</div>

---

## 🎯 Our Formatting Intent

We believe that code is read more often than it is written. Our objective is to maintain a high degree of structural consistency across our UI codebases, enabling any developer to move between modules with zero friction and total predictability.

- **Automated Uniformity**: We rely on linters and formatters rather than manual review for style.
- **Semantic Structure**: Directory layouts reflect the logical architecture of the application.
- **Expressive Naming**: identifiers clearly communicate intent and scope.

---

## 📝 1. Syntax & Style Blueprint

The foundational rules for code appearance and structure.

| Rule                | Specification                    | Standard                       | Impact                      | Description                   |
| :------------------ | :------------------------------- | :----------------------------- | :-------------------------- | :---------------------------- |
| **Indentation**     | `[2 Spaces \| 4 Spaces \| Tabs]` | Consistent depth across files. | Visual structure precision. | Rule for file indentation.    |
| **Quotes**          | `['Single' \| "Double"]`         | Deterministic string syntax.   | Syntax consistency.         | Rule for string literals.     |
| **Semicolons**      | `[Required \| Omitted]`          | Syntax termination policy.     | Logic termination.          | Rule for statement endings.   |
| **Max Line Length** | `[e.g., 100 Characters]`         | Horizontal scroll prevention.  | Code readability.           | Target width for source code. |

---

## 🏷️ 2. Naming Convention Matrix

Standardizing the language of our codebase.

- **Files & Dirs**: `[kebab-case (all lowercase)]`
- **Components/Classes**: `[PascalCase (UserCard)]`
- **Variables/Logic**: `[camelCase (userData)]`
- **Global Constants**: `[SCREAMING_SNAKE_CASE (API_URL)]`
- **Style Selectors**: `[BEM | Utility-classes | Modules]`

---

## 📂 3. Directory Topology

The physical organization of the client-side domain.

```txt
/src
├── components/    # Reusable, atomic UI elements.
├── features/      # Business logic and domain modules.
├── layouts/       # Structural templates for views.
├── styles/        # Shared tokens and global themes.
└── services/      # API communication and external state.
```

---

## 🛠️ 4. Automated Quality Gates

Ensuring that human error is caught by machine logic.

- **Linter Engine**: `[ESLint | SwiftLint | RuboCop]`
- **Formatting Engine**: `[Prettier | Black | ClangFormat]`
- **Pre-commit Gate**: `[Husky | lint-staged enforcement]`

---

## 📖 5. Documentation Standards

How we explain our technical decisions and present our data.

- **Visual Consistency**: All documents must follow the **[Document Styling & Formatting](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md)** guidelines.
- **Self-Documenting Code**: Favoring clear names over extensive comments.
- **Component Docs**: `[Storybook | JSDoc | Header Blocks]`
- **Module README**: Each major feature folder requires a local README following the centered header pattern.

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Formatted once. Consistent everywhere.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
