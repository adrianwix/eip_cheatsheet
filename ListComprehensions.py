squares = [x**2 for x in range(10)]

print(squares)

# Is the same
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
