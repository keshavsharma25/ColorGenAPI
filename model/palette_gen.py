import scipy.cluster
from colormap import rgb2hex


class PaletteGenerator:
    def __init__(self, n_colors=4):
        self.n_colors = n_colors
        self.palette_list = list()

    def create_palette(self, data):

        codes, _ = scipy.cluster.vq.kmeans(data, self.n_colors)

        for code in codes:
            if len(code) == 4:
                code = code[:3]
            self.palette_list.append(rgb2hex(*code.astype(int)))

        return self.palette_list
