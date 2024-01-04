import telnetlib
import sys, time


def main():
    host = "192.168.4.108"
    tn = telnetlib.Telnet()
    tn.open(host)

    telnetlib.Telnet.set_debuglevel(tn, debuglevel=1)

    time.sleep(1)
    # 获取登录结果
    # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
    # tn.read_very_eager().decode('utf-8')
    tn.read_very_eager().decode('utf-8')
    tn.close()

    print("---------------------------------------------------------")
    # print(command_result)





main()






