
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")




c = int(position[0]) - 1
r = int(position[1]) - 1
map[r][c] = '👣'



print(f"{row1}\n{row2}\n{row3}")
