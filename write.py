#read the file store in list
#reverse list
# write list back to the file
with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)




