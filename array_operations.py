def reverse_array(arr):
    return arr[::-1]

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result

def find_kth_smallest(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

def demonstrate_data_structures():
    print("\n--- Data Structures Demo ---")
    my_list = [10, 20, 30]
    my_list.append(40)
    print("List (ordered, editable):", my_list)

    my_tuple = (1, 2, 3)
    print("Tuple (ordered, fixed):", my_tuple)

    my_set = {1, 2, 2, 3, 3, 3}
    print("Set (no duplicates):", my_set)

    my_dict = {"name": "Daksh", "course": "CSE", "marks": 90}
    print("Dictionary (key-value pairs):", my_dict)