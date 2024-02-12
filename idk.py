numbers = {1, 2, 3, 4, 5, 7, 8, 12, 9}

def create_intervals(sets):
    if len(sets) == 0:
        return []
    sets = sorted(list(sets))
    intervals = []
    temp = []
    for i in range(len(sets) - 1):
        current_number = sets[i]
        next_number = sets[i + 1]
        if current_number + 1 == next_number:
            temp.append(current_number)
        else:
            temp.append(current_number)
            temp = (temp[0], temp[-1])
            intervals.append(temp)
            temp = []
    last_number = sets[-1]
    if len(temp) == 0:
        intervals.append((last_number, last_number))
    else:
        temp.append(last_number)
        temp = (temp[0], temp[-1])
        intervals.append(temp)
    return intervals


print(create_intervals(numbers))
