fd = open("inputs/inputs.txt")

lines = fd.readlines()

# PART 1
points = {
    5: 50 * (10**10),
    4: 35 * (10**10),
    3: 15 * (10**10),
    2: 5 * (10**10),
    1: 0,
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

score_hands = dict()
for line in lines:
    symbols = {}
    hand, _bid = line.split(" ")
    bid = int(_bid)
    score = 0
    for index, symbol in enumerate(hand):
        score += points[symbol] * (10 ** ((4 - index) * 2))
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1
    for occurences in symbols.values():
        score += points[occurences]
    score_hands[score] = bid

sorted_score_hands = dict(sorted(score_hands.items()))
ans = 0
for index, score_hand in enumerate(sorted_score_hands.items()):
    ans += (index + 1) * score_hand[1]
print(ans)

# PART 2
points = {
    5: 50 * (10**10),
    4: 35 * (10**10),
    3: 15 * (10**10),
    2: 5 * (10**10),
    1: 0,
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 0,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

score_hands = dict()
for line in lines:
    symbols = {}
    hand, _bid = line.split(" ")
    bid = int(_bid)
    score = 0
    for index, symbol in enumerate(hand):
        score += points[symbol] * (10 ** ((4 - index) * 2))
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1
    jokers = 0
    if symbols.get("J"):
        jokers = symbols["J"]
        symbols.pop("J")
    if jokers == 5:
        symbols["K"] = 5
    if jokers != 5:
        key_to_add = list(dict((sorted(symbols.items(), key=lambda x: x[1]))).keys())[
            -1
        ]
        symbols[key_to_add] += jokers
    for occurences in symbols.values():
        score += points[occurences]
    score_hands[score] = bid

sorted_score_hands = dict(sorted(score_hands.items()))
ans = 0
for index, score_hand in enumerate(sorted_score_hands.items()):
    ans += (index + 1) * score_hand[1]
print(ans)
