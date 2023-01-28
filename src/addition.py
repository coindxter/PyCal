from typing import typingInput, typingPrint, clearScreen
import time

history = []

def additionMode():
  while True:  
    print('Mode: Addition')
    print(' ')
    num1 = typingInput('Enter a number: ' )
    if num1 == 'back' or num1 == 'menu':
      clearScreen()
      return
    num2= typingInput('Enter a number: ' )
    if num2 == 'back' or num1 == 'menu':
      clearScreen()
      return
    real_answer = float(num1) + float(num2)
    history.append("%s + %s = %s" % (num1, num2, real_answer))
    with open("calHistory.py", "a") as f:
      for i, calc in enumerate(history):
        f.write(calc + "\n")
    print(' ')
    time.sleep(1)
    typingPrint('%s + %s = %s' % (num1, num2, real_answer))
    time.sleep(2)
    clearScreen()
   