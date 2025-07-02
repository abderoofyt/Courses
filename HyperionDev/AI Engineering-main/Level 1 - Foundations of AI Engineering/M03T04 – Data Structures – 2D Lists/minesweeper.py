def count_adjacent_mines(grid):
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                result[r][c] = "#"
            else:
                mine_count = sum(
                    1 for dr, dc in directions
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == "#"
                )
                result[r][c] = str(mine_count)
    return result

# Example usage
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = count_adjacent_mines(grid)
for row in result:
    print(" ".join(row))
