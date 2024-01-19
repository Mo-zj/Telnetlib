import telnetlib
import sys, time



class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# dt = datetime.fromtimestamp(timestamp)
# formatted_dt = dt.strftime("%Y-%m-%d_%H-%M-%S")
# string = "autoTestSaveLog_%s.txt" % formatted_dt
# # 输出结果到txt文件
# sys.stdout = Logger(string)

def log_save(host,content=b""):

    file_name = time.strftime("%Y%m%d_", time.localtime()) +  host + ".txt"

    with open("./"+file_name, 'a', encoding='utf-8') as f:
        # time.strftime("[%Y-%m-%d %H:%M:%S]  ", time.localtime())
        # f.write(content.decode(encoding="utf-8").strip())

        f.write(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + content.decode(encoding="utf-8"))
        #     f.write(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime()) + content1)




def remove_empty_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open("copy_"+filename, 'w') as f:
        for line in lines:
            if line.strip():
                f.write(line)



def main():

    results = []
    #
    # with open("count_log.txt", 'a', encoding='utf-8') as f:
    #     sys.stdout = f
    host = "100.100.100.222"
    # host = "192.168.4.108"

    tn = telnetlib.Telnet()
    tn.open(host)


    telnetlib.Telnet.set_debuglevel(tn, debuglevel=1)
    # time.sleep(3)
    # result1 = tn.read_very_eager().decode('utf-8')
    # print("-+" * 20, end=" ")
    # print(result1.decode(encoding="utf-8"))
    # print("-+" * 20, end=" ")


    time.sleep(1)
    # 获取登录结果
    # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出

    #
    # print(type(result))


    tn.write(b"root\n")
    time.sleep(1)
    tn.write(b"admin\n")


    # telnetlib.Telnet.set_debuglevel(tn, debuglevel=2)
    time.sleep(1)



    tn.write(b"en\n\nconfig\n\n")
    time.sleep(1)

    # result3 = tn.read_until(b"FD1304E(config)#")
    # print("-+"*20, end=" ")
    # print(tn.read_until(b"FD1304E(config)#").decode(encoding="utf-8"))
    log_save(host, content=tn.read_until(b"FD1304E(config)#"))
    # print("-+" * 20, end=" ")



    tn.write(b"interface epon 0/1\n")
    # result2 = tn.read_until(b"interface epon 0/1")

    # print("-+" * 20, end=" ")
    # print(tn.read_until(b"interface epon 0/1").decode(encoding="utf-8"))
    log_save(host, content=tn.read_until(b"interface epon 0/1"))
    # print("-+" * 20, end=" ")

    tn.write(b"shutdown 2\n")
    # result4 = tn.read_until(b"6666", 10)

    # time.sleep(5)

    # print("-+" * 20, end=" ")
    # print(tn.read_until(b"6666", 10).decode(encoding="utf-8"))
    log_save(host, content=tn.read_until(b"6666", 10))
    # print("-+" * 20, end=" ")

    tn.write(b"no shutdown 2\n")
    # time.sleep(10)
    # tn.write(b"\n\n")
    # print(tn.read_until(b"666", 30).decode(encoding="utf-8"))
    log_save(host, content=tn.read_until(b"666", 30))
    # tn.read_until(b"66666", 10)


    time.sleep(5)
    # result = tn.read_very_eager().decode('utf-8')

    # time.sleep(5)
    # print(result)
    tn.close()

    # with open("count_log.txt", 'a', encoding='utf-8') as f:
    #     sys.stdout = f
    #     print(result)



    # print(command_result)

def sys_stdout_exam():

    with open("count_log.txt", 'a', encoding='utf-8') as f:
        sys.stdout = f
        print("any consle print")


def debug():
    for i in range(10):
        print(type(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print(time.strftime("[%Y-%m-%d %H:%M:%S]  *", time.localtime()))
        time.sleep(1)





# main()
# debug()
remove_empty_lines("20240116_100.100.100.222.txt")

# sys_stdout_exam()





