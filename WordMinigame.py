# In this game we prompt the user to give us a 7 letter work, check if it's right then ask for a 4 letter word
UserWord = input("Give me a seven letter word: ")

if len(UserWord) == 7:
    UserWord = input("Well Done you can spell! Now input a four letter word: ")
    if len(UserWord) == 4:
        print("Well Played!")
    else:
        print("X That's wrong")
else:
    print("X that's wrong")
