import sys, time
#sys.path.append(r'C:\Users\van\Desktop\test')
sys.path.append(r'.')
import __adbtest__
import __sta_simulator__

if __name__ == '__main__':
    __sta_simulator__.sta_simulator()
    time.sleep(25)
    __adbtest__.adbtest()
