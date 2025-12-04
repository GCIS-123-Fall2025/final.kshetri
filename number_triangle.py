"""

# Main file provided for Q1 of mte3 (number_triangle.py)
# GCIS-123 Section 14 (2251)

Please complete the function below, that given an integer between 0 and 9, prints an
increasing sequence starting with only 0 and ending with 0 1 ... n.  See below
for examples.
If n is < 0 or > 9, the function should raise a ValueError with a message of
"n must be between 0 and 9 inclusive" printed from the function.
Your function must use recursion.
You have been provided with a main and test cases using the 
exception handling construct (note: this doesn't use pytest!).
Use main() as it is given.

Expected Output:
    number_triangle(3):
    0
    0 1 
    0 1 2 
    0 1 2 3 
    
    number_triangle(9):
    0
    0 1 
    0 1 2 
    0 1 2 3 
    0 1 2 3 4 
    0 1 2 3 4 5 
    0 1 2 3 4 5 6 
    0 1 2 3 4 5 6 7 
    0 1 2 3 4 5 6 7 8 
    0 1 2 3 4 5 6 7 8 9 
    
    number_triangle(0):
    0
    
    number_triangle(-1):
    n must be between 0 and 9 inclusive
    
    number_triangle(10):
    n must be between 0 and 9 inclusive

Please complete your function below.
"""

def number_triangle(n):
    
################ YOUR CODE HERE




##############################

# Please do not alter any code in the main () function below !

def main():
    print("number_triangle(3):")
    number_triangle(3)

    print("\nnumber_triangle(9):")
    number_triangle(9)

    print("\nnumber_triangle(0):")
    number_triangle(0)

    try:
        print("\nnumber_triangle(-1):")
        number_triangle(-1)
    except ValueError as ve:    print(ve)

    try:
        print("\nnumber_triangle(10):")
        number_triangle(10)
    except ValueError as ve:    print(ve)

if __name__ == "__main__":    main()