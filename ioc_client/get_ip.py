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
def compare_ip(ioc_ip_list):
    if GET_IP_TEST is 1:
        for i in range(len(get_ip_test_data)):
            if get_ip_test_data[i] in ioc_ip_list:
                print(get_ip_test_data[i])
            else:
                print(AD)

def get_ip():
    #print_format = "%-30s %-13s"
    #print(print_format % ("Remote address", "Status"))

    ioc_ip_tuple = ()
    for c in psutil.net_connections(kind='inet'):
        remote_address = ""
        if c.raddr:
            remote_address = "%s:%s" % (c.raddr)
        # remote address empty
        if c.raddr == ():
            continue

        ioc_ip_tuple += c.raddr[:1]

     #   print(print_format % (remote_address or AD, c.status))

    ioc_ip_list = list(set(list(ioc_ip_tuple)))

    # print(ioc_ip_list)

    compare_ip(ioc_ip_list)




get_ip()