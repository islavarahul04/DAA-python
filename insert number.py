def insert_number(lst, num, pos):
    lst.insert(pos, num)
    return lst

# Example usage
my_list = [1, 2, 3, 5, 6]
number_to_insert = 4
position_to_insert = 3
new_list = insert_number(my_list, number_to_insert, position_to_insert)
print("List after insertion:", new_list)
