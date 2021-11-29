
#1. 15 57 14 33 72 79 26 56 42 40

#2. 14 15 57 33 72 79 26 56 42 40

#3. 14 15 33 57 72 79 26 56 42 40

#4. 14 15 33 57 72 79 26 56 42 40

#5. 14 15 26 33 57 72 79 56 42 40

#6. 14 15 26 33 56 57 72 79 42 40


def insertion_sort(my_list):
    for key_position in range(1, len(my_list)):
        key_value = my_list[key_position]
        scan_position = key_position - 1
        while (scan_position >= 0) and (my_list[scan_position] > key_value):
            my_list[scan_position + 1] = my_list[scan_position]
            scan_position -= 1
        my_list[scan_position + 1] = key_value

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)

"""average cases 
n = 10, 10 * 2.5 = 25
n = 100, 100 * 25 = 2500
n = 1000, 1000 * 25 = 250000
n * (n / 4)
"""

"""Best Case
n = 10, 10 * 1 = 10
n = 100, 100 * 1 = 100
n = 1000, 1000 * 1 = 1000
n
"""