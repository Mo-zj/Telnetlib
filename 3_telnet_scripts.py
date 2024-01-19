
import telnetlib
import sys, time


def log_save(host,content=b""):

    file_name = time.strftime("%Y%m%d_", time.localtime()) +  host + "_log.txt"

    with open("./"+file_name, 'a', encoding='utf-8') as f:

        f.write(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + content.decode(encoding="utf-8"))



def remove_empty_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open("copy_"+filename, 'w') as f:
        for line in lines:
            if line.strip():
                f.write(line)


def telnet_olt(host, username, password):

    tn = telnetlib.Telnet()
    tn.open(host)
    telnetlib.Telnet.set_debuglevel(tn, debuglevel=1)
    time.sleep(1)
    tn.write("{}\n".format(username).encode(encoding="utf-8"))
    time.sleep(1)
    tn.write("{}\n".format(password).encode(encoding="utf-8"))
    time.sleep(1)

    return tn


def main():

    host = "100.100.100.222"
    username = "root"
    password = "admin"


    tn = telnet_olt(host, username, password)

    tn.write(b"en\nconfig\n")
    log_save(host, content=tn.read_until(b"FD1304E(config)#", 3))

    tn.write(b"interface epon 0/1\n")
    log_save(host, content=tn.read_until(b"FD1304E(config-epon-0/1)#", 3))

    while True:
        tn.write(b"ont re-register 2 all\n")
        time.sleep(35)
        tn.write(b"\n\n\n")
        tn.write(b"show ont register-statistics all\n\n")
        log_save(host, content=tn.read_until(b"wait-register", 5))

    # log_save(host, content=tn.read_very_eager())
    # tn.read_very_eager()

main()

# remove_empty_lines("20240117_100.100.100.222_log.txt")
# remove_empty_lines("20240118_100.100.100.222_log.txt")






