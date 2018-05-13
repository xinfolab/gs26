import json
import time
import conn.server_data
import requests
from collections import OrderedDict

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

    return ready_data

def send_report(report):
    save_time_data = time.localtime()
    time_format = "%04d%02d%02d%02d%02d%02d" % (save_time_data.tm_year, save_time_data.tm_mon, save_time_data.tm_mday, save_time_data.tm_hour, save_time_data.tm_min, save_time_data.tm_sec)
    url = conn.server_data.server + conn.server_data.REPORT_PARAMETER + time_format
    headers = conn.server_data.json_type_headers

    res = requests.post(url, headers=headers, data=json.dumps(report))

    print(res)

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

def test_json_data_load(json_data):
    data = json_data
    # data = json.loads(json_data)

    print(data["user"])
    print(data["report"]["ip"])
    print(data["report"]["reg"])
    print(data["report"]["hash"])
    print(data["report"]["file"])


if JSON_SET_TEST is 1:
    # report = OrderedDict()
    report = test_json_data_set()
    # test_json_data_load(report)
    send_report(report)