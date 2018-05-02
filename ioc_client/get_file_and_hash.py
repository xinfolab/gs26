# -*- encoding:utf-8 -*-
import wmi
import os
import re
import sys

enc = sys.stdin.encoding
c = wmi.WMI()
data = open('ioc_file_list.txt', 'rb').readlines()

def compare_ioc_file(file_name, full_filename):
    file_name = file_name.encode(enc)
    try:
        if file_name+b"\r\n" in data:
            print(full_filename)
    except:
        pass

def file_search(disk):
    try:
        filenames = os.listdir(disk)
        for filename in filenames:
            full_filename = os.path.join(disk, filename)
            compare_ioc_file(filename, full_filename)
            if os.path.isdir(full_filename):
                file_search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
    except:
        pass

for physical_disk in c.Win32_DiskDrive():
    for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
        for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
            file_search(logical_disk.Caption+"\\")
