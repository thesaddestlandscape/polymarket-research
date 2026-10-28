from statistics import NormalDist
N = NormalDist()
def tm(s, c): z = c / s; return s * N.pdf(z) / (1 - N.cdf(z))
rows = []
for s in (0.8, 1.3, 2.0, 2.6):
    for c in (-1.0, -0.5, 0.5):
        rows.append('| %.1f | %+.1f | %.0f %% | %+.2f |' % (s, c, 100 * N.cdf(c / s), tm(s, c)))
tab = '\n'.join(rows)
cap = ' ; '.join('sigma %.1f pp: %.2f pp' % (s, 0.798 * s) for s in (0.8, 1.3, 2.0))
txt = open('PREREG_TEMPLATE.md').read().replace('@@TABLA@@', tab).replace('@@CAP@@', cap)
open('PREREG_FORMULA_R2.md', 'w').write(txt)
