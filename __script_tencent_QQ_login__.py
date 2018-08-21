# coding=UTF-8
import os
import time


def device():
    if "5555" in str(os.popen("adb devices").readlines()):
        print("android debug bridge 连接上你的Android设备")
    else:
        print("没检测到你的Android设备，正在尝试重新连接")
        os.popen("adb kill-server")
        os.popen("adb start-server")
        if "5555" in str(os.popen("adb devices").readlines()):
            print("android debug bridge 连接上你的Android设备")
        else:
            print("你的设备不能连上adb\n1.请确认你的android设备已连接\n2.请确认你开启了开发者选项")
            exit(-1)


def click(x, y):
    cmd = "adb shell input tap {} {}".format(x, y)
    os.popen(cmd)


def text(c):
    cmd = "adb shell input text {}".format(c)
    os.popen(cmd)


def delete():
    cmd = "adb shell input keyevent 67"
    os.popen(cmd)


def screeencap():
    time_now = str(time.localtime().tm_hour) + "hour" + str(time.localtime().tm_min) + "min" + str(
        time.localtime().tm_sec) + "second"
    cmd = "adb shell screencap /date/local/curr.png"
    print(cmd)
    os.popen(cmd)
    time.sleep(1)
    cmd = "adb pull /data/local/curr.png c:\\Users\\xiewenhua\\Desktop\\script\\screencap"
    print(cmd)
    os.popen(cmd)
    # 重命名
    time.sleep(1)
    os.rename("c:\\Users\\xiewenhua\\Desktop\\script\\screencap\\curr.png",
              r"c:\\Users\\xiewenhua\\Desktop\\script\\screencap\\%s" % time_now + ".png")
    time.sleep(1)
    # 删除手机内的缓存
    cmd = "adb shell rm -rf /data/local/curr.png"
    os.popen(cmd)
    time.sleep(1)


if __name__ == "__main__":
    device()
    # 点击QQ图标
    click(120, 120)
    time.sleep(4)
    # 点击用户名输入框
    click(209, 205)
    time.sleep(1)
    i = 1
    while 1:
        i += 1
        delete()
        if i > 12:
            break
    time.sleep(4)
    text(r'2572881705')
    time.sleep(4)
    click(144, 212)
    time.sleep(1)
    i = 1
    while 1:
        i += 1
        delete()
        if i > 10:
            break
    time.sleep(4)
    text(r'xwh2835326')
    time.sleep(1)
    click(283, 277)
