def locate_number(number_list, target):
    # Assume the list is in descending order
    low, high = 0, len(number_list)-1
    while low <= high:
        mid = (low+high)//2
        mid_number = number_list[mid]
        if mid_number == target:
            return "Found at position " + str(mid)
        elif mid_number < target:
            high = mid - 1
        elif mid_number > target:
            low = mid + 1
    return "Not Found"

cards= [9,8,7,6,5,4]
print(locate_number(cards,6))
print(locate_number(cards,9))
print(locate_number(cards,4))
print(locate_number(cards,0))
print(locate_number([],6))