def frequency(arr: dict):
    print(arr)
    freq_map = {}
    for j in range(len(arr)):
        if arr[j] in freq_map:
            freq_map[arr[j]] += 1
        else:
            freq_map[arr[j]] = 1
    print(freq_map)

frequency([1,2,3,4,4,5,5,6,5])