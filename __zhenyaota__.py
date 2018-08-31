# 每个模拟器不同，需要自己改
# coding='utf-8'
import os, time
import time


def exist_devices():
    if "127.0.0.1" in str(os.popen("adb devices").readline()):
        return 0
    else:
        print("没有检测到设备，重启adb")
        os.popen("adb kill-server")
        os.popen("adb start-server")
        if "127.0.0,1" in str(os.popen("adb devices").readlines()):
            return 0
        else:
            print("无法找到模拟器--")
            exit(-1)


def click(x, y):
    cmd = "adb shell input tap {} {}".format(x, y)
    os.popen(cmd)


def paochangjin():
    click(563, 754)
    time.sleep(8)
    screencap()
    time.sleep(12)
    click(961, 684)
    time.sleep(3)
    click(914, 749)
    time.sleep(8)
    screencap()
    time.sleep(12)
    click(961, 864)
    time.sleep(3)
    click(1267, 747)
    time.sleep(8)
    screencap()
    time.sleep(12)
    click(961, 684)
    time.sleep(3)


def input():
    raw = input("please input the line of your select")
    print(raw)
    if raw == "2":
        click(1217, 191)
    elif raw == "3":
        click(604, 344)
    else:
        click(1218, 345)
    time.sleep(1)


def text(x):
    cmd = "adb shell input tap{}".format(x)
    os.popen(cmd)


def screencap():
    time_now = str(time.localtime().tm_hour) + "hour" + str(time.localtime().tm_min + "min") + "min" + str(
        time.localtime().tm_sec) + "second"
    cmd = "adb shell screencap /data/local/curr.png"
    print(cmd)
    os.popen(cmd)
    time.sleep(1)
    cmd = "adb pull /data/local/curr.png C:\\Users\\van\\Desktop\\script\\screencap"
    print(cmd)
    os.popen(cmd)
    time.sleep(1)
    os.rename("C:\\Users\\van\\Desktop\\script\\screencap\\curr.png",
              r"C:\\Users\\van\\Desktop\\script\\screencap\\%s" % time_now + ".png")
    time.sleep(1)
    cmd = "adb shell rm -rf /data/local/curr.png"
    os.popen(cmd)
    time.sleep(1)


'''
def time_now():
    time_now() = str(time.localtime().tm_hour) + "hour" + str(time.localtime().tm_min) + "min" + str(
        time.localtime().tm_sec) + "second"
'''
if __name__ == '__main__':
    exist_devices()
    click(1261, 54)
    time.sleep(1)
    click(1481, 323)
    time.sleep(1)
    input()
    for n in range(17):
        paochangjin()
