import random
print("Hangman Game!")
words_list = ["apple", "orange", "banana", "laptop", "monitor"]
word = words_list[random.randint(0, len(words_list) - 1)]
tries = 5
user_input = []

for i in word:
  user_input.append("_")
answer = []
for i in word:
  answer.append(i)

while tries != 0:
  if user_input == answer:
    print("\nYou won! The word is: " + ''.join(user_input))
    break
  print("\n" + ' '.join(user_input))
  print(f"You have {tries} tries left!")
  user_guess = input("Which letter would you like to try? ")
  if user_guess in answer:
    for i in range(len(answer)):
      if user_guess == answer[i]:
        user_input[i] = user_guess
  else:
    tries -= 1

if tries == 0:
  print("\nYou lose! The word is: " + ''.join(answer))