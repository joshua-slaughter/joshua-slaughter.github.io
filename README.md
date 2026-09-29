# joshua-slaughter.github.io

Personal academic website of Joshua Slaughter, Ph.D. candidate in the School of Informatics at the University of Edinburgh.

**Live site:** https://joshua-slaughter.github.io/

Built with [Hugo](https://gohugo.io/) (no theme, just a few small templates) and deployed to GitHub Pages by GitHub Actions on every push to `main`.

## Where things live

| What | File |
|------|------|
| Name, title, tagline, email, social links | `hugo.yaml` |
| Bio and research interests | `content/_index.md` |
| Papers | `data/papers.yaml` |
| Software | `data/projects.yaml` |
| Teaching | `data/teaching.yaml` |
| Education and prior research | `data/background.yaml` |
| Fellowships and awards | `data/awards.yaml` |
| CV | `static/files/cv.pdf` |
| Photo | `static/images/photo.jpg` |
| Colours and layout | `assets/css/style.css` |
| Banner artwork | `tools/make_art.py` → `layouts/partials/art/convergence.html` |
| Page templates | `layouts/` |

See [UPDATING.md](UPDATING.md) for step-by-step instructions.

## Previewing locally (optional)

Install Hugo extended (`winget install Hugo.Hugo.Extended` on Windows, `brew install hugo` on macOS), then from this folder run:

```
hugo server
```

and open the address it prints (http://localhost:1313/).
