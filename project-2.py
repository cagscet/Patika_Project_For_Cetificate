my_list = [[1, 2], [3, 4], [5, 6, 7]]
reversed_list =  [sublist[::-1] for sublist in my_list][::-1]
print(reversed_list)