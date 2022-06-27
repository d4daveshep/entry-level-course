# open text file for reading (file must exist)
stream = open("tzop.txt", "rt", encoding="utf-8")

# print(stream.read())

from os import strerror

try:
    count = 0
    stream = open("text.txt", "rt")
    ch = stream.read(1)
    while ch != "":
        print(ch, end="")
        count += 1
        ch = stream.read(1)
    stream.close()
    print(f"\n\nRead {count} characters from file")
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


