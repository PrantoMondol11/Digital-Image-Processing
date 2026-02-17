import random

SIZE = 90
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

buildings = [
    (19, 10),
    (19, 25),
    (19, 45),
    (19, 65),
    (64, 10),
    (64, 25),
    (64, 45),
    (64, 65)
]


for br, bc in buildings:
    for i in range(br, br + 6):
        for j in range(bc, bc + 6):
            grid[i][j] = -1


NUM_BIOHAZARDS = 400
placed = 0

while placed < NUM_BIOHAZARDS:
    r = random.randint(0, SIZE - 1)
    c = random.randint(0, SIZE - 1)

    if grid[r][c] == 0: 
        grid[r][c] = 1
        placed += 1

building_coords = []
biohazard_coords = []

for i in range(SIZE):
    for j in range(SIZE):
        if grid[i][j] == -1:
            building_coords.append((i, j))
        elif grid[i][j] == 1:
            biohazard_coords.append((i, j))

print("\n BUILDING COORDINATES (-1):")
for coord in building_coords:
    print(f"BUILDINGS at:{coord}")

print("\n BIOHAZARD COORDINATES (1):")
for coord in biohazard_coords:
    print(f" BIO Hazards:{coord}")


print("\nSUMMARY")
print("Total building cells:", len(building_coords))
print("Total biohazards:", len(biohazard_coords))
