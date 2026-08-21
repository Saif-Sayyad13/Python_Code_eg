'''rows=int(input('enter rows'))
columns=int(input('enter columns'))
for row in range(rows):
    for col in range(columns):
        print('*',end=" ")
    print()
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * '''

'''rows=int(input('enter rows'))
columns=int(input('enter columns'))
for row in range(rows):
    for col in range(columns):
        if row==col:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()
*         
  *       
    *     
      *   
        * '''
        
'''rows=int(input('enter rows'))
columns=int(input('enter columns'))
for row in range(rows):
    for col in range(columns):
        if row+col==rows-1:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()
        * 
      *   
    *     
  *       
* '''

'''rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for row in range(rows):
    for col in range(columns):
      # row == col checks the main diagonal (\)
        # row + col == rows - 1 checks the anti-diagonal (/)
        if row == col or row + col == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
*       * 
  *   *   
    *     
  *   *   
*       * '''

'''
rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for row in range(rows):
    for col in range(columns):
        # col <= row prints the standard left triangle
        # row == rows - 1 completely fills the very last row
        if col <= row or row == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
*         
* *       
* * *     
* * * *   
* * * * * '''


'''rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for row in range(rows):
    for col in range(columns):
        # row + col < rows ensures the number of stars decreases each row
        if row + col < rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
* * * * * 
* * * *   
* * *     
* *       
* '''

'''rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for row in range(rows):
    for col in range(columns):
        # col >= row leaves empty spaces on the left and prints stars on the right
        if col >= row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
* * * * * 
  * * * * 
    * * * 
      * * 
        * '''
        
'''rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for row in range(rows):
    for col in range(columns):
        # row + col >= rows - 1 prints stars on and below the anti-diagonal
        if row + col >= rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
        * 
      * * 
    * * * 
  * * * * 
* * * * * '''

'''
import os
import time

# Frame 1: Legs open, arms forward/back
frame1 = [
    "   O   ",
    "  /|\\  ",
    "  / \\  "
]

# Frame 2: Legs bent, arms pumping
frame2 = [
    "   O   ",
    "  <|>  ",
    "  /  > "
]

frames = [frame1, frame2]
screen_width = 40  # How far the man will run

# Clear screen command based on Operating System
clear_command = 'cls' if os.name == 'nt' else 'clear'

try:
    for step in range(screen_width):
        # 1. Clear the terminal screen
        os.system(clear_command)
        
        # 2. Select which animation frame to show
        current_frame = frames[step % 2]
        
        # 3. Print each line of the stick figure with increasing spaces on the left
        for line in current_frame:
            print(" " * step + line)
            
        # 4. Control the speed of the runner (lower number = faster)
        time.sleep(0.15)
        
except KeyboardInterrupt:
    print("\nRunner stopped!")

'''


'''rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for i in range(rows):
    for j in range(columns):
        if i%2==1 and j%2==1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * * 
'''


'''
rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for i in range(1,rows+1):
    for j in range(1,columns+1):
        if i%2==0 and j%2==0:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
#* * * * * 
#*   *   * 
#* * * * * 
#*   *   * 
#* * * * * '''
'''
rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for i in range(1,rows+1):
    for j in range(1,columns+1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#*         
#  *       
#   *     
#     *   
#        * 
   '''
''' 
rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

for i in range(1,rows+1):
    for j in range(1,columns+1):
        if i!=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#  * * * * 
#*   * * * 
#* *   * * 
#* * *   * 
#* * * *  '''