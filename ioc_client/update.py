import os
from requests import get

import server_data

IOC_DIRECTORY = "..\\ioc"

# test
UPDATE_CLASS_TEST = 1

class update:
    file_list = []

    # @ breif 서버에서 파일 다운로드 함수
    # @ param paramter get으로 전송할 경우 사용할 파라미터
    #         directory 다운로드 할 디렉토리 경로
    #         file_name 다운받을 파일 이름
    def download_ioc(self, parameter, directory, file_name):
        url = server_data.server + parameter +  file_name
        with open(directory + file_name, "wb") as file:
            res = get(url)
            # print(res.status_code)
            if res.status_code == 200:
                file.write(res.content)
            else:
                print(file_name, "file download error!")

    def server_ioc_list(self, parameter):
        url = server_data.server + parameter
        res = get(url)

        # 서버에서 list를 문자열로 반환하여 리스트로 적용되게끔 파싱함
        split_list = res.text[1:-1].split(',')
        for i in range(len(split_list)):
            self.file_list.append(split_list[i].strip()[1:-1])

        # print(self.file_list)

    def start(self):
        # ioc 파일 리스트를 서버에서 받아옴
        self.server_ioc_list(server_data.GET_FILE_LIST_PARAMETER)

        if 0 == len(self.file_list):
            print("Not Found ioc file, check sever")
            return False

        # 디렉토리 없으면 생성
        if not os.path.isdir(IOC_DIRECTORY):
            os.mkdir(IOC_DIRECTORY)

        # ioc 다운로드
        for i in range(len(self.file_list)):
            self.download_ioc(server_data.UPDATE_PARAMETER, IOC_DIRECTORY + "\\", self.file_list[i])

        return True

if UPDATE_CLASS_TEST == 1:
    test_class = update()

    # test_class.download_ioc("update", ".\\", "ioc_c2_list.txt")
    # test_class.server_ioc_list("update/all_file_list")
    if True != test_class.start():
        print("UPDATE_CLASS_TEST failed !!")