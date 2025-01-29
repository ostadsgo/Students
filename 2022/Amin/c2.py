##x = 10
##
##if x > 5:
##    print('hello')
##else:
##    print('goodbye')
##
##
##
##print('end of program.')
# falsey values: 0 0.0 '' [] {} () None


##if x > 10 and y < 10:  # 2 3 4
##    pass
##
##elif x > 20:
##    pass
##
##else:
##    pass
##
##if x > 0
##
##
##if y < 0
##
##
##if z == 0

##x = -5
##
##result = ""
##
##if x > 0:
##    result = "Positive"
##elif x < 0:
##    result = "Negative"
##else:
##    result = "Zero"
##
##print(x, 'is', result)
##
##


# uppercase number len > 8

##score = 0
##
##password = "HH22HHHH3332299034ccc0"
##
##for ch in password:
##    if ch.isupper():
##        score += 1
##    if ch.isdigit():
##        score += 1
##        
##if len(password) > 8:
##    score += 1
##
##if score in range(0, 5):
##    print('weak')
##elif score in range(5, 10):
##    print('meh')
##elif score in range(10, 15):
##    print("normal")
##elif score in range(15, 20):
##    print("strong")
##else:
##    print("very strong")

##n = 10
##result = ""
##
##for n in range(1, 20):
##    if n % 2 == 0:
##        result = "even"
##    else:
##        result = "odd"
##    print(n, result)
##        

# fizz buzz

result = "*****"

for n in range(1, 100):
    if n % 15 == 0:
        result = "FizzBuzz"
    elif n % 3 == 0:
        result = "Fizz"
    elif n % 5 == 0:
         result = "Buzz"
    else:
        continue
    print(n, result)


