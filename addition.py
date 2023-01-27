from typing import typingInput, typingPrint, clearScreen
import time

def additionMode():
  while True:  
    print("Mode: Addition")
    print(" ")
    num1 = typingInput('Enter a number: ' )
    if num1 == 'back':
      clearScreen()
      return
    num2= typingInput('Enter a number: ' )
    if num2 == 'back':
      return
    real_answer = float(num1) + float(num2)
    print(' ')
    time.sleep(1)
    print('%s + %s = %s' % (num1, num2, real_answer))
    time.sleep(2)
    clearScreen()