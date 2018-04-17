import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

import psutil

AD = "-"
AF_INET6 = getattr(socket, 'AF_INET6', object())
proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}
#####
#   @brief 현재 PC 에 연결되어 있는 TCP, UDP 정보를 가져옴
#   @param 추가 예정
#   @return bool 형
#
#   현재 실행 결과
#   Proto Local address                  Remote address                 Status
#   tcp   127.0.0.1:16106                -                              LISTEN
#   tcp6  :::7680                        -                              LISTEN
#
#####
def get_ip():
    print_format = "%-5s %-30s %-30s %-13s"
    print(print_format % ("Proto", "Local address", "Remote address", "Status"))

    for c in psutil.net_connections(kind='inet'):
        local_address = "%s:%s" % (c.laddr)
        remote_address = ""
        if c.raddr:
            raddr = "%s:%s" % (c.raddr)
        print(print_format %
              (proto_map[(c.family, c.type)],local_address,remote_address or AD,c.status)
              )

def get_system_info():
    get_ip()

#####
#   @brief PC 네트워크 현황과 IOC를 비교함
#   @param 추가 예정
#   @return bool 형
#
#####
def ip_compare():
    print("ip_compare\n")


def ioc_compare():
    ip_compare()

def ready():
    get_system_info()

def start():
    ioc_compare()

if __name__ == '__main__':

    ready()

    start()