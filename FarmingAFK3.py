import time as t
import keyboard as k
from directkeys import PressKey, ReleaseKey, W, A, S, D, J, E, F, G, Q, Mouse, UP, DOWN, LEFT, RIGHT

def keyPress(key, dur):
    PressKey(key)
    t.sleep(dur)
    ReleaseKey(key)
    t.sleep(0.1)

def main():
    d=20
    a=4.5
    b=0.9
    c=1.3
    diff=c+0.704997643478260869565217391304347826
    angle=75
    angle1=74
    angle2=76
    for i in range(1,5):
        print(".")
        t.sleep(1)
    while True:
        if True:
            for i in range(1,2):
                print(i)
                if i==1:
                    keyPress(D,0.1)
                    Mouse(4*d,0,)
                    keyPress(W,a+b)
                else:
                    t.sleep(0.5)
                    keyPress(Q,0.1)
                    t.sleep(2.5)
                #if i%10==0:
                #    keyPress(A,0.18)
                #    Mouse(-178*d,0,)
                if i!=1:
                    Mouse(-180*d,0,)
                    print("back")
                if i!=1:
                    keyPress(W,a)
                Mouse(-angle*d,0,)
                print("left")
                keyPress(W,c)
                keyPress(J,4)
                keyPress(J,4)
                Mouse(180*d,0,)
                print("back")
                keyPress(W,diff)
                #if i%15==0:
                #    Mouse(angle2*d,0,)
                #else:
                Mouse(angle*d,0,)
                print("right")
                keyPress(W,a)
                t.sleep(0.5)
                keyPress(E,0.1)
                t.sleep(3)
                #if i%30==0:
                #        keyPress(DOWN,0.1)
                #        keyPress(E,0.1)
                #        keyPress(UP,0.1)
                #        keyPress(UP,0.1)
                #        keyPress(RIGHT,0.1)
                #        keyPress(E,0.1)
                #        keyPress(LEFT,0.1)
                #        keyPress(E,0.1)
                #        keyPress(Q,0.1)
                #        t.sleep(1)
                #if i%10==0:
                keyPress(G,0.1)
                keyPress(F,0.1)
                keyPress(F,0.1)
                keyPress(E,0.1)
                keyPress(E,0.1)
                t.sleep(6)
        t.sleep(0.1)
if __name__ == "__main__":
    main()


