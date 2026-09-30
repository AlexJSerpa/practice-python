import pickle

# list_names = ["Naruto", "Sasuke", "Kakashi"]

# binary_file = open("list_names", "wb")

# pickle.dump(list_names, binary_file)

# binary_file.close()

# del (binary_file)

file = open("list_names", "rb")

list_names = pickle.load(file)

print(list_names)

