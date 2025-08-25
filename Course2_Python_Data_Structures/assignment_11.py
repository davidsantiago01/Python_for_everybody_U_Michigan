
import re

hand = open("data.txt")
y = []   

for line in hand:
    line = line.rstrip()
    matches = re.findall(r"[0-9]+", line) 
    if matches:
        y.extend([float(m) for m in matches])

print("Sum of numbers:", sum(y))

#Sum of numbers: 387687.0
