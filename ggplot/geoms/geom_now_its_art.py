from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.image as mpimg
from .geom import geom
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))


class geom_now_its_art(geom):

    def _plot_unit(self, data, ax):
        img = mpimg.imread(os.path.join(_ROOT, 'bird.png'))
        ax.imshow(img, alpha=0.5)
        print ("Put a bird on it!")
