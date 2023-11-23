import time


def create_empty_grid(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


def print_grid(grid):
    print("\033[H\033[3J", end="")
    for row in grid:
        print("".join(["█" if cell else " " for cell in row]))
    print()


def initialize_grid(grid, start_points):
    for x, y in start_points:
        grid[y][x] = 1


def count_neighbors(grid, x, y):
    height, width = len(grid), len(grid[0])
    neighbors = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ]
    count = 0
    for nx, ny in neighbors:
        if 0 <= nx < width and 0 <= ny < height:
            count += grid[ny][nx]
    return count


def update_grid(grid):
    height, width = len(grid), len(grid[0])
    new_grid = create_empty_grid(width, height)

    for y in range(height):
        for x in range(width):
            cell = grid[y][x]
            neighbors = count_neighbors(grid, x, y)

            if cell == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1

    return new_grid


def center_pattern(pattern, grid_width, grid_height):
    # Calculate the center of the grid
    center_x = grid_width // 2
    center_y = grid_height // 2

    # Calculate the offset to center the pattern
    offset_x = center_x - (max(x for x, y in pattern) + 1) // 2
    offset_y = center_y - (max(y for x, y in pattern) + 1) // 2

    # Adjust the pattern coordinates based on the offset
    centered_pattern = [(x + offset_x, y + offset_y) for x, y in pattern]

    return centered_pattern


def main():
    # Specify the width and height of the grid
    width = 50
    height = 25

    # Specify the initial starting points (x, y coordinates) as a list of tuples
    start_points = [(1, 0), (0, 1), (2, 1), (1, 2), (1, 3), (1, 4), (1, 5), (0, 6), (2, 6), (1, 7)]

    grid = create_empty_grid(width, height)
    initialize_grid(grid, center_pattern(start_points, width, height))

    while True:
        print_grid(grid)
        time.sleep(0.1)
        grid = update_grid(grid)


if __name__ == "__main__":
    main()
