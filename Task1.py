#Perform basic operations on the list
def add_to_list(lst, element):
    lst.append(element)
    return lst
# Adding element from the list
my_list = [1, 2, 3]
print(add_to_list(my_list, 4)) 

def remove_from_list(lst, element):
    if element in lst:
        lst.remove(element)
    return lst
# Removing element from the list
my_list = [1, 2, 3, 4]
print(remove_from_list(my_list, 3)) 

def update_list(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
    return lst
# Updating element from the list
my_list = [1, 2, 3, 4]
print(update_list(my_list, 2, 5)) 



# Perform basic operations on the Dictionary
def add_to_dict(dct, key, value):
    dct[key] = value
    return dct
# Adding element to the Dictionary
my_dict = {'a': 1, 'b': 2}
print(add_to_dict(my_dict, 'c', 3))  

def remove_from_dict(dct, key):
    if key in dct:
        del dct[key]
    return dct
# Removing element from the Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(remove_from_dict(my_dict, 'b'))  

def update_dict(dct, key, new_value):
    if key in dct:
        dct[key] = new_value
    return dct
# Updating element from the Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(update_dict(my_dict, 'b', 4))  



# Perform basic operations on the Tuple
def add_to_tuple(tup, element):
    return tup + (element,)
# Adding element to the Tuple
my_tuple = (1, 2, 3)
print(add_to_tuple(my_tuple, 4))


def remove_from_tuple(tup, element):
    lst = list(tup)
    if element in lst:
        lst.remove(element)
    return tuple(lst)
# Removing element from the tuple
my_tuple = (1, 2, 3, 4)
print(remove_from_tuple(my_tuple, 3)) 

def update_tuple(tup, index, new_value):
    lst = list(tup)
    if 0 <= index < len(lst):
        lst[index] = new_value
    return tuple(lst)
# Updating element from the tuple
my_tuple = (1, 2, 3, 4)
print(update_tuple(my_tuple, 2, 5))

