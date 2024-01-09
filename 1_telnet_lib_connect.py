import telnetlib
import sys, time






def main():
    host = "192.168.5.222"
    tn = telnetlib.Telnet()
    tn.open(host)

    # telnetlib.Telnet.set_debuglevel(tn, debuglevel=1)

    time.sleep(1)
    # 获取登录结果
    # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
    result = tn.read_very_eager().decode('utf-8')
    #
    # print(type(result))


    # assert "User name" in result



    print("yes")
    tn.write(b"root\n")
    time.sleep(1)
    tn.write(b"admin\n")


    telnetlib.Telnet.set_debuglevel(tn, debuglevel=1)
    time.sleep(1)
    # result2 = tn.read_very_eager().decode('utf-8')
    # print("1111111")
    # print(result2)
    for i in range(101):

        tn.write(bin(i))
        tn.read_until(b">", 0.1)
    time.sleep(5)

    time.sleep(1)
    tn.close()

    # print(command_result)

def debug():
    for i in range(10):
        print(i)
        i = bytes(str(i),encoding="utf-8")
        str1 = b"this is "+i+b" line"
        print("--------------------------")
        print(str1)
        print("**************************")
        print(str1.decode(encoding="utf-8"))





# main()
debug()





