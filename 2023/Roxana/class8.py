##import math
##
##def first_result():
##    res = sum(range(1, 10))
##    comp_file = open("result.txt", 'w')
##    comp_file.write(str(res))
##    comp_file.close()
##
### first_result()
##    
##def second_result():
##    x = sum(range(10, 15))
##    comp_file = open("result.txt", 'r')
##    res = comp_file.read()
##    result = x + int(res)
##    print(result)
##    comp_file.close()
##
##second_result()

##import random
##
##
##def next_quote():
##    index = quotes.index(quote)
##    q = quotes[index + 1]
##    print(q)
##
##quotes = ["q 1", "q 2", "q 3", "q 4", "q 5"]
##
##quote = random.choice(quotes)
##
##print(quote)
##next_quote()

from collections import Counter

f = open("pythonwiki.txt", 'r', encoding="utf-8")
content = f.read()
r = content.count('python')
r += content.count("Python")
words = content.split(' ')
res = Counter(words)
res = sorted(res.items(), key=lambda i: i[1], reverse=True)
print(res[:10])




