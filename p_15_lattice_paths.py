def latticePaths(gridSize):
    grid = []
    for i in range(0, gridSize+1):
        grid.append([])
        for j in range(0, gridSize+1):
            if (i == 0 or j == 0):
                grid[i].append(1)
            else:
                grid[i].append(grid[i - 1][j] + grid[i][j-1])

    return grid[gridSize][gridSize]

print(latticePaths(2))