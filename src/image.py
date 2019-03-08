import numpy as np
import os
from skimage import color
from scipy.misc import imsave


class Image:
    def __init__(self):
        self.array = np.zeros((500, 500, 3), dtype='float32')

    def initialize(self):
        for y in range(self.array.shape[1]):
            self.array[:, y, :] = y / self.array.shape[0], .9, .9

    def randomize(self):
        for x in range(self.array.shape[0]):
            np.random.shuffle(self.array[x, :, :])

    def save(self, name):
        rgb = color.convert_colorspace(self.array, 'HSV', 'RGB')
        imsave(name, rgb)

    def make_frames(self, algorithm):
        max_steps = 0
        steps = []

        for dimension in range(self.array.shape[0]):
            new_moves = algorithm.sort(self.array[dimension, :, 0])

            if len(new_moves) > max_steps:
                max_steps = len(new_moves)
            steps.append(new_moves)

        current_step = 0

        # 24 fps, and we want a 5 second gif 24 * 5 = 120 total frames
        total_frames = 120
        step_size = max_steps // total_frames
        current_frame = 0

        os.makedirs(algorithm.name, exist_ok=True)

        while current_step < max_steps:
            for i in range(self.array.shape[0]):
                if current_step < len(steps[i]) - 1:
                    self.swap_pixels(self.array, i, steps[i][current_step])

            if current_step % step_size == 0:
                path = '{}/{:05d}.png'.format(algorithm.name, current_frame)
                imsave(path,
                       color.convert_colorspace(self.array, 'HSV', 'RGB'))
                current_frame += 1
            current_step += 1

    def swap_pixels(self, array, row, places):
        tmp = array[row, places[0], :].copy()
        array[row, places[0], :] = array[row, places[1], :]
        array[row, places[1], :] = tmp
