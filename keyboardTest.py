from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

sleep(5)
keyboard.press(Key.left)
sleep(2)
keyboard.release(Key.left)