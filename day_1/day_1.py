with open('input.txt', 'r') as file:
    data = file.read().replace("\n",",").split(",")
    elves = []
    sum = 0
    for val in data:
        try:
            n = int(val)
            sum = sum + n
        except ValueError:
            elves.append(sum)
            sum = 0

    elves.sort()
    elves.reverse()

    print(elves[0])
    print(elves[0] + elves[1] + elves[2])




