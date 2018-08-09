# adb检测脚本
import os, time


def consimulator():
    cmd = "adb devices"
    if "127.0.0.1" in str(os.popen(cmd).read()):
        print("你的adb已经连上了模拟器")
        time.sleep(1)
        print(os.popen(cmd).read())
    else:
        print("Q。Q")
        time.sleep(1)
        print("1.你的adb还是连不上模拟器,请确认你的模拟器打开了")
        time.sleep(1)
        print("2.请确认你的模拟器的开发者选项、usb调试已经被打开")


def adbtest():
    #print("( ゜- ゜)つロ\n", "欢迎使用van制作的简易模拟器控制脚本")
    #time.sleep(1)
    print("( ゜- ゜)つロ....正在检测你的adb是否连上模拟器")
    time.sleep(3)
    cmd = "adb devices"
    if "127.0.0.1" in str(os.popen(cmd).read()):
        print("你的adb已经连上了模拟器")
        time.sleep(1)
        print(os.popen(cmd).read())
    else:
        print("你的adb没有连上了任何模拟器")
        time.sleep(1)
        print("请确认你的模拟器已经打开")
        time.sleep(1)
        print("？=Q.Q=？")
        time.sleep(1)
        print("你用的模拟器是哪个？？？")
        time.sleep(1)
        print("本脚本自动连接的模拟器有::\n", "夜神模拟器,逍遥模拟器\n", "BlueStacks（蓝叠安卓模拟器） ,雷电安卓模拟器\n", "天天模拟器,网易MUMU模拟器\n",
              "安卓模拟器,genymotion")
        time.sleep(2)
        print("请输入你正在使用的模拟器（必须完全和上方显示的一致,建议复制黏贴）;")
        time.sleep(1)
        simulator = input("please input simulator you are using: ")
        if simulator == "夜神模拟器":
            print(r"你输入的是夜神模拟器")
            os.popen("adb connect 127.0.0.1:62001")
            time.sleep(1)
            consimulator()
        elif simulator == "逍遥模拟器":
            print(r"你连接的是逍遥模拟器")
            os.popen("adb connect 127.0.0.1:21503")
            time.sleep(1)
            consimulator()
        elif simulator == "BlueStacks（蓝叠安卓模拟器）":
            print(r"你连接的是BlueStacks（蓝叠安卓模拟器）")
            os.popen("adb connect 127.0.0.1:5555")
            time.sleep(1)
            consimulator()
        elif simulator == "雷电安卓模拟器":
            print(r"你连接的是雷电安卓模拟器")
            os.popen("adb connect 127.0.0.1:5555")
            time.sleep(1)
            consimulator()
        elif simulator == "天天模拟器":
            print(r"你连接的是天天模拟器")
            os.popen("adb connect 127.0.0.1:5037")
            time.sleep(1)
            consimulator()
        elif simulator == "网易MUMU模拟器":
            print(r"你连接的是网易MUMU模拟器")
            os.popen("adb connect 127.0.0.1:7555")
            time.sleep(1)
            consimulator()
        elif simulator == "安卓模拟器":
            print(r"你连接的是安卓模拟器")
            os.popen("adb connect 127.0.0.1:54001")
            time.sleep(1)
            consimulator()
        elif simulator == "genymotion":
            print(r"你连接的是genymotion")
            os.popen("adb connect 127.0.0.1:5555")
            time.sleep(1)
            consimulator()
        else:
            print(r"你没有输入本脚本支持的模拟器")
            time.sleep(1)
            print("步骤1：你需要先打开自己的模拟器\n")
            time.sleep(1)
            print("步骤2：请在下方输入自己的adb连接指令\n")
            cmd = input("请输入自己的adb指令;")
            try:
                os.popen("cmd")
                consimulator()
                return 0
            except:
                print("出错了、出错了")
            finally:
                time.sleep(1)
                print("你的指令已被执行")
                exit(0)


if __name__ == '__main__':
    adbtest()
