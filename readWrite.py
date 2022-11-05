file=open('text.txt')
#read all content of the file
# read n no of char's by passing parameter
# print(file.read(5))
#
# print(file.readline())  # read single Line at a time
# print(file.readline())


#Print line by line using readLine method

# line = file.readline()
#
# while line != "":
#     print(line)
#     line=file.readline()

for line in file.readlines():
    print(line)

file.close()