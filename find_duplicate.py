s = [1, 2, 3, 2, 1]
temp = []


def find_first_occurrence_duplicate(lst):
    for x in lst:
        if x in temp:
            return x
        else:
            temp.append(x)


print(find_first_occurrence_duplicate(s))
