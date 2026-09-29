"""Generate the site's banner illustration as a Hugo partial.

layouts/partials/art/convergence.html
  A ridgeline of the exact sampling densities of sqrt(n) * (Xbar_n - 1) for
  Xbar_n the mean of n Exponential(1) draws (so Xbar_n ~ Gamma(n, rate n)).
  Rows run from n = 2 (skewed) down to the N(0, 1) limit.

Colours come from assets/css/style.css, so the drawing follows the light/dark
theme. Standard library only:  python tools/make_art.py
"""

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "layouts" / "partials" / "art"


def fmt(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


def density(z, n):
    """Density of sqrt(n) * (Xbar_n - 1), Xbar_n ~ Gamma(shape n, rate n)."""
    if n is None:
        return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    x = 1 + z / math.sqrt(n)
    if x <= 0:
        return 0.0
    log_g = n * math.log(n) + (n - 1) * math.log(x) - n * x - math.lgamma(n)
    return math.exp(log_g) / math.sqrt(n)


def convergence_svg():
    ns = [2, 3, 4, 5, 7, 10, 14, 20, 30, 50, 90, 200, 1000, None]
    W = 3600
    cx = W / 2
    unit = 68          # px per standard deviation
    spacing = 11       # px between rows
    amp = 74 / density(0, None)  # the Gaussian peak rises 74 px
    top = 100
    H = top + spacing * (len(ns) - 1) + 10

    # Dense sampling where the curves live, flat tails out to (just past) the edges.
    step = 0.08
    zs = [-(cx + 10) / unit] + [(-4.6 + step * i) for i in range(int(11.2 / step) + 1)] + [(W - cx + 10) / unit]

    rows = []
    last = len(ns) - 1
    for k, n in enumerate(ns):
        base = top + spacing * k
        pts = [(cx + z * unit, round(base - amp * density(z, n), 1)) for z in zs]
        # Drop interior points of flat runs (where the density rounds to zero).
        kept = [p for i, p in enumerate(pts)
                if i in (0, len(pts) - 1) or not (pts[i - 1][1] == p[1] == pts[i + 1][1])]
        line = "M" + "L".join(f"{fmt(x)} {fmt(y)}" for x, y in kept)
        # One path per row: filled in the page colour below the curve so nearer rows
        # hide the ones behind. The closing edges run outside the viewBox, so only
        # the curve itself is stroked on screen.
        d = line + f"L{W + 10} {H + 40}L-10 {H + 40}Z"
        opacity = 0.3 + 0.7 * (k / last) ** 1.3
        rows.append(f'<path stroke-opacity="{opacity:.2f}" d="{d}"/>')

    return (
        f'<svg class="art-convergence" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false" '
        f'preserveAspectRatio="xMidYMax meet">'
        + "".join(rows)
        + "</svg>\n"
    )


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "convergence.html"
    target.write_text(convergence_svg(), encoding="utf-8")
    print(target.name, target.stat().st_size, "bytes")
