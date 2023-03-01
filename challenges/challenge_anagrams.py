def is_anagram(first_string, second_string):
    str1 = list(first_string.lower())
    str2 = list(second_string.lower())

    sorted_str1 = merge_sort(str1)
    sorted_str2 = merge_sort(str2)

    sorted_s1 = "".join(sorted_str1)
    sorted_s2 = "".join(sorted_str2)

    are_anagrams = (
        sorted_s1 == sorted_s2 and sorted_s1 != "" and sorted_s2 != ""
    )

    return (sorted_s1, sorted_s2, are_anagrams)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged
