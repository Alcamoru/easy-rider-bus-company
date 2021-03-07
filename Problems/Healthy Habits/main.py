# the list "walks" is already defined
# your code here
all_values = []

for i in walks:
    all_values.append(i["distance"])

print(sum(all_values) // len(all_values))
