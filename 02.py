import re

fd = open("inputs/input.txt")
content = fd.read().strip()

# PART 1
limits = {"red": 12, "green": 13, "blue": 14}

valid_games = []

for index, line in enumerate(content.split("\n")):
    digits = re.findall(r"\d+", line)[1:]
    colors = re.findall(r"[a-z]+", line)[1:]
    valid_games.append(index + 1)
    for index_digit, digit in enumerate(digits):
        if int(digit) > limits[colors[index_digit]]:
            valid_games.pop()
            break

print(sum(valid_games))

# PART 2
powers = []
for index, line in enumerate(content.split("\n")):
    digits = re.findall(r"\d+", line)[1:]
    colors = re.findall(r"[a-z]+", line)[1:]
    minimum_per_color = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for index_digit, digit in enumerate(digits):
        if int(digit) > minimum_per_color[colors[index_digit]]:
            minimum_per_color[colors[index_digit]] = int(digit)
    ans = 1
    for value in minimum_per_color.values():
        ans *= value
    powers.append(ans)

print(sum(powers))
