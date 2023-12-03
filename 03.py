fd = open("inputs/inputs.txt")
content = fd.read().strip()
lines = content.split("\n")

newlines = []
newlines.append("." * (len(lines[0]) + 2))
for line in lines:
    newlines.append("." + line + ".")
newlines.append("." * (len(lines[0]) + 2))


# PART 1
add_number = False
inside_number = False
number = 0
part_numbers = []
for line_index, line in enumerate(lines):
    if add_number:
        part_numbers.append(number)
    number = 0
    add_number = False
    inside_number = False
    for element_index, element in enumerate(line):
        if element.isdigit():
            if not inside_number:
                number = int(element)
                inside_number = True
                add_number = False
            else:
                number = number * 10 + int(element)
            if not add_number:
                for i in range(line_index, line_index + 3):
                    for j in range(element_index, element_index + 3):
                        if (not newlines[i][j].isdigit()) and newlines[i][j] != ".":
                            add_number = True
        else:
            if add_number:
                part_numbers.append(number)
            inside_number = False
            add_number = False
            number = 0
print(sum(part_numbers))

# PART 2
gear_ratios = []
for line_index, line in enumerate(lines):
    for element_index, element in enumerate(line):
        if element != "*":
            continue
        digits = []
        for i in range(line_index, line_index + 3):
            j = element_index
            while j <= element_index + 2:
                if newlines[i][j].isdigit():
                    while newlines[i][j - 1].isdigit():
                        j -= 1
                    digit = 0
                    increment = 1
                    while newlines[i][j].isdigit():
                        digit = digit * 10 + int(newlines[i][j])
                        j += 1
                    digits.append(digit)
                else:
                    j += 1
        if len(digits) == 2:
            gear_ratios.append(digits[0] * digits[1])
print(sum(gear_ratios))
