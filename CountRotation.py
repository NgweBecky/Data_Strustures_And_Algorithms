import time
def linear_count_rotation(number_list):
    position = 0
    while position < len(number_list):
        if position > 0 and number_list[(position)] < number_list[(position-1)]:
            return position
        position += 1
    return -1


def binary_count_rotation(number_list):
    # if the middle number is smaller than the last element of the range, then the answer on the left
    # if the middle number is greate than the last element of the range, then the answer on the right
    low, high = 0, len(number_list)-1
    
    while low <= high:
        mid = (low+high)//2
        mid_num = number_list[mid]
        #print("lo:", low, ", hi:", high, ", mid:", mid, ", mid_number:", mid_num)
        if mid > 0 and mid_num < number_list[mid-1]:
            return mid
        elif mid_num < number_list[(len(number_list)-1)]:
            print(len(number_list))
            high = mid-1
        else:
            low = mid+1
    return -1

num_list = [17,34,-1,6,9,12,15]
start_time = time.time()
print(linear_count_rotation(num_list))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(binary_count_rotation(num_list))
print("--- %s seconds ---" % (time.time()-start_time))