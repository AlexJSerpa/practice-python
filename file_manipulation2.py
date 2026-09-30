from io import open

#file = open("file.txt", "r")

# print(file.read())

# file.seek(0)

# print(file.read())

#file.seek(len(file.read())/2)

file = open("file.txt", "r+")

file_lines = file.readlines()

file_lines[1] = "this line is include outside \n"

file.seek(0)

file.writelines(file_lines)


file.close()