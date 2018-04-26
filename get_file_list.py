#import hashpkg
import wmi
import re
import os

c = wmi.WMI()

def compare_ioc_path(file_name): # 해당 파일이 ioc_file_list에 존재하면 출력.
    ioc_list = open('..\\ioc\\ioc_file_list.txt')
    while True:
        line = ioc_list.readline()
        if not line:
            ioc_list.close()
            break
        if file_name.lower() == line.lower():
            print (file_name, line)

def file_search(disk): # 디스크 내의 모든 경로와 파일 탐색.
    try:
        for(path, dir, files) in os.walk(disk):
            for filename in files:
                file_path = path+"\\"+filename
                compare_ioc_path(filename)
    except:
        pass


for physical_disk in c.Win32_DiskDrive(): # 컴퓨터 내의 디스크 정보 추출.
    for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
        for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
            file_search(logical_disk.Caption+"\\")
