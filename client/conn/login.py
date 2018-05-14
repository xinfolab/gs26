import json
from collections import OrderedDict
import requests

import conn

# 현재 서버로 아이디 비밀번호 전송할 경우 이렇게 됨
# 117.16.11.8:8888/api/login
# json포맷으로 {'email': 'test@test.com', 'password': 'test'}

LOGIN_TEST = 0

class login:
    id = None
    password = None

    def set_sending_data(self):
        data = OrderedDict()

        data["email"] = self.id
        data["password"] = self.password

        return json.dumps(data)

    def send_info(self):
        data = self.set_sending_data()

        url = conn.server_data.server + conn.server_data.LOGIN_PARAMETER
        headers = conn.server_data.json_type_headers

        res = requests.post(url,data=data, headers=headers)
        data = json.loads(res.text)

        if True != data['result']:
            return False

        # print(res.text)

        return True

    def login_start(self, id, passwd):
        if id == "" or passwd == "":
            # print("err")
            return False

        self.id = id
        self.password = passwd

        if True != self.send_info():
            print("send_info function err!!")
            return False

        return True


if 1 == LOGIN_TEST:
    test_class = login()
    if True != test_class.login('test@test.com' ,'test'):
        print("login class test failed")