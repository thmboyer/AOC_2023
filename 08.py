import math
import re

fd = open("inputs/inputs.txt")
lines = fd.read().strip().split("\n")

instructions = lines[0]

haunted_wasteland = lines[2:]

# PART 1
mapping = dict()
for location in haunted_wasteland:
    points = re.findall(r"[A-Z]+", location)
    mapping[points[0]] = (points[1], points[2])

next_point = "AAA"
index = 0
nb_instructions = len(instructions)
while next_point != "ZZZ":
    next_point = mapping[next_point][instructions[index %
                                                  nb_instructions] == "R"]
    index += 1
print(index)


# PART 2
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


mapping = dict()
for location in haunted_wasteland:
    points = re.findall(r"[1-9A-Z]+", location)
    mapping[points[0]] = (points[1], points[2])

next_points = []
for point in mapping.keys():
    if point[len(point) - 1] == "A":
        next_points.append(point)

index = 0
number_of_instructions = len(instructions)
first_finishes = []
while len(next_points):
    indexes_to_remove = []
    for point_index in range(len(next_points)):
        next_points[point_index] = mapping[next_points[point_index]][
            instructions[index % number_of_instructions] == "R"
        ]
        if next_points[point_index][len(next_points[point_index]) - 1] == "Z":
            indexes_to_remove.append(point_index)
    index += 1
    for index_to_remove in indexes_to_remove:
        next_points.pop(index_to_remove)
        first_finishes.append(index)

while len(first_finishes) != 2:
    first_finishes[0] = lcm(first_finishes[0], first_finishes[1])
    first_finishes.pop(1)
print(lcm(first_finishes[0], first_finishes[1]))
