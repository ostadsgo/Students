# Guessing number game
import random
# Create random number
rand_number = random.randint(1, 100)
print(rand_number)

def message_output(key):
    msg = {
        "lower": "I am samller.",
         "higher": "I am bigger.",
         "congrats": "Congragulation."
     }
    return msg[key]
    

def compare(guess, random_nume):
    if guess > rand_number:
        return "lower"
    elif guess < rand_number:
        return "higher"
    else:
        return "congrats"


def main():
    print("I am a number between 1 to 100\nTry to guess me\nYou have 10 chances.")
    # 10 chances to guess the number

    for guess_number in range(1, 3):
        guess = int(input("Guess a number: "))
        result = compare(guess, rand_number)
        print(message_output(result))
        if result == "congrats":
            print(f"It's took {guess_number} times.")
            break
        
    else:  # no break 
        print("You didn't make it")
        
        
main()

