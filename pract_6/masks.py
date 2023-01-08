"""
Xinghua Peng
DS 2000: Intro to Programming with Data

Date: Thu Oct 13 11:51:37 2022
    
File: masks.py
    
Comment: The final output is amazingly cool like loops of pyramids!
I was totally surprised by the emergent pattern!!! 


"""
## Import package needed for this assignment
import matplotlib.pyplot as plt

## Step 1
def initialize_array(m, n, init_value = 0):
    """ This function creates an initial m x n array of values,
    with all values initialized to 0 by default.
    m - number of rows / days (sub-lists)
    n - number of columns / students (elements in each sub-list)
    """
    
    L = []
    for i in range(m):
        L.append([])
        for j in range(n):
            L[i].append(init_value)
    L[0][n//2] = 1
    return L

## Step 2
# Brainstorming Process
# () - wear a mask
# Day 0 -                   99 (100) 101 ...
# Day 1 -                   (99) 100 (101) ...
# Day 2 -                (98) 99 100 101 (102) ...
# Day 3 -             (97) 98 (99) 100 (101) 102 (103) ...
# Day 4 -           (96) 97 98 99 100 101 102 103 (104) ...
# Day 5 -       (95) 96 (97) 98 99 100 101 102 (103) 104 (105) ...

def apply_rule(L):
    """ This function apply the rules and determines which students are 
    wearing a mask on each subsequent day (365).
    """
    rows = len(L)
    cols = len(L[0])
    for i in range(1,rows):
        for j in range(cols):
            neighbor = 0
          
            if j > 0:
                neighbor += L[i-1][j-1]
            if j < cols - 1:
                neighbor += L[i-1][j+1]
            if neighbor == 1:
                 L[i][j] = 1
                

## Step 3
def array_to_image(L):
    """ This function plots the results by converting the two-dimensional
    array into an image.
    """
    # Dimensions and resolution of the image
    plt.figure(figsize = (4, 5), dpi = 200)
    
    # Convert list-of-lists into an image
    plt.imshow(L, cmap = "binary")
    
    # Create x & y label
    plt.xlabel("Number of Students")
    plt.ylabel("Number of Days")
    
    # Save image as a .png
    plt.savefig("masks.png")
    

## Step 4
# Main function & Use previous defined functions
def main():
    
    list_simulation = initialize_array(365, 201, init_value = 0)
    apply_rule(list_simulation)
    array_to_image(list_simulation)
    
    
main()

    