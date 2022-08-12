#Q1/Write a method that will remove any given character from a String?

def Rmv(txt,Rmv_char):
    return txt.replace(Rmv_char,"")  if Rmv_char in txt else f"{Rmv_char} doesn't belong to {txt}!"
print(Rmv(txt=input('Write your text:'),Rmv_char=input("Charater to delete: ")))
#Q: if I want the code to delete A and This text is provided "AAA". Everything will be deleted, your question didn't cover this point actually and
#I'm sort of confused whether I should set the code to only del the first char or leave it as it is.


#Q2/Write a program to find all prime numbers up to a given range of numbers?

def prime_num(n):
    ini = 0
    for x in range(2, n):
        ini = ini + 1 if n % x == 0 else ""
    return ini   
n = int(input("Wrte down thenumber=  "))
#print("Prime num.") if prime_num(n) == 0 else print("Not prime num.")

#Q3/write a function that count how many the given character repeated in a given string?
from itertools import count
def Repeat(sen):
    return {char:  sen.count(char) for char in set(sen)}
print(Repeat(sen=input("Put your sentence please: ")))
