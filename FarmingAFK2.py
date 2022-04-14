import pyautogui as p
import time as t
import keyboard as k
from directkeys import PressKey, ReleaseKey, W, A, S, D, J, E, Q, Mouse

def keyPress(key, dur):
    PressKey(key)
    t.sleep(dur)
    ReleaseKey(key)
    t.sleep(0.1)

def main():
    d=20
    a=4.5
    b=0.02
    c=1.3
    diff=c+0.704997643478260869565217391304347826
    angle=75
    angle1=74
    angle2=76
    while True:
        if k.is_pressed("enter"):
            for i in range(1,101):
                print(i)
                t.sleep(0.5)
                keyPress(Q,0.1)
                t.sleep(2.5)
                if i%10==0:
                    keyPress(A,0.18)
                    Mouse(-178*d,0,)
                else:
                    Mouse(-180*d,0,)
                print("back")
                keyPress(W,a)
                #t.sleep(0.5)
                Mouse(-angle*d,0,)
                print("left")
                #t.sleep(0.5)
                keyPress(W,c)
                keyPress(J,4)
                keyPress(J,4)
                Mouse(180*d,0,)
                print("back")
                keyPress(W,diff)
                #t.sleep(0.5)
                if i%15==0:
                    Mouse(angle2*d,0,)
                else:
                    Mouse(angle*d,0,)
                print("right")
                #t.sleep(0.5)
                keyPress(W,a)
                t.sleep(0.5)
                keyPress(E,0.1)
                t.sleep(3)
        t.sleep(0.1)
if __name__ == "__main__":
    main()


