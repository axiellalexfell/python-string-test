#!/usr/bin/python3

f = open("test.txt", 'r')
contents = f.read()
f.close()

print(f"Contents: {contents}")

dict = {}
dict['contents'] = contents.encode()
print(f"New contents: " + repr{dict['contents']))

