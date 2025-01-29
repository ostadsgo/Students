import logging


f = open("hello.txt", "w")
f.write("Salam donya\n")
f.close()


with open("hello.txt", "w") as f:
    f.write("Salam donya\n")


logging.basicConfig(filename="example.log")

try:
    with open("some.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    logging.error("some.txt not found!")


print("end of program")
