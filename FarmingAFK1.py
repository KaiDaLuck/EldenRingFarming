import pyautogui as p
import time as t
from directkeys import PressKey, ReleaseKey, W, A, S, D, J, E, Q, Mouse

def keyPress(key, dur):
    PressKey(key)
    t.sleep(dur)
    ReleaseKey(key)
    t.sleep(0.5)

d=20

def main():
    p.FAILSAFE = True
    for i in range(0,3):
        print(".")
        t.sleep(1)
    while True:
        for i in range(1,90):
            print(i)
            Mouse(180*d,0)
            keyPress(W,4)
            keyPress(J,4)
            keyPress(J,4)
            Mouse(180*d,0)
            keyPress(W,4.64)
            keyPress(E,0.1)
            t.sleep(3)
            keyPress(Q,0.1)
            t.sleep(2)
            if i%30==0:
                keyPress(D,0.15)
            elif i%15==0:
                keyPress(A,0.15)

if __name__ == "__main__":
    main()

