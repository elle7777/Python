#Revers Array rotaion
#verion 0.1.0
#@Iustin Desrobitu

def array_rotation(number_list):
    temp_list = number_list.copy()
    temp_number = number_list[0]
    temp_list.pop(0)
    new_list = temp_list.copy()
    new_list.append(temp_number)
    return new_list

def array_rotation_iteration(number_list, rotation):
    counter = 0
    if rotation == 0:
        return number_list
    new_list = array_rotation(number_list)
    while counter < rotation - 1:
        new_list = array_rotation(new_list)
        array_rotation(new_list)
        counter += 1
    return new_list    

print("This Pogram rotates an array of numbers to the left by an amount")
rotaion = int(input("insert the number of steps: "))

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{number_list} before rotation")
print(f"{array_rotation_iteration(number_list, rotaion)} after the rotation")