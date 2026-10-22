def count_items(values:  list) -> dict:
    count_dict = {}
    for value in values:
        count_dict[value] = count_dict.get(value, 0) + 1
    return count_dict

def unique_sorted(values):
    unique = sorted(list(set(values)))
    return unique

def common(first, second):
    common = set(first) & set(second)
    return sorted(list(common))

def only_in_first(first, second):
    only_in_first = set(first) - set(second)
    return sorted(list(only_in_first))