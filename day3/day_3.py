def toboggan_trajectory(right,down):
    
    '''right and down are intergers
       right is the slope right and down is the slope down
       tells you how many trees you will hit in the given grid'''
   
    with open("day_3_input.txt", "r") as input_file:
        file_lines = input_file.readlines()
        input_grid = [line.strip() for line in file_lines]

        grid_list = []

        for string in input_grid:
            lists = list(string)
            grid_list.append(lists)

        #print(grid_list) ... to print grid

        trees_hit = 0
        row_index = 0
        col_index = 0

        rows = len(input_grid)
        cols = len(input_grid[0])

        starting_point = grid_list[0][0]

        while row_index < rows - 1: 
            
            if starting_point == '#': 
                    trees_hit +=1
            row_index += down

            if col_index < (cols - right):
                starting_point = grid_list[row_index][col_index + right] 
                col_index += right

            elif col_index >= (cols - right): 
                starting_point = grid_list[row_index][col_index - cols + right]
                col_index = col_index - cols + right

        print('Trees Hit:',trees_hit)

toboggan_trajectory(1,1)
toboggan_trajectory(3,1)
toboggan_trajectory(5,1)
toboggan_trajectory(7,1)
toboggan_trajectory(1,2)

