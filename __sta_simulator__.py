# 一个控制模拟器的脚本【夜神模拟器】
# __script_noxsimulator__.py
import os, sys
import time


def sta_simulator():
    print("( ゜- ゜)つロ\n", "欢迎使用van制作的简易模拟器脚本")
    time.sleep(1)
    print("List of known simulator:\n", "--NOXsimulator--:\n", r"E:\xwh\simulator\nox_simulator\Nox\bin\Nox.exe")
    time.sleep(1)
    print("--录入值为空时--")
    print("--默认打开夜神模拟器--")
    name_simulator = input("please input the path of your simulator:")
    if name_simulator == "":
        name_simulator = r"E:\xwh\simulator\nox_simulator\Nox\bin\Nox.exe"
        os.startfile(name_simulator)
        print("正在帮你打开夜神模拟器.....")

    else:
        print("你输入了自己模拟器的路径:\n", "starting for you .......")
        try:
            os.startfile(name_simulator)
        except Exception as err:
            print("报错了，报错了........:\n", "你的路径写错了!!!!")
            sys.exit(-1)
        finally:
            print("=.=.==.==.=..=.=..==.==.=.=.==.=.=.")


if __name__ == '__main__':
    sta_simulator()
