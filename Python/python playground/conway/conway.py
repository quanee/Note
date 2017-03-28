import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def addGlider(i, j, grid):
    """adds a glider with top-left cell at (i, j)"""

    glider = np.array([0, 0, 255],
                      [255, 0, 255],
                      [0, 0, 0])

    grid[i: i + 3, j: j + 3] = glider


def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum using toroidal boundary conditions
            # takes place on a toroidal surface
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1), (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1), (j + 1) % N]) / 255)

            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]

    return img,


# main() function
def main():
    # command line arguments are in sys.argv[1], sys.argv[2], ...
    # sys.argv[0] is the script name and can be ignored
    # parse arguments
    parse = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")