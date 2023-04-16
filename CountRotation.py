def linear_count_rotation(number_list):
    position = 0
    while position < len(number_list):
        if position > 0 and number_list(position) < number_list(position-1):
            return position
        position += 1
    return -1


def binary_count_rotation(number_list):
    # if the middle number is smaller than the last element of the range, then the answer on the left
    # if the middle number is greate than the last element of the range, then the answer on the right
    low = 0
    high = len(number_list)
    mid = (low+high)/2
    mid_num = number_list[mid]
    while low < high:
        if mid > 0 and mid_num < number_list[mid-1]:
            return mid
        elif mid_num < number_list[(len(number_list))]:
            high = mid-1
        else:
            low = mid+1
    return -1