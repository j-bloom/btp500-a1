#    Main Author(s):
#    Main Reviewer(s):

from a1_partc import Queue
import copy

def get_overflow_list(grid):

    overflows = []

    # loop over every row in grid, column by
    # column and set appropriate overflow limit
    # based on coordinate, corners = 2, edges = 3, center = 4
    for index, row in enumerate(grid):
        for column, val in enumerate(row):
            if (column == 0 or column == len(row) - 1) and (index == 0 or index == len(grid) - 1 ):
                overflow = 2
            elif (index == 0 or index == len(grid) - 1) or (column == 0 or column == len(row) - 1):
                overflow = 3
            else:
                overflow = 4

    # check if value at coordinate is negative
    # check if it has overflowed, e.g a corner is -2 or 2
    # Then apped it to list of coordinates that have overflowed
            if val < 0:
                overflow = -overflow
                if val <= overflow:
                    overflows.append((index, column))
            elif val >= overflow:
                overflows.append((index, column))

    # return list of coordinates that have overflowed
    # or None if nothing has
    if overflows:
        return overflows
    else:
        return None

def overflow(grid, a_queue, __count=0):
    # private count variable to track number
    # of changes this recursive loop of overflow
    count = __count

    # get list of tuple pairs of coordinates that have overflowed
    overflows = get_overflow_list(grid)

    # if coordinates have overflowed this branch runs
    if overflows:
        # seperate lists of tuple pairs for coordinates that have increased
        # by 1 because a neighbor has overflowed
        positive_changes = []
        negative_changes = []

        # Check if each value at coordinate is negative or positive
        for coord in overflows:
            if grid[coord[0]][coord[1]] < 0:
                negative = True
            else:
                negative = False

        # Neighbors of this coordinate that will increase by 1
            neighbors = [(coord[0] - 1, coord[1]),
                            (coord[0] + 1, coord[1]),
                            (coord[0], coord[1] - 1),
                            (coord[0], coord[1] + 1)]

        # Remove neighbor coordinates that do not exist, e.g have negative indexes
            valid_neighbors = [(y, x) for y, x in neighbors if (x >= 0 and y >= 0)
                               and (y < len(grid) and x < len(grid[y]))]
        # If the value at this coordinate is negative, add its neighbors to
        # list of negative changes and their signs will become negative
        # else add to list of positive changes and their signs will become positive
            if negative:
                negative_changes.append(valid_neighbors)
            else:
                positive_changes.append(valid_neighbors)

        # deep copy current grid into variable then set overflowed coordinates
        # to 0 in that new grid
        next_grid = copy.deepcopy(grid)
        for coord in overflows:
            next_grid[coord[0]][coord[1]] = 0

        # Process all changes adding 1 to every coordinate
        # in positive_changes and negative_changes and setting their signs
        # as appropriate
        for change in positive_changes:
            for y, x in change:
                val = next_grid[y][x]
                val = abs(val)
                val += 1
                next_grid[y][x] = val

        for change in negative_changes:
            for y, x in change:
                val = next_grid[y][x]
                val = abs(val)
                val += 1
                next_grid[y][x] = -val

        # Add new grid we completed one overflow run of into queue and add 1
        # count variable we will return from this function
        a_queue.enqueue(next_grid)
        count += 1

        # recursively call overflow passing the new grid we created, the current
        # queue and the count for how many grids we've added to the queue so far
        return overflow(next_grid, a_queue, count)

    # return the number of grids added to queue this call to overflow
    return count
