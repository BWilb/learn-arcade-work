#15, 57, 14, 33, 72, 79, 26, 56, 42, 40
"""if number after next number is greater than current number; position is fine
However if number after next number is less than current number; position will be pushed back
14 is pushed to position zero
15 is pushed to position one
26 is pushed to position two (26 is next smallest, swap 26 to position two)
33 is next smallest, swap to position 3

"""
def selection_sort(my_list):
    for cur_position in range (len(my_list)):
        min_value = cur_position
        for scan_pos in range(cur_position + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_value]:
                min_value = scan_pos
        #swap
        temp = my_list[min_value]
        my_list[min_value] = my_list[cur_position]
        my_list[cur_position] = temp

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

selection_sort(my_list)
print(my_list)

"""
n = 10, 10 * 5 = 50
n = 100, 100 * 50 = 5000
n = 1000, 1000 * 500 = 500,000

n * (n / 2) --> how many times I expect this to run --> inside loop
"""