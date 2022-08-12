#Q1/Write a method that will remove any given character from a String?

def Rmv(txt,Rmv_char):
    return txt.replace(Rmv_char,"")  if Rmv_char in txt else f"{Rmv_char} doesn't belong to {txt}!"
print(Rmv(txt=input('Write your text:'),Rmv_char=input("Charater to delete: ")))
#bug, if the sentence has two repeated charater, it will delete them both



#Q2/Write a program to find all prime numbers up to a given range of numbers?



#Q3/write a function that count how many the given character repeated in a given string?
from itertools import count
def Repeat(sen):
    return {char:  sen.count(char) for char in set(sen)}
print(Repeat(sen=input("Put your sentence please: ")))