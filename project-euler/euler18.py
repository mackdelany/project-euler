import numpy as np

base_triangle = np.zeros((15, 15))
value_triangle = np.zeros((15, 15))

list_of_row_lists = [[75], 
                    [95, 64], 
                    [17, 47, 82], 
                    [18, 35, 87, 10],
                    [20, 4, 82, 47, 65],
                    [19, 1, 23, 75, 3, 34], 
                    [88, 2, 77, 73, 7, 63, 67], 
                    [99, 65, 4, 28, 6, 16, 70, 92],
                    [41, 41, 26, 56, 83, 40, 80, 70, 33], 
                    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
                    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                    [91, 72, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
                    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for row_list in list_of_row_lists:

    base_triangle[(len(row_list)-1), :(len(row_list))] = np.array(row_list).reshape(1,-1)

value_triangle[-1, :] = base_triangle[-1, :]

for i in range(-13,1): 
    i = -i
    for j in range(i+1):

        value_triangle[i, j] = base_triangle[i, j] + max(value_triangle[i+1, j], value_triangle[i+1, j+1])

print('The maximum possible value is {}'.format(value_triangle[0,0]))



