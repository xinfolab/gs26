import wmi
import hashlib

hash_md5 = hashlib.md5()
hash_sha1 = hashlib.sha1()

c = wmi.WMI()


for process in c.Win32_Process():
    flag = process.ExecutablePath
    if flag != None:
        with open(flag, 'rb') as afile:
            buf = afile.read()
            hash_md5.update(buf)
        print(hash_md5.hexdigest())

