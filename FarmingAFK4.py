import time as t
import keyboard as k
from directkeys import PressKey, ReleaseKey, W, A, S, D, J, E, F, G, Q, Mouse, UP, DOWN, LEFT, RIGHT, SPACE

def keyPress(key, dur):
    PressKey(key)
    t.sleep(dur)
    ReleaseKey(key)
    t.sleep(0.1)

def sprint(dur):
    PressKey(W)
    PressKey(SPACE)
    t.sleep(dur)
    ReleaseKey(SPACE)
    ReleaseKey(W)

def main():
    d=20
    a=2.8
    b=0.9
    c=0.8
    diff=+0.8
    angle=75
    cycle=1
    while True:
        if k.is_pressed("enter"):
            while True:
                print(cycle)
                for i in range(1,2):
                    keyPress(G,0.1)
                    keyPress(F,0.1)
                    keyPress(F,0.1)
                    keyPress(E,0.1)
                    keyPress(E,0.1)
                    t.sleep(5)
                    Mouse(7*d,0,)
                    sprint(a+b)
                    Mouse(-angle*d,0,)
                    sprint(c)
                    keyPress(J,5)
                    Mouse(180*d,0,)
                    sprint(c/2+diff)
                    Mouse(-85*d,0,)
                    sprint(1.5)
                    t.sleep(0.5)
                cycle+=1
        t.sleep(0.1)
if __name__ == "__main__":
    main()


