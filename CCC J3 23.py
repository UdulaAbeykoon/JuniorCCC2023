x = int(input())  


availability = [[0] * 5 for _ in range(x)]


for i in range(x):
    availability[i] = input().strip()


available_count = [0] * 5
for day in range(5):
    for person in availability:
        if person[day] == 'Y':
            available_count[day] += 1


max_available = max(available_count)


best_days = [day + 1 for day, count in enumerate(available_count) if count == max_available]


print(*best_days, sep=",")

