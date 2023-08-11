#! /usr/bin/python

"""
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. 
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

"""

def print_table(string_list):
    # which will create a list containing the same number of 0 values 
    # as the number of inner lists in string_list
    col_width = [0] * len(string_list)

    # set value to col_width to justify list accordingly
    for l in range(len(string_list)):
        for i in range(len(string_list[l])):
            if len(string_list[l][i]) > col_width[l]:
                col_width.pop(l)
                col_width.insert(l, len(string_list[l][i]))

    # print table
    for l in range(len(string_list[0])):
        for i in range(len(string_list)):
            #print(string_list[i][l],end="")
            justified = string_list[i][l].rjust(col_width[i])
            print(justified + " ", end="")
        print()

test = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"]
]

print_table(test)
