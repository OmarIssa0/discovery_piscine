list = [2, 8, 9, 48, 8, 22, -12, 2]
print(list)
list2 = []
i = 0
while i < len(list):
    if list[i] > 5:
        list2.append(list[i] + 2)
    i += 1
print(list2)