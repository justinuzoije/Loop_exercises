#Triangle 2

height = int(raw_input("What is the height?: "))

#The oddNumbers is a way to have an infinite number of odd numbers
#It will do the sequence 1, 3, 5, 7, 9, etc
#The range goes through these numbers, the farthest it should go is
#double the height of the pyramid, because it is like looking at a big square
#range(start, stop, count by) It counts by 2 so it is only odd numbers
oddNumbers = range(1, height*2, 2)

for number in range(height):
    #This will print stars
    #It is a way to print an odd number of stars, so it prints
    #1 star, 3 stars, 5 stars, then 7 stars
    #
    #center is a
    print ('*'*oddNumbers[number]).center(oddNumbers[height-1])
