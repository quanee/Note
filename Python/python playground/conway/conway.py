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

    # add arguments
    parse.add_argument('--grid-size', dest='N', required=False)
    parse.add_argument('--mov-file', dest='movfile', required=False)
    parse.add_argument('--interval', dest='interval', required=False)
    parse.add_argument('--glider', action='store_true', required=False)
    parse.add_argument('--gosper', action='store_true', required=False)
    args = parse.parse_args()

    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])
    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N * N).reshape(N, N)
        addGlider(1, 1, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = randomGrid(N)

    # set up the animation