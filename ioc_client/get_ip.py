import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

import psutil

#1 이면 get_ip 함수 점검, 0이면 지나감
GET_IP_TEST = 1

AD = "-"
AF_INET6 = getattr(socket, 'AF_INET6', object())
proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}

#######
# 127.0.0.1 은 정상적으로 탐지하는지 확인하기 위한 값
if GET_IP_TEST is 1:
    get_ip_test_data = [
        "103.85.226.65",
        "185.203.116.126",
        "45.77.49.118",
        "50.63.202.38",
        "104.202.173.82",
        "127.0.0.1"
    ]
#######

#######
# TODO : 현재는 ioc 리스트를 각자 점검하기 때문에 나중에 완성하자
#######
class ip:
    match_ip_list = []
    def compare_ip(self, user_ip_list):
        ioc_c2_file = []
        # compare_ip 함수 점검용 코드
        if GET_IP_TEST is 1:
            for i in range(len(get_ip_test_data)):
                if get_ip_test_data[i] in user_ip_list:
                    print(get_ip_test_data[i])
                else:
                    print(AD)
            return "test function\n"

        # compare_ip 정상 작동
        with open("..\\ioc\\ioc_c2_list.txt") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                ioc_c2_file.append(line)

        for i in range(len(ioc_c2_file)):
            if ioc_c2_file[i] in user_ip_list:
                self.match_ip_list.append(ioc_c2_file[i])

    def get_ip(self):
        user_ip_tuple = ()
        for c in psutil.net_connections(kind='inet'):
            remote_address = ""
            if c.raddr:
                remote_address = "%s:%s" % (c.raddr)
            # remote address empty
            if c.raddr == ():
                continue

            user_ip_tuple += c.raddr[:1]
        user_ip_list = list(set(list(user_ip_tuple)))

        # ioc와 사용자 ip를 비교
        self.compare_ip(user_ip_list)

        return self.match_ip_list

if GET_IP_TEST is 1:
    class_test = ip()
    test_list = class_test.get_ip()
    print(test_list)