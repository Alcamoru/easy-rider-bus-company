squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}

inp = int(input())
if inp in squares.keys():
    print(squares.pop(inp))
else:
    print("There is no such key")

print(squares)
