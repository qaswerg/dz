def merge_dicts(dict1, dict2):
    merged = {}
    for key, value in dict2.items():
        if key in merged:
            merged[key].append(value)
        else:
            merged[key] = [value,]
    for key, value in dict1.items():
        if key in merged:
            merged[key].append(value)
        else:
            merged[key] = [value,]
    return merged

print(merge_dicts({'a': 5, 'b': 7}, {'a': 4, 'c': 1}))