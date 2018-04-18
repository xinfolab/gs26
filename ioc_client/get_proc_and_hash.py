import wmi
import hashlib

hash_md5 = hashlib.md5()
hash_sha1 = hashlib.sha1()

c = wmi.WMI()

for process in c.Win32_Process():
    flag = process.ExecutablePath #실행중인 프로세스 목록 가져옴.
    if flag != None: # 실행중인 프로세스의 목록 중 경로를 가져올 수 없는 부분은 제외.
        with open(flag, 'rb') as afile: # 각 프로세스 별 해쉬 값 계산
            buf = afile.read()
            hash_md5.update(buf)
           # hash_sha1.update(buf)
        if hash_md5.hexdigest() in open('ioc_hash_list.txt').read(): # 계산된 해쉬값이 ioc_hash_list에 존재하는 경우 출력.
            print(process.Name)
