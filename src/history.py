from typing import typingInput, typingPrint, clearScreen

def historyMode():
    while True:
        clearScreen()
        with open('calHistory.py', 'r') as f:
            print(f.read())
            f.close()
        print('1.Clear History\n2.Exit History')
        print(' ')
        act = input('Choose an action above: ')
        if act == '1':
            f = open('calHistory.py', 'w')
            clearScreen()
            return
        if act == '2':
            clearScreen()
            return