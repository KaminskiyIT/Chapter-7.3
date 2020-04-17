#! python3
# test7.2 - функция, которая принимает строку и делает то же,
# что и строковый метод strip(). Если ей не переданы никакие другие аргументы,
# кроме строки, то данная функция должна удалить из строки начальные и конечные пробельные символы.
# В противном случае из строки должны быть удалены символы, переданные функции в качестве второго аргумента.

import pyperclip, re

def myStript(someText, textDel = ''):
    if textDel == '':
        textRegex = re.compile(r'(\s*)(.*(\S))', re.DOTALL)
        myText = textRegex.search(someText)
        myTextTo = myText.group(2)
        print(myTextTo)
        return pyperclip.copy(myTextTo)
    else:
        subRegex = re.compile(r'['+textDel+']')
        resultDel = subRegex.sub('',someText)
        print(resultDel)
        return pyperclip.copy(resultDel)   

print('Enter your text:')
inputSomeText = input()

print('Enter the characters you want to remove from your text:')
inputCharacters = input()

myStript(inputSomeText, inputCharacters)
