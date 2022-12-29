from bigcock import *

input_data = open('input.txt', 'r').read().split('\n')[:-1]


def day_3_part_1():
    common_items = []
    
    for row in input_data:
        split_items = int(len(row)/2)

        first_compartment = set(row[:split_items])
        second_compartment = set(row[split_items:])

        common_item = list(first_compartment & second_compartment)
        common_items.append(common_item[0])

    sum_of_priorities = 0

    for item in common_items:
        if item.isupper():
            priority = ord(item) - 38
        else:
            priority = ord(item) - 96

        sum_of_priorities += priority

    print(sum_of_priorities)

def split_by_three(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def day_3_part_2():
    list_of_rows_as_sets = []        
    
    for row in input_data:
        row_as_set = set(row)
        list_of_rows_as_sets.append(row_as_set)
    
    common_items = []
    for item_sets_grouped_by_three in split_by_three(list_of_rows_as_sets, 3):
        common_item = list(item_sets_grouped_by_three[0] & item_sets_grouped_by_three[1] & item_sets_grouped_by_three[2])
        common_items.append(common_item[0])

    sum_of_priorities = 0

    for item in common_items:
        if item.isupper():
            priority = ord(item) - 38
        else:
            priority = ord(item) - 96
        
        sum_of_priorities += priority

    print(sum_of_priorities)

#day_3_part_1()
day_3_part_2()
