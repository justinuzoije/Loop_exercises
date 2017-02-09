


height = int(raw_input("What is the height?: "))

#for number in range(width):
#    a = ""
#    for number in range(height):
#        a +='*'
#        print a


#spacing = (1,3,5,7)
#spacing = []
spacing = range(1, height*2, 2)

for number in range(height):
    print ('*'*spacing[number]).center(spacing[height-1])
