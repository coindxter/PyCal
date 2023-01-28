from typing import typingInput, typingPrint, clearScreen
from history import historyMode

def settingsMode():
    typingPrint('--------------\n')
    typingPrint('Settings\n')
    typingPrint('--------------')
    print(' ')
    print('1.Help\n2.History\n')
    act = typingInput('Choose an action above: ')
    if act == '1':
        clearScreen()
        helpMode()
    if act == '2':
        clearScreen()
        historyMode()
    if act == 'back' or act == 'Back':
        clearScreen()
        return
    
