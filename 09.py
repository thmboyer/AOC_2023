import re

fd = open("inputs/inputs.txt")
histories = fd.read().strip().split("\n")


def extrapolation(history: list[int], part: int) -> int:
    new_history = extrapolate(history, part)
    if part == 1:
        return history[len(history) - 1] + new_history[len(new_history) - 1]
    else:
        return history[0] - new_history[0]


def extrapolate(history: list[int], part: int) -> list[int]:
    last_call = True
    for element in history:
        if element != 0:
            last_call = False
    if last_call:
        history.append(0)
        return history
    new_history = []
    for i in range(len(history) - 1):
        new_history.append(history[i + 1] - history[i])
    new_new_history = extrapolate(new_history, part)
    if part == 1:
        new_history.append(
            new_history[len(new_history) - 1]
            + new_new_history[len(new_new_history) - 1]
        )
    elif part == 2:
        new_history.insert(
            0,
            new_history[0] - new_new_history[0],
        )
    return new_history


# PART 1
extrapolations = []
for history in histories:
    extrapolations.append(
        extrapolation(list(map(int, re.findall(r"-?\d+", history))), 1)
    )
print(sum(extrapolations))

# PART 2
extrapolations = []
for history in histories:
    extrapolations.append(
        extrapolation(list(map(int, re.findall(r"-?\d+", history))), 2)
    )
print(sum(extrapolations))
