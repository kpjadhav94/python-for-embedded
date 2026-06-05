# Lines that start with a "#" are comments.

# Example 1: Printing a string
# In Python, we can use either single quotes ' ' or double quotes " " to define a string.
# For multi-line strings, we can use triple quotes ''' ''' or """ """.
print("Hello World!")       # Double quotes for a string
print ('My name is Ketan')  # Single quotes for a string
print ("""This is a         # Multi-line string example.
       multi-line
       string.""")

# Example 2: String Indexing - Like C Arrays
mcu = "STM32F4"

# Indexing - exactly like C arrays, we can access individual 
# characters in a string using their index.
print(mcu[0])       # S
print(mcu[1])       # T
print(mcu[2])       # M

# Negative indexing - unique to Python, we can also access characters from 
# the end of the string using negative indices.
print(mcu[-1])      # 4 <- Last character
print(mcu[-2])      # F <- Second last character

# In the above example, Memory Layout is looks like:
# S    T      M      3      2      F      4
# [0]  [1]    [2]    [3]    [4]    [5]    [6]   
# [-7] [-6]   [-5]   [-4]   [-3]   [-2]   [-1]   
