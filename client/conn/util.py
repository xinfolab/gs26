import json
import time
import conn.server_data
import requests
import os
from collections import OrderedDict
from seleniumrequests import Chrome

JSON_SET_TEST = 0

if JSON_SET_TEST is 1:
    ip_list = ["1234","1234","1234","1234"]
    reg_list = ["test1","test2","test3","test4"]
    hash_dic = {"file1":"hash1", "file2":"hash2","file3":"hash3","file4":"hash4"}
    file_dic = {"malw1":"path1","malw2":"path2","malw3":"path3","malw4":"path4"}

def make_format(session_id, report):
    ready_data = OrderedDict()
    ready_data["user"] = session_id
    ready_data["report"] = report

    return json.dumps(ready_data)

def send_report(report):
    save_time_data = time.localtime()
    time_format = "%04d%02d%02d%02d%02d%02d" % (save_time_data.tm_year, save_time_data.tm_mon, save_time_data.tm_mday, save_time_data.tm_hour, save_time_data.tm_min, save_time_data.tm_sec)
    url = conn.server_data.server + conn.server_data.REPORT_SAVE_PARAMETER  + time_format
    headers = conn.server_data.json_type_headers

    res = requests.post(url, headers=headers, data=json.dumps(report))

    print(res)

def web_open():
    url = conn.server_data.server + conn.server_data.REPORT_TOKEN_PARAMETER
    headers = conn.server_data.json_type_headers
    data={}
    data['token']=conn.server_data.USER_TOKEN
    path_token = os.getcwd()
    path = path_token + '\\conn\\chromedriver.exe'
    browser = Chrome(path)
    res = browser.request('POST', url, headers=headers, data=json.dumps(data))
    print(url)
    print(res.cookies)

    browser.get(url)

def web_test():

    url = conn.server_data.server + conn.server_data.REPORT_TOKEN_PARAMETER
    headers = conn.server_data.json_type_headers
    data = {}
    data['token']= '02cda594401840ec955c81533bc761d4'

    path = 'C:\gs26\client\conn\chromedriver.exe'
    browser = Chrome(path)

    r = browser.request('POST', url, headers=headers, data=json.dumps(data))
    print(r.cookies)
    browser.get(url)

def test_json_data_set():
    ip_list = ["1234","1234","1234","1234"]
    reg_list = ["test1","test2","test3","test4"]
    hash_dic = {"file1":"hash1", "file2":"hash2","file3":"hash3","file4":"hash4"}
    file_dic = {"malw1":"path1","malw2":"path2","malw3":"path3","malw4":"path4"}


    report = OrderedDict()
    report["ip"] = ip_list
    report["hash"] = hash_dic

    report["file"] = file_dic
    report["reg"] = reg_list

    total = OrderedDict()

    total["user"] = "test@test.com"
    total["report"] = report

    # print(total)

    return total


def json_read_test():
    data = ""
    with open("C:\\gs26\\ioc_server\\ioc_server\\report\\20180516134556","r") as f:
        data = f.readline()

    test = json.loads(data)

    print(test)

    print(data)

if JSON_SET_TEST is 1:
    # report = OrderedDict()
    # report = test_json_data_set()
    # test_json_data_load(report)
    # send_report(report)
    # web_test()
    json_read_test()