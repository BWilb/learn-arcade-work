my_list = []

if "apple" in my_list:
    print("yes")
else:
    print("no")
my_list.append("Bubble")
my_list.insert(0, "Google")
print(my_list)
my_list.pop()
print(my_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[::3])