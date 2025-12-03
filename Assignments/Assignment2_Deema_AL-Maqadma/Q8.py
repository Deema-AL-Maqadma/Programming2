#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/8 :   Write a Python program that asks the user to enter a text and return a dictionary whose keys are the words of the text entered and the values are the lengths of the words that make up the text. 

def text_to_dict(text):
    dic_words = {}
    words = text.split()
    for word in words:
        dic_words[word]= len(word)
    return dic_words
        
text = input("Enter a text: ")
print(f"---> The original text : \n---> {text}")
print("---> The Dictionary : ")
print(text_to_dict(text)) 
