import re

fd = open("inputs/input.txt")
lines = fd.readlines()

# PART 1
digits = []
for line in lines:
    line_digits = re.findall(r"\d", line)
    digits.append(int(line_digits[0] + line_digits[-1]))
print(sum(digits))

# PART 2
numbers_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

ans = 0
for line in lines:
    first = None
    last = None
    index = -1
    for char in line:
        index += 1
        if char.isdigit():
            if first is None:
                first = ord(char) - ord("0")
            last = ord(char) - ord("0")
        else:
            for number in list(numbers_dict.keys()):
                if line[index:].find(number) == 0:
                    if first is None:
                        first = numbers_dict[number]
                    last = numbers_dict[number]

    if first is not None and last is not None:
        line_value = first * 10 + last
        ans += line_value
print(ans)
