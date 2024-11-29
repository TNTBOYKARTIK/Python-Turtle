import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Tree Using Python Turtle")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# Function to draw a realistic leaf
def draw_leaf():
    t.color("green")
    t.begin_fill()
    for _ in range(2):  # Create an oval-like leaf
        t.circle(10, 90)
        t.circle(10 // 2, 90)
    t.end_fill()

# Recursive function to draw the tree
def draw_tree(branch_length, level, thickness):
    if level == 0:
        # Draw a realistic leaf at the tip
        t.right(45)  # Tilt the leaf for realism
        draw_leaf()
        t.left(45)  # Reset angle
        return

    t.width(thickness)  # Adjust branch thickness
    t.color("brown")  # Branch color
    t.forward(branch_length)
    
    # Left branch
    t.left(30)
    draw_tree(branch_length - 15, level - 1, thickness - 1)
    t.right(30)  # Reset angle
    
    # Right branch
    t.right(30)
    draw_tree(branch_length - 15, level - 1, thickness - 1)
    t.left(30)  # Reset angle
    
    t.backward(branch_length)  # Return to the starting point of the branch

# Function to scatter realistic leaves at the base
def scatter_leaves():
    t.penup()
    t.color("green")
    for _ in range(30):  # Scatter 30 leaves
        x = random.randint(-200, 200)
        y = random.randint(-300, -200)
        t.goto(x, y)
        t.setheading(random.randint(0, 360))  # Random rotation for leaves
        draw_leaf()

# Display source code below the tree
def display_source():
    source_code = '''
# Realistic Turtle Tree:
# - Brown trunk and branches
# - Realistic leaf shapes (ovals) at branch tips
# - Scattered realistic leaves at the base
# - Source code displayed below the design using turtle.write()
'''
    t.penup()
    t.goto(-300, -350)
    t.color("white")
    t.write(source_code, align="left", font=("Courier", 8, "normal"))

# Main trunk and branches
t.penup()
t.goto(0, -200)
t.setheading(90)
t.pendown()
t.width(10)  # Thick trunk
t.color("brown")

# Draw the tree, scattered leaves, and source code
draw_tree(100, 6, 10)  # Main branch length, depth, and thickness
scatter_leaves()
turtle.color("white")
turtle.write("Source Code in Comments!", align="center", font=("Arial", 15, "bold"))



# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
