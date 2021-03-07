cards = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

inputs = []
for _ in range(6):
    inputs.append(input())

for i in inputs:
    if i.isnumeric():
        inputs[inputs.index(i)] = int(i)
    else:
        inputs[inputs.index(i)] = cards[i]

print(sum(inputs) / 6)
