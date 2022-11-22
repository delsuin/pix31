def bresenham_line(origin, pos):
    """
    Draws a line between two positions using Bresenham's line algorithm. 
    Mode tells if the line is a line of pixels (0) or a line of pixels to erase (1).
    """
    line = []

    x0, y0 = origin[0], origin[1]
    x1, y1 = pos[0], pos[1]

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            line.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            line.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    line.append((x, y))

    return line

def flood_fill(origin, canvas):
    """
    "Paint bucket tool"
    """
    area = []

    posList = []                                                # a list for possible fillable positions
    canvasCopy = canvas.copy()
    posList.append((origin[0], len(canvasCopy) - 1 - origin[1]))    # add the clicked position to the list
    prevColor = canvasCopy[origin[1]][origin[0]]                # check the original color that will be recolored
    newColor = [x+1 for x in prevColor]

    while posList:
        pos = posList.pop()                      # take one position out of the list
        if canvasCopy[pos[1]][pos[0]] == prevColor:
            area.append((pos[0], len(canvasCopy) - 1 - pos[1]))
            canvasCopy[pos[1]][pos[0]] = newColor

            # check pos from upside
            x, y = pos[0], pos[1] - 1
            if y >= 0 and x >= 0 and y < len(canvasCopy) and x < len(canvasCopy[pos[1]]):
                if canvasCopy[y][x] == prevColor:
                    posList.append((x, y))

            # check pos from downside
            y = pos[1] + 1
            if y >= 0 and x >= 0 and y < len(canvasCopy) and x < len(canvasCopy[pos[1]]):
                if canvasCopy[y][x] == prevColor:
                    posList.append((x, y))

            # check pos from left side
            x, y = pos[0] - 1, pos[1]
            if y >= 0 and x >= 0 and y < len(canvasCopy) and x < len(canvasCopy[pos[1]]):
                if canvasCopy[y][x] == prevColor:
                    posList.append((x, y))

            # check pos from right side
            x = pos[0] + 1
            if y >= 0 and x >= 0 and y < len(canvasCopy) and x < len(canvasCopy[pos[1]]):
                if canvasCopy[y][x] == prevColor:
                    posList.append((x, y))

    return area

def rectangle(origin, pos):
    """
    Rectangle
    """
    # TODO: if x1 or y1 smaller than 0 counterpart
    path = []

    x0, y0 = origin[0], origin[1]
    x1, y1 = pos[0], pos[1]

    for i in range(x0, x1+1):
        path.append((i, y0))
        path.append((i, y1))

    for j in range(y0+1, y1):
        path.append((x0, j))
        path.append((x1, j))
