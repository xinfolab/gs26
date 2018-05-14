# -*- encoding:utf-8 -*-
import wmi
import os
import re
import sys
import hashpkg



class file_path():
    result_hash = {}
    enc = sys.stdin.encoding
    data = open('.\\core\\ioc_list\\ioc_file_list.txt', 'rb').readlines()

    def compare_ioc_hash(self, hash_value, full_filename):
        if re.search(hash_value, open('.\\core\\ioc_list\\ioc_hash_list.txt').read(), re.IGNORECASE) !=None:
            #print(self.result_hash)
            self.result_hash[full_filename] = hash_value

    def compare_ioc_file(self, file_name, full_filename):
        file_name = file_name.encode(self.enc)
        try:
            if file_name+b"\r\n" in self.data:
                self.result_hash[full_filename] = ""
                #print(self.result_hash)
                return True
        except:
            pass

    def file_search(self, disk):
        try:
            filenames = os.listdir(disk)
            for filename in filenames:
                full_filename = os.path.join(disk, filename)
                if os.path.isdir(full_filename):
                    self.file_search(full_filename)
                else:
                    file_flag = self.compare_ioc_file(filename, full_filename)
                    if file_flag == True:
                        hs = hashpkg.hash_calc()
                        md5_hash = hs.get_md5_hash(full_filename)
                        self.compare_ioc_hash(md5_hash, full_filename)
                        sha1_hash = hs.get_sha1_hash(full_filename)
                        self.compare_ioc_hash(sha1_hash, full_filename)
                        sha256_hash = hs.get_sha256_hash(full_filename)
                        self.compare_ioc_hash(sha256_hash, full_filename)
        except:
            pass

    def get_file(self):
        c = wmi.WMI()
        for physical_disk in c.Win32_DiskDrive():
            for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
                for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                    self.file_search(logical_disk.Caption+"\\")
        print("Done")
        return(self.result_hash)
