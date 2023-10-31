with open('mbox.txt', 'r') as file:
    count = 0 
    host = ""
    for line in file:
        if line.startswith("From "):
            line = line.rstrip()
            parts = line.split()
            if len(parts) >= 2:
                email = parts[1]
            print(email)
            count = count + 1
    print(f'Total {count} lines were printed ')
    