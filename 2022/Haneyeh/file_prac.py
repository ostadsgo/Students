f = open("hello.txt", 'r')
content = f.read()
f.close()

print(content.count("t"))
