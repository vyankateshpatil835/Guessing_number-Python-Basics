import random 
radnum = random.randint(1,100)

print('''\n\n<<<<<<<<  Let's Play The Game  >>>>>>>>

You Have to Guess a Number i'm thinking
let's see how much you guess 
Guess in 1 To 100
**************************************** 
''')
user = input('Enter Your Name:\n')
print('**************************************** ')

guesses =0
userguess = None 
while (userguess != radnum):
    try:
        userguess = int(input(f"{user} Let's guess a number:\n"))
        guesses += 1
        if radnum == userguess:
            print('You guessed it Right\n')
        else:
            if userguess<radnum:
                print("You are Close, Guess little Higher\n")
            elif userguess > radnum:
                print("You are Close, Guess little Lower\n")
    except Exception as e:
        print(f'''
        What is This Behaviour Bro...
        Kya He Ye --> {e}\n''')

with open("Score.txt",'r') as f:
    f.read()
with open("Score.txt", 'a') as f:
    f.write(f'{user} = {guesses}'+ '\n')

print(f'''
****************************************
You guessed it in {guesses} guesses
****************************************''')
print('''
*******************************************************************************
Compliment From Me :  
''')
if guesses < 3:
    print('--> Bhagwan He Kya Sale...\n')
elif guesses in [3,4]:
    print('--> Galti Se Guess Hua Na Sach Bol...\n')
elif guesses in [5,6]:
    print('--> Pro Guesser, Itne Ache Guess Ager JEE Me Ker leta To Soch Aj Kaha Hota \n')
elif guesses in [8,9]:
    print('--> Itne Guesses Me To Bachaa Bhi Guess ker lega, Koi Badi Baat Nahi Hai\n')
elif guesses == 10: 
    print('--> NOOB...!, Ek Number Guess Nahi Hota\n')
elif guesses in [11,12]:
    print('--> Chulhu Bhar Pani Me Dub Marja\n')
elif guesses > 12:
    print('--> Tu Firse Mat Kheliyo...!!!, Ek Kam Ker Jina Hi Chod de\n')
print("*******************************************************************************")
