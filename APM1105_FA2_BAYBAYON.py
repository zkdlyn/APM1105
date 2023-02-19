'''
Write a Python function to multiply
all the numbers in a list.

import numpy

def multiply_list(numlist):
    product = 1
    for number in numlist:
        product = product number
    return product

list = [1, 2, -2]

print(multiply_list(list))
'''

'''
# fixed list
def multiply_list(num):
    x = 1
    for n in num:
        print(x, 'x', n, '=', x*n)
        x = x * n
    return x

num_list = [1, 2, 3, 4, 5]

print(multiply_list(num_list))
'''

# list by user
your_num_list = []
print("This program multiplies the user's given set of numbers")

while True:
    num_entry = input('Enter a number: ')
    if num_entry =='':
        break
    else:
        your_num_list.append(int(num_entry))

def multiply_list(num):
    x = 1
    for n in num:
        x = x * n
    return x

print(multiply_list(your_num_list))

# grid with user input

def draw_grid(row, col):
  r = ('+ _ _ _ _ ' * col + '+')
  c = ('\n' +  '|         ' * (col+1))
  return ((r+3*c) + '\n')*row + r


row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
print(draw_grid(row,col))