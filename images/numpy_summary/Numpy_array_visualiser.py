import numpy as np
import seaborn as sns
import matplotlib
import itertools
from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

def pastel(colour, weight=2.4):
    """ Convert colour into a nice pastel shade"""
    rgb = np.asarray(mcolors.to_rgba(colour)[:3])
    # scale colour
    maxc = max(rgb)
    if maxc < 1.0 and maxc > 0:
        # scale colour
        scale = 1.0 / maxc
        rgb = rgb * scale
    # now decrease saturation
    total = rgb.sum()
    slack = 0
    for x in rgb:
        slack += 1.0 - x

    # want to increase weight from total to weight
    # pick x s.t.  slack * x == weight - total
    # x = (weight - total) / slack
    x = (weight - total) / slack

    rgb = [c + (x * (1.0 - c)) for c in rgb]

    return rgb

rows    = ["0", "1"]
columns = ["0", "1"]

arr = np.array([[0.25, 0.6],
                [0.6, 0.25]])

fig = plt.figure()
ax = fig.add_subplot(111)

# make a color map of fixed colors
colour_indices = [i for i in range(-10,10)]
cmap = mcolors.ListedColormap(sns.color_palette('tab20c').as_hex())

boundaries = list(itertools.chain.from_iterable(itertools.repeat(x, 2) for x in colour_indices))
norm = mcolors.BoundaryNorm(boundaries, cmap.N, clip=True)

im = plt.imshow(arr, cmap=cmap, norm=norm)

ax.tick_params(axis=u'both', which=u'both',length=0)

# set major grid lines
major_ticks = np.arange(0.5, 2, 1)
ax.set_xticks(major_ticks)
ax.set_yticks(major_ticks)

# set tick offset
offsetx = matplotlib.transforms.ScaledTranslation(-1.05, 0, fig.dpi_scale_trans)
offsety = matplotlib.transforms.ScaledTranslation(0, 1.05, fig.dpi_scale_trans)

#and label them with the respective list entries
ax.set_xticklabels(rows, weight='bold', Fontsize=14)
ax.set_yticklabels(columns, weight='bold', Fontsize=14)
# change colour of x and y-axis numbers
ax.tick_params(axis='x', colors='gray')
ax.tick_params(axis='y', colors='gray')
# move the tick label positions to the centre
for tick in ax.yaxis.get_majorticklabels():
    tick.set_transform(tick.get_transform() + offsety)

for tick in ax.xaxis.get_majorticklabels():
    tick.set_transform(tick.get_transform() + offsetx)
plt.rc('font', size=15)
# draw thje grid lines
ax.grid(which='major', color='black', linestyle='-', linewidth=1)
'''
# Loop over data dimensions and create text annotations.
for i in range(len(rows)):
    for j in range(len(columns)):
        text = ax.text(i, j, (j,i), ha="center", va="center", color="black")
'''
# Loop over data dimensions and create text annotations.
for i in range(len(rows)):
    for j in range(len(columns)):
        text = ax.text(i, j, arr[j,i], ha="center", va="center", color="black")

fig.tight_layout()
plt.show()
