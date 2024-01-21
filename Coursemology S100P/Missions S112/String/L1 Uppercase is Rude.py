# Question 1: Is He Rude?
def msgRating(message):
    if message.isupper():
        return "Rude"
    else:
        return "Polite"
    
# Question 2: Make Him Polite
def makeMsgSillyPolite(message):
    return message.lower()
    
# print(msgRating("THIS IS TERRIBLE"))
# print(msgRating("This is amazing"))
# print(msgRating("I DON'T THINK YOU WILL LIKe THIS"))