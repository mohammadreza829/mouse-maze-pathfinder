from random import randint

matrix = [[0] * 12 for _ in range(12)]


for i in range(1, 11):  
    for j in range(1, 11):  
        matrix[i][j] = randint(0, 1)


print("Initial Matrix:")
for i in range(1, 11):  
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()


mouse_row = int(input("\nEnter mouse row (1-10): "))
mouse_col = int(input("Enter mouse col (1-10): "))


cheese_row = int(input("Enter cheese row (1-10): "))
cheese_col = int(input("Enter cheese col (1-10): "))

if matrix[mouse_row][mouse_col] != 1:
    print("Error: Mouse is on a wall! (Cell value must be 1)")
    exit()

if matrix[cheese_row][cheese_col] != 1:
    print("Error: Cheese is on a wall! (Cell value must be 1)")
    exit()


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]



def find_path(current_row, current_col, cheese_row, cheese_col):
  
    if current_row == cheese_row and current_col == cheese_col:
        return True

 
    matrix[current_row][current_col] = 2

 
    for direction in directions:
        new_row = current_row + direction[0]
        new_col = current_col + direction[1]

        
        if 1 <= new_row <= 10 and 1 <= new_col <= 10:
            if matrix[new_row][new_col] == 1:
                print(f"Moving to: ({new_row}, {new_col})")
                if find_path(new_row, new_col, cheese_row, cheese_col):
                    return True

    
    return False



print("\nSearching for path...")
result = find_path(mouse_row, mouse_col, cheese_row, cheese_col)


if result:
    print("\ncheese founded")
else:
    print("\nNo path found!")


print("\nFinal Matrix (2 = visited cells):")
for i in range(1, 11):
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()
