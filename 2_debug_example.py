


# todo：字符串类型与bytes类型之间互转
# https://blog.csdn.net/weixin_43852058/article/details/129088186?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20%E6%95%B4%E6%95%B0%E8%BD%ACbytes&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-129088186.142^v99^pc_search_result_base9&spm=1018.2226.3001.4187
def str_to_bytes():
    for i in range(10):
        print(i)
        # 把字符串类型转为bytes类型
        i = bytes(str(i),encoding="utf-8")
        str1 = b"this is "+i+b" line"
        print("--------------------------")
        print(str1)
        print("**************************")
        # 把bytes类型进行解码
        print(str1.decode(encoding="utf-8"))

    # 或
    # str 转 bytes
    s_to_b = "张三abcd".encode(encoding="utf-8")
    print("str 转 bytes:",s_to_b)

    b_to_s = s_to_b.decode(encoding="utf-8")
    print("bytes 转 str:",b_to_s)


# todo：整数类型与bytes类型之间互转
def int_to_bytes():

    # int 转 bytes
    for i in range(10):
        """
        # int 转 bytes
        int.to_bytes(字节长度, 大端/小端存储, 关键字参数有符号还是无符号)
        - 大端：big
        - 小端：little
        
        # 例如：将数字128存储为int16类型的字节，在计算机里小端存储
        # 如果实际数字超出了存储字节的长度，将会报错
        int(128).to_bytes(2, 'little', signed=True)
        ————————————————
        版权声明：本文为CSDN博主「秀聚」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
        原文链接：https://blog.csdn.net/weixin_43852058/article/details/129088186
        """
        print("--------------------------")
        i = int(i).to_bytes(2, 'little', signed=True)
        print(i)

        # bytes 转 int
        print("**************************")
        print(int.from_bytes(i, 'little', signed=True))


# str_to_bytes()
int_to_bytes()





