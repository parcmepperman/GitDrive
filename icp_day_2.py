## ICP Number 1

list_one = ("WordOne", "SecondWord", "Third")
list_two = [(len(list_one[0]), list_one[0]), (len(list_one[1]), list_one[1]), (len(list_one[2]), list_one[2])]
list_three = max(sorted(list_two))
# max(list_three)

print(list_one)
print(list_two)
print(list_three)
print("""

""")

## ICP Number 2

infile = open("sample.txt", 'r')
line1 = infile.readlines()
file = open("outputfile.txt", "w")
for line in line1:
    length = len(line) - 1
    file.write(str(length))
    file.write(" ")
    file.write(line)

# ICP Number 3

infile = open("sample2.txt", 'r')
line2 = infile.readlines()

for lineS in line2:
    split = " "
    print(lineS, "  Number of words in this line is:", len(lineS.split()))
    # printed to terminal indented to separate txt line and print line

# ICP Number 4

height_brd = int(input("Enter the Height of the game board:"))
width_brd = int(input("Enter the WIDTH:"))
i = "___"
j = "|"
game_size = j + i + j
game_floor = j
h = 1
w = 0
print(" ___ " * width_brd) #top of the game board

while h <= height_brd:
    print(width_brd * game_size)
    h = h + 1


















