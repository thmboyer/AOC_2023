import re

fd = open("inputs/inputs.txt")
lines = fd.readlines()

# PART 1
times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

time_distance_list = list(zip(times, distances))
print(time_distance_list)

number_of_options = [0] * len(time_distance_list)
ans = 1
for index, time_distance in enumerate(time_distance_list):
    for i in range(time_distance[0]+1):
        distance = (time_distance[0] - i) * i
        if distance > time_distance[1]:
            number_of_options[index] += 1
    ans *= number_of_options[index]

print(ans)

# PART 2
time = int(('').join(list(re.findall(r"\d+", lines[0]))))
distance = int(('').join(list(re.findall(r"\d+", lines[1]))))

ans = 0
for i in range(time+1):
    distance_i = (time - i) * i
    if distance_i > distance:
        ans += 1
print(ans)
