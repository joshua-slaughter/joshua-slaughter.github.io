# Updating your website

Everything on the site comes from a handful of plain-text files. You can edit
them directly on GitHub in your browser:

1. Open the file on github.com and click the pencil icon (**Edit this file**).
2. Make your change.
3. Click **Commit changes…** and commit to `main`.

The site rebuilds and goes live automatically, usually within about 2 minutes.
You can watch progress under the repository's **Actions** tab. A green tick
means it worked; a red cross means something in your edit couldn't be read
(most often a YAML indentation slip). Open the failed run to see which line.

> **YAML tips.** The `.yaml` files are indentation-sensitive. Use spaces, not
> tabs, and line new entries up with the ones above them. Put text in
> `"double quotes"`, especially if it contains a colon.

---

## 1. Add a new paper

Edit `data/papers.yaml`. Papers show in the order they appear in the file, so
put the newest near the top. Copy an existing entry and change it:

```yaml
- title: "Title of the new paper"
  authors: ["Slaughter J", "Coauthor A", "Ponting CP"]
  year: 2026
  status: "preprint"
  venue: "medRxiv"
  pdf: ""
  link: "https://doi.org/10.xxxx/xxxxx"
```

- `status` controls where the paper appears. `published` and `accepted` go
  under **Publications**. Everything else (`preprint`, `under review`,
  `revise and resubmit`, `working paper`, `work in progress`) goes under
  **Working Papers** with a small label.
- The title links to `pdf` if you give one, otherwise to `link`.
- Your name is shown in bold wherever it matches `Slaughter J` exactly. You can
  change this under `authorHighlight` in `hugo.yaml`.

**To attach a PDF:** go to the `static/files/` folder on GitHub, click
**Add file → Upload files**, and upload the PDF (for example,
`slaughter-mecfs-2026.pdf`). Then set `pdf: "files/slaughter-mecfs-2026.pdf"`
on that paper.

## 2. Mark a paper as published

In `data/papers.yaml`, change the paper's `status` from `"preprint"` (or
`"under review"`) to `"published"`, set `venue` to the journal name, update
`year`, and replace `link` with the journal DOI. It moves to the
**Publications** list automatically.

## 3. Add a job market paper

On the relevant entry in `data/papers.yaml`, add:

```yaml
  job_market_paper: true
  abstract: "One-paragraph abstract."
  pdf: "files/job-market-paper.pdf"
```

It then appears at the top of the Research section in a highlighted card with
its abstract.

## 4. Update your bio or research interests

Edit `content/_index.md`. The research interests are the list at the top
(between the `---` lines). The bio is the text below them. Separate paragraphs
with a blank line. Links look like `[TarGene](https://github.com/TARGENE/targene-pipeline)`.

The tagline under your name, your title, and your affiliations are in
`hugo.yaml` under `params`.

## 5. Add a teaching entry

Edit `data/teaching.yaml`. Add a course under the right institution:

```yaml
    - course: "Course name"
      role: "Teaching Fellow"
      term: "Spring 2027"
```

Note the six spaces before `- course` so it lines up with the others.

## 6. Add an award

Edit `data/awards.yaml` and add a line pair near the top:

```yaml
- name: "Name of the award"
  year: "2027"
```

## 7. Update your CV

Go to `static/files/` on GitHub, click **Add file → Upload files**, and upload
your new CV **named exactly `cv.pdf`**. It replaces the old one, and every CV
link on the site keeps working.

## 8. Change your photo

Upload a new square-ish photo to `static/images/` named **`photo.jpg`**
(about 500×500 pixels is plenty). It is cropped to a circle automatically.

## 9. Add news items

Create a new file `data/news.yaml` (on GitHub: **Add file → Create new file**
and type `data/news.yaml` as the name):

```yaml
- date: "Oct 2026"
  text: "Paper accepted at *Nature Genetics*."
- date: "Sep 2026"
  text: "Preprint posted on medRxiv."
```

A **News** section appears on the homepage showing the 8 most recent items (put
newest first). Delete the file to remove the section.

## 10. Add a blog post

Create a new file `content/blog/your-post-slug/index.md`:

```markdown
---
title: "Post Title"
date: 2026-10-15
description: "One-sentence summary."
---

Your post, written in Markdown.
```

The homepage then shows a **Writing** section with your latest posts, and the
full list lives at `/blog/`. To add a nav link, add this under `menu: main:` in
`hugo.yaml`:

```yaml
    - name: Writing
      url: "blog/"
      weight: 45
```

## 11. Add or change social links

Edit the `social:` list in `hugo.yaml`. Supported icons: `github`, `scholar`,
`linkedin`, `bluesky`, `orcid`, `twitter`. For example:

```yaml
    - name: "ORCID"
      icon: orcid
      url: "https://orcid.org/0000-0000-0000-0000"
```

## 12. Moving to a custom domain

If you later buy a domain (for example `joshuaslaughter.com`):

1. In `hugo.yaml`, change `baseURL` to `"https://joshuaslaughter.com/"`.
2. In `static/llms.txt`, replace the old address in each link.
3. Add the domain under the repository's **Settings → Pages → Custom domain**
   and follow GitHub's DNS instructions.

## Colours and dark mode

The site follows each visitor's system light/dark setting, and the sun/moon
button in the top bar lets them switch (their choice is remembered in their
browser). All colours are defined at the top of `assets/css/style.css`: the
light theme in the `:root` block, and the dark theme in the two blocks below it.
If you change a dark colour, change it in both of those blocks.

## The artwork

The banner under your name (sampling distributions of √n(X̄ₙ − μ) settling
into the normal limit) is generated by `tools/make_art.py`, which writes it to
`layouts/partials/art/convergence.html`. It takes its colours from the
stylesheet, so it follows the light/dark theme automatically. To tweak it
(row count, spacing, peak height), edit the numbers in the script and run
`python tools/make_art.py`. It needs only standard Python. To remove the
banner, delete the block marked "Banner art" in `layouts/index.html`.

## Footer credit and site metadata

`hugo.yaml` has two switches under `params: mysite:`:

- `credit` shows a small "Created using GaryKing.org/mysite" line in the
  footer. It's currently `false` (hidden).
- `discovery` adds invisible metadata (a `generator` tag and schema.org data
  that helps search engines). It's currently `true`. Set it to `false` to
  remove it.
