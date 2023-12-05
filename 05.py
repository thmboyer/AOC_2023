import re

fd = open("inputs/inputs.txt")
lines = fd.readlines()

# PART 1
seeds = list(map(int, re.findall(r"\d+", lines[0])))

line_index = 0
while line_index < len(lines) - 1:
    line_index += 1
    if lines[line_index].find(":"):
        new_seeds = seeds.copy()
        while True:
            line_index += 1
            if line_index >= len(lines):
                break
            numbers = list(map(int, re.findall(r"\d+", lines[line_index])))
            if len(numbers) == 0:
                break
            for seed_index, seed in enumerate(seeds):
                if seed >= numbers[1] and seed < numbers[1] + numbers[2]:
                    new_seeds[seed_index] = numbers[0] + seed - numbers[1]
        seeds = new_seeds.copy()
print(min(seeds))

# PART 2

seeds = list(map(int, re.findall(r"\d+", lines[0])))
seeds_intervals = []
for seed_and_number in zip(seeds[0::2], seeds[1::2]):
    seeds_intervals.append(
        (seed_and_number[0], seed_and_number[0] + seed_and_number[1])
    )

line_index = 0
while line_index < len(lines) - 1:
    line_index += 1
    if lines[line_index].find(":"):
        new_seeds_intervals = []
        while True:
            line_index += 1
            if line_index >= len(lines):
                break
            numbers = list(map(int, re.findall(r"\d+", lines[line_index])))
            if len(numbers) == 0:
                break
            numbers_interval = (numbers[1], numbers[1] + numbers[2])
            new_seeds_temp = seeds_intervals.copy()
            for seed in seeds_intervals:
                if seed[0] > numbers_interval[1] or seed[1] <= numbers_interval[0]:
                    continue
                new_seeds_temp.remove(seed)
                if seed[0] >= numbers_interval[0] and seed[1] > numbers_interval[1]:
                    new_seeds_intervals.append(
                        (
                            numbers[0] + seed[0] - numbers_interval[0],
                            numbers[0] + numbers[2],
                        )
                    )
                    new_seeds_temp.append((numbers_interval[1], seed[1]))
                elif seed[0] >= numbers_interval[0] and seed[1] <= numbers_interval[1]:
                    new_seeds_intervals.append(
                        (
                            numbers[0] + seed[0] - numbers_interval[0],
                            numbers[0] + seed[1] - numbers_interval[0],
                        )
                    )
                elif seed[0] < numbers_interval[0] and seed[1] > numbers_interval[1]:
                    new_seeds_intervals.append((numbers[0], numbers[0] + numbers[2]))
                    new_seeds_temp.append((seed[0], numbers_interval[0]))
                    new_seeds_temp.append((numbers_interval[1], seed[1]))
                elif seed[0] < numbers_interval[0] and seed[1] <= numbers_interval[1]:
                    new_seeds_intervals.append(
                        (numbers[0], numbers[0] + seed[1] - numbers_interval[0])
                    )
                    new_seeds_temp.append((seed[0], numbers_interval[0]))
            seeds_intervals = new_seeds_temp.copy()
        seeds_intervals.extend(new_seeds_intervals.copy())

print(min([seed[0] for seed in seeds_intervals]))
