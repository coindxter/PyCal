from menu import printMenu
from settings import settingsMode
from addition import additionMode
from subtraction import subtractionMode
from typing import clearScreen, typingInput, typingPrint
from history import historyMode

import os
import sys
import time

PIE = 3.14159265359

#-----------------------------------------------------------------

clearScreen()
typingPrint('Welcome User\n')
print(' ')
time.sleep(1.5)
Val = True
while Val:  
  printMenu()
  print(' ')
  act = typingInput('Choose an action above: ')
  print(' ')
  if act == '1':
    clearScreen()
    additionMode()
  if act == '2':
    clearScreen()
    subtractionMode()
  if act == 'stop' or act == 'quit':
    clearScreen()
    Val = False
  if act == 'settings' or act == 'Settings':
    clearScreen()
    settingsMode()

        


