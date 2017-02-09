width = int(raw_input("What is the width?: "))
height = int(raw_input("What is the height?: "))

print '*'*width
for number in range(height-2):
    print '*' + " "* (width-2) + '*'
print '*'*width
