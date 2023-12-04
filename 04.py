import re

fd = open("inputs/inputs.txt")
content = fd.read().strip()

# Part 1
ans = 0
for line in content.split("\n"):
    _, numbers = line.split(":")
    winning, elf = numbers.split("|")
    winning_numbers = set(map(int, re.findall(r"\d+", winning)))
    elf_numbers = set(map(int, re.findall(r"\d+", elf)))
    common_numbers = winning_numbers & elf_numbers
    if len(common_numbers) > 0:
        ans += 2 ** (len(common_numbers) - 1)
print(ans)

# Part 2
number_of_cards = [1] * len(content.split("\n"))
for index, line in enumerate(content.split("\n")):
    _, numbers = line.split(":")
    winning, elf = numbers.split("|")
    winning_numbers = set(map(int, re.findall(r"\d+", winning)))
    elf_numbers = set(map(int, re.findall(r"\d+", elf)))
    common_numbers = winning_numbers & elf_numbers
    for i in range(index + 1, index + 1 + len(common_numbers)):
        number_of_cards[i] += number_of_cards[index]
print(sum(number_of_cards))
