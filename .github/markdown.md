<!--
title: '🎨 README THEME'
description: 'How the Markdown Kit draws this README, and how to change its theme, holidays, words, placards and trophies. Read it before editing its settings.'
type: guide
keywords: [markdown kit, blackprint, holidays, placards, trophies, banners, drawn readme]
-->

<div align="center">

# 🎨 README THEME

<a name="top"></a>

**How this README is drawn, and how to give it the theme you want.**

_Seeded once. Yours to change. Never synced over._

</div>

---

## 💡 What Draws It

The [Markdown Kit](https://github.com/tannergolden/markdown) draws this
repository's README every night at midnight UTC: the header, the placards, the
trophy case and the footer, each committed as SVGs under `assets/`, in one
theme. Two files decide how, and both are yours:

| File                             | What it holds                                                                   |
| :------------------------------- | :------------------------------------------------------------------------------ |
| `.github/workflows/markdown.yml` | The stub: when the kit runs, and the one secret it may read                     |
| `.github/markdown.yaml`          | The settings: the theme, the holidays, the words, the placards and the trophies |

**🔄 Template Sync never touches either.** A repository generated from the
golden path starts with the template's own settings, the `blackprint` with the
holidays on, and from then on they change only when you change them, so a
theme you choose stays chosen. This page is the one part a sync keeps current,
so its instructions follow the kit.

The kit owns what sits between its `<!-- markdown:... -->` markers in
`README.md`, what it draws under `assets/`, and its lock,
`.github/markdown.lock.json`. Never edit those by hand: change the settings
and the next run redraws them. Every word outside the markers is yours.

---

## 🎨 Change The Theme

1. **Set `theme:`** in `.github/markdown.yaml` to any theme below.
2. **Commit it** to your default branch.
3. **Run 📝 Markdown** from the Actions tab, or wait for midnight UTC. The run
   redraws every part in the new theme and commits the page once.

| `theme:`                                                           | The page wears                                                                           |
| :----------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| `standard`                                                         | The kit's default: the original badges' look at the size of a header                     |
| `blueprint`, `blackprint`, `brownprint`, `redprint` to `pinkprint` | A print: one colour drawn as a drafting sheet, on white by day and on the sheet by night |
| `rainbowprint`                                                     | The next print of the spectrum each time something the page shows changes                |
| A print of your own, named under `prints:`                         | Your colours, drawn as a print                                                           |
| `heaven-and-hell`                                                  | A pixel theme: heaven in GitHub's light mode and hell in its dark mode, all year         |
| `medieval` or `matrix`                                             | A collection: a new pixel design on the first of every month                             |
| One collection's design, such as `medieval-forge`                  | That design, kept all year                                                               |

[The kit's theme-sets page](https://raw.githack.com/tannergolden/markdown/Development/docs/references/themes/index.html)
draws every theme by day and by night, so you can pick by eye, and the kit's
[Your own prints](https://github.com/tannergolden/markdown/blob/Development/docs/references/Settings.md#your-own-prints)
shows how to make a print in your own colours.

The stub can name a theme too, as an input under `with:`, and wins over the
settings when it does. Keep the choice in one place, the settings.

---

## ✍️ Everything Else It Draws

- **The holidays.** With `holidays: true`, each holiday's set takes the whole
  page for its days, then hands it back: New Year's Day, Valentine's Day,
  Juneteenth, Independence Day, Halloween, Thanksgiving and Christmas.
  `holidays: false` keeps them away, `holiday-days:` sets how long each is
  up, 3 to 7 days, and `timezone:` whose midnight they start at. Every year
  on the day GitHub created this repository the Birthday set takes the page;
  `birthday: false` keeps it away.
- **The words.** The header letters this repository's name and its
  description on GitHub, which reads best at 150 characters or fewer: the kit
  cuts one longer than 160. `motto` and `closing` under `banners:` start as the
  golden path's own; write your page's, or delete them.
- **The placards.** Each entry under `elements:` with `kind: placard` and
  `measure: owner/name` draws a card for that repository, measured from GitHub.
  A card is drawn only where the README carries its two markers,
  `<!-- markdown:element:ID:start -->` and its `:end` twin, and two pairs side
  by side make a row. Delete the entry and its markers to drop one.
- **The trophy case.** `style:` under `trophies:` is `trophy`, `crest`,
  `medallion`, `crystal` or `plaque`, each drawn in the theme; `look: standard`
  keeps the metal look in every theme.

Every other key, the badges among them, is in the kit's
[Settings](https://github.com/tannergolden/markdown/blob/Development/docs/references/Settings.md).
A part set to `false`, such as `trophies: false`, is taken away on the next
run, its files and its README block with it.

---

## 🛠️ When Something Needs You

| You see, or want                                                          | Do this                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A new README, from `docs/templates/Project-README.md`                     | Leave out its masthead and footer: the next run puts the header at the top and the trophy case and footer at the foot. Copy the placards' markers across to keep them                                                                                                 |
| **📤 Commit and push** refused, by a branch that takes only pull requests | Uncomment `with:` and `commit: pr` in the stub: each redraw then arrives as one pull request on `chore/markdown`, once **Allow GitHub Actions to create and approve pull requests** is on                                                                             |
| A placard for a private repository                                        | Save a read-only personal token as the `MARKDOWN_TOKEN` secret, and the kit measures with it                                                                                                                                                                          |
| No drawn page at all                                                      | Set `banners`, `badges`, `elements` and `trophies` to `false` and let one run take the drawing away, then delete the stub and the settings                                                                                                                            |
| A repository generated before the template drew its README                | Take the `#` off `/.github/markdown.yaml` and `/.github/workflows/markdown.yml` in `.github/template-sync`, run 🔄 Template Sync once with a `BOT_ACCESS_TOKEN`, which a workflow file needs, then put the `#` back and take the README's own masthead and footer out |

The kit's
[Troubleshooting A Run](https://github.com/tannergolden/markdown/blob/Development/docs/operations/Troubleshooting-A-Run.md)
covers the rest.

---

<div align="center">

**One file chooses the look. Every run redraws it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
