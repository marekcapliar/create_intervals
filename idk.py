def create_intervals(data):
    if len(data) == 0:
        return []
    data = sorted(list(data))
    intervals = []
    temp = []
    for i in range(len(data) - 1):
        current_number = data[i]
        next_number = data[i + 1]
        if current_number + 1 == next_number:
            temp.append(current_number)
        else:
            temp.append(current_number)
            temp = (temp[0], temp[-1])
            intervals.append(temp)
            temp = []
    last_number = data[-1]
    if len(temp) == 0:
        intervals.append((last_number, last_number))
    else:
        temp.append(last_number)
        temp = (temp[0], temp[-1])
        intervals.append(temp)
    return intervals
