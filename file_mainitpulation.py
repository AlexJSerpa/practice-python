from io import open

# file = open("file.txt", "w")

# phase = "great day for studying \n python on Wednesday"

# file.write(phase)

#file = open("file.txt", "r")

#text = file.read()

# text_lines = file.readlines()

# print(text_lines)


#append
file = open("file.txt", "a")
file.write("\n great day for studying in general")

file.close()

