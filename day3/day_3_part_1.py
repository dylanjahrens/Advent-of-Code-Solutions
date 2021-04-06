#Sloppy first draft, only calculates the slope 3 right 1 down
#Other file will take in any slope with a function!!!

with open("day_3_input.txt", "r") as input_file:
    file_lines = input_file.readlines()
    input_grid = [line.strip() for line in file_lines]

    grid_list = []

    for string in input_grid:
        lists = list(string)
        grid_list.append(lists)

    #print(grid_list) to print grid

    #grid list is a list of lists of strings
    #input_grid is a list of strings

    trees_hit = 0
    row_index = 0
    col_index = 0
    #file is 31 columns wide and 323 rows long
    starting_point = grid_list[0][0]

    while row_index < 322: 
        
        if starting_point == '#': 
                trees_hit +=1
        row_index += 1

        if col_index < 28:
            starting_point = grid_list[row_index][col_index + 3] 
            #down 1 and right 3, starts on second row (index 1)
            col_index += 3

        elif col_index == 28: 
            starting_point = grid_list[row_index][0]
            #goes back to the first item in the next row
            col_index = 0

        elif col_index == 29: #30, 31, 1
            starting_point = grid_list[row_index][1]
            #goes to the second item in the next row
            col_index = 1
        
        elif col_index == 30:
            starting_point = grid_list[row_index][2]
            #goes to the third item in the next row
            col_index = 2
    
    print(trees_hit)
    
