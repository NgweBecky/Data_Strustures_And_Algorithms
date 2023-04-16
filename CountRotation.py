def count_rotation(number_list):
    position = 0
    while position < len(number_list):
        if position > 0 and number_list(position) < number_list(position-1):
            return position
        position += 1
    return -1