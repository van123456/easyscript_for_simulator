#!/usr/bin/env python
# -*-coding:utf-8-*-
# 这是adb连接的升级版
import time
import os


# def函数作用：检测adb -是否连上了模拟器
def test_adb():
    print("检测adb连接状态")
    n = 0
    while n < 3:
        time.sleep(1)
        n = n + 1
        print('*', end='.')

    cmd = "adb devices"
    if '127.0.0.1' in str(os.popen(cmd).readlines()):
        print("p(*_____*)==adb连上了模拟器\n")
        n = 1
        for v in list(os.popen(cmd).readlines()):
            if "127.0.0.1" in v:
                print("你连上了第{0}台设备\n端口:{1}".format(n, v))
                n = n + 1
    else:
        print("你的adb没连上模拟器,玩个奶子哦")
        time.sleep(1)
        print("*********帮你自动连接模拟器")
        auto_emulator()


# def函数作用：一些说明信息
def inform():
    print("( ゜- ゜)つロ --你使用的python3下运行的脚本")
    time.sleep(1)
    print("作者：van")
    time.sleep(1)
    print("你要确认你的adb已配置成环境变量，不然((((;°Д°))))，这个脚本没什么卵用")
    time.sleep(1)


# def函数作用：去fetch adb的版本
def adb_environment():
    cmd = "adb version"
    if "version" in str((os.popen(cmd)).readlines()):
        for v in list((os.popen(cmd)).readlines()):
            if "version" in v:
                print("c(*____*)=你的android版本就是：%s" % v)
    else:
        print("不清楚你的adb版本,((((;°Д°))))")


# 自动连接模拟器
def auto_emulator():
    # 设置开关
    u = 1
    while u:
        cmd = "adb devices"
        if '127.0.0.1' not in str(os.popen(cmd).readlines()):
            try:
                list = [62001, 21503, 5555, 5555, 5037, 7555, 54001, 5555]
                list1 = ['夜神模拟器', '逍遥模拟器', '蓝叠安卓模拟器/雷电安卓模拟器/genymotion', ' 蓝叠安卓模拟器/雷电安卓模拟器/genymotion', ' 天天模拟器',
                         ' 网易MUMU模拟器', '安卓模拟器', '蓝叠安卓模拟器/雷电安卓模拟器/genymotion']
                for v in list:
                    os.popen('adb connect 127.0.0.1:%s' % v)
                    print('尝试帮你连接%s' % list1[list.index(v)])
            except Exception as err:
                print(err)
            finally:
                time.sleep(1)
                print('((((;°Д°))))')
                time.sleep(1)
                print("连不上模拟器，请确认模拟器是否打开，且开启usb调试选项")
                u = 0
        else:
            print("连上模拟器")
            u = 0


# 控制执行信息
def main():
    inform()
    adb_environment()
    test_adb()
    auto_emulator()


# 函数作用：脚本入口
if __name__ == '__main__':
    main()
