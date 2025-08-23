

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
    
fh = open(fname)

counts = dict()


for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):  
        continue
    words = line.split()
    email = words[1]                
    counts[email] = counts.get(email, 0) + 1   


max_sender = None
max_count = None

for sender, count in counts.items():
    if max_count is None or count > max_count:
        max_sender = sender
        max_count = count

print(max_sender, max_count)
