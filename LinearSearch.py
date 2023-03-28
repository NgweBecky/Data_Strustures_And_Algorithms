def locate_number(number_list, target):
    position = 0
    while position < len(number_list):
        if(number_list[position] == target):
            return "Found at position " + str(position)
        position += 1
    else:
        if(len(number_list) == 0):
            return "The List is empty."
        elif(target not in number_list):
            return "Not found."
        return -1

cards= [9,8,7,6,5,4]
print(locate_number(cards,6))
print(locate_number(cards,9))
print(locate_number(cards,4))
print(locate_number(cards,0))
print(locate_number([],6))