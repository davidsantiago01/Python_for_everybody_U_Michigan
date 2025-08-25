
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

hours_count = dict()

for line in fhand:
    line = line.strip()
    if line.startswith("From "): 
        words = line.split()
        time = words[5]            
        hour = time.split(":")[0]  
        hours_count[hour] = hours_count.get(hour, 0) + 1

# Sort by hour key
for hour, count in sorted(hours_count.items()):
    print(hour, count)
