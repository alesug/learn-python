question = ""
name = ""

import random
random_number = random.randint(1,9)
print(random_number)

if name == "" and question != "":
  print('Question: ' + question)
elif name != "" and question == "":
  print(name + ', you didn'+"'"+'t ask a question...please try again!')
elif name == "" and question == "":
  print('No question.')
else:
  print(name + ' asks: ' + question)

if question == "":
  answer = 'No answer required.'
else:
  if random_number == 1:
    answer = 'Yes - definitely'
  elif random_number == 2:
    answer = 'It is decidedly so'
  elif random_number == 3:
    answer = 'Without a doubt'
  elif random_number == 4:
    answer = 'Reply hazy, try again'
  elif random_number == 5:
    answer = 'Ask again later'
  elif random_number == 6:
    answer = 'Better not tell you now'
  elif random_number == 7:
    answer = 'My sources say no'
  elif random_number == 8:
    answer = 'Outlook not so good'
  elif random_number == 9:
    answer = 'Very doubtful'
  else:
    answer = 'Error'

print('Magic 8-Balls answer: ' + answer)
