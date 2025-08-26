import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(56):
    t.forward(100)  # Move forward by 100 units
    t.right(20)     # Turn right by 90 degrees

# Keep the window open
turtle.done()