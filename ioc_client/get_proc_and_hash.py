import hashpkg #해시함수 패키지화
import wmi
import re

c = wmi.WMI()

def compare_ioc(hash_value): # 계산된 해시 값을 ioc_hash_list와 비교.
    if re.search(hash_value, open('..\\ioc\\ioc_hash_list.txt').read(), re.IGNORECASE): #ioc_hash_list의 대소문자를 무시.
        print(hash_value) # 해시값이 존재한다면 해당 해시값 출력.


for process in c.Win32_Process():
    flag = process.ExecutablePath # 현재 실행중인 프로세스 가져오기.
    if flag != None: # 경로를 가져올 수 없는 경우는 제외.
        hs = hashpkg.hash_calc() # 패키지 내의 해쉬 클래스 객체 선언.
        hash_md5 = hs.get_md5_hash(flag) # 해당 프로세스 경로를 찾아 MD5 해시값 계산.
        compare_ioc(hash_md5)
        hash_sha1 = hs.get_sha1_hash(flag) # 해당 프로세스 경로를 찾아 SHA1 해시값 계산.
        compare_ioc(hash_sha1)
        hash_sha256 = hs.get_sha256_hash(flag) #해당 프로세스 결로를 찾아 SHA256 해시값 계산.
        compare_ioc(hash_sha256)
