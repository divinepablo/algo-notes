import numpy as np

import matplotlib.pyplot as plt

def create_maze(width, height):
    maze = np.ones((height, width), dtype=bool)
    # maze = [['#'] * width for _ in range(height)]
    start_x, start_y = 1, 1
    maze[start_y][start_x] = False

    def dfs(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        np.random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == True:
                maze[ny - dy][nx - dx] = False
                maze[ny][nx] = False
                dfs(nx, ny)
    dfs(start_x, start_y)
    return maze

def plot_maze(maze, filename):
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap='binary')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()

if __name__ == "__main__":
    width, height = 21, 21  # Dimensions of the maze
    maze = create_maze(width, height)
    plot_maze(maze, 'maze.png')