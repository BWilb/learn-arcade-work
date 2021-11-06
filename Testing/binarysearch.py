def read_in_file(file_name):
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    key = "morgina the shrew"
    my_file = open(file_name)

    # Create an empty list to store our names
    name_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        name_list.append(line)

    my_file.close()
    lower_boud = 0
    upper_bound = len(name_list) - 1
    found = False
    while lower_boud <= upper_bound and not found:
        middle_pos = (lower_boud + upper_bound) // 2

        if name_list[middle_pos] < key:
            lower_boud = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
        print("found at position ", middle_pos)
    else:
        print("not found")
def main():
    read_in_file()

main()