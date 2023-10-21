print('Hey, how are you doing today?')

total_score = 0

confirmation = input('Do you want to play an interesting quiz game? ').lower()

print(confirmation)

if confirmation == 'yes':
    print("Great! let's start")
else:
    quit()

question = input('What is the largest planet in our solar system? ')

if question.capitalize() == 'Jupiter':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is Jupiter')

question = input('Who wrote the famous play "Romeo and Juliet"? ')

if question.capitalize() == 'William Shakespeare':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is William Shakespeare')


question = input('What is the chemical symbol for the element gold? ')

if question.capitalize() == 'Au':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is Au')

question = input('In which year did the Titanic sink? ')

if question == '1912':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is 1912')

question = input('What is the capital of Australia? ')

if question.capitalize() == 'Canberra':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is  Canberra')

question = input('What is the largest mammal in the world? ')

if question.lower() == 'blue whale':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is blue whale')

question = input(' Which planet is often referred to as the "Red Planet? ')

if question.capitalize() == 'Mars':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is Mars')

question = input('What is the largest organ in the human body? ')

if question.capitalize == 'Skin':
    print('Correct :)')
    total_score += 1
else:
    print('Wrong! Correct answer is Skin')

print(f'You have scored {total_score} out of 8')

total_percent = (total_score/8) * 100
print(f' Your total percentage is {total_percent}% ')

# check = type(total_percent)

# print(check)

# if total_percent >= 80:
#     print('Congratulations! Well done')
