# f = open('File.txt', 'r')
# print(f.read())

file_name = 'File.txt'
with open(file_name, 'r') as file:
    contents = file.readline ()
print(len(contents))