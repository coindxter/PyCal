from typing import typingInput, typingPrint, clearScreen
import time

def SubtractionMode():
  while True:
    num1=input('Enter a number:   ' )
    if num1 == 'back' :
      return
    num2=input('Enter a number:   ' )
    real_answer = float(num1) - float(num2)
    print(' ')
    time.sleep(1)
    print('%s - %s = %s ' % (num1, num2, real_answer))