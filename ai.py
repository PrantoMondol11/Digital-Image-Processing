import random

ROWS, COLS = 100, 100

DIRT_PROB = 0.2        # 20% dirt
RESTRICTED_PROB = 0.1 # 10% restricted

area = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for i in range(ROWS):
    for j in range(COLS):
        r = random.random()
        if r < RESTRICTED_PROB:
            area[i][j] = -1      # restricted
        elif r < RESTRICTED_PROB + DIRT_PROB:
            area[i][j] = 1       # dirt
        else:
            area[i][j] = 0       # clean

# Example: print a small section
for row in area[:10]:
    print(row[:10])
