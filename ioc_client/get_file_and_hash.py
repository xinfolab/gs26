# -*- encoding:utf-8 -*-
import wmi
import os
import re
import sys
import hashpkg

enc = sys.stdin.encoding
c = wmi.WMI()
data = open('ioc_file_list.txt', 'rb').readlines()

def compare_ioc_hash(hash_value):
    if re.search(hash_value, open('ioc_hash_list.txt').read(), re.IGNORECASE):
        print(hash_value)

def compare_ioc_file(file_name, full_filename):
    file_name = file_name.encode(enc)
    try:
        if file_name+b"\r\n" in data:
            return True
    except:
        pass

def file_search(disk):
    try:
        filenames = os.listdir(disk)
        for filename in filenames:
            full_filename = os.path.join(disk, filename)
            if os.path.isdir(full_filename):
                file_search(full_filename)
            else:
                file_flag = compare_ioc_file(filename, full_filename)
                if file_flag == True:
                    hs = hashpkg.hash_calc()
                    md5_hash = hs.get_md5_hash(full_filename)
                    compare_ioc_hash(md5_hash)
                    sha1_hash = hs.get_sha1_hash(full_filename)
                    compare_ioc_hash(sha1_hash)
                    sha256_hash = hs.get_sha256_hash(full_filename)
                    compare_ioc_hash(sha256_hash)
    except:
        pass

for physical_disk in c.Win32_DiskDrive():
    for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
        for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
            file_search(logical_disk.Caption+"\\")
