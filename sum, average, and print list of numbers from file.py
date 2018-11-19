# Enter the name of your file followed by the extension
filename = input("Please enter your file name: ")

# Create initial containers for the sum, numLength, and average
sum = 0
numLength = 0
average = 0

# Open the file to access its contents
openTheFile = open("numbers.txt", "r")

# Create for loop to iterate through list of integers
# ignoring whitespace and setting necessary calculations
# for the sum, numLength, and average data containers
for line in openTheFile:
    for numbers in line.split(","):
        sum = sum + float(numbers.strip())
        numLength = numLength + 1
        average = sum/numLength

# Close file after accessing its contents and performing calculations
openTheFile.close()

# Proceed to print the list, sum, and average of integers read from your file
print(open("numbers.txt").read())

print("\nThe sum of your numbers is:", sum)

print("\nThe average of your numbers is:", average)
