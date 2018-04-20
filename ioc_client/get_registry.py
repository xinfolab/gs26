import wmi

GET_REGISTRY_TEST = 1

####
# AppEvents\EventLabels 는 데이터가 일치하는지 확인하기 위한 값
if GET_REGISTRY_TEST == 1:
  get_registry_test_data=[
    "Microsoft\MediaPlayer\{E6696105-E63E-4EF1-939E-15DDD83B669A}",
    "Software\Microsoft\ShipTr",
    "Software\Microsoft\CurrentHalInf",
    "Software\Microsoft\CurrentPnpSetup",
    "AppEvents\EventLabels"
  ]

# 0x80000001 : HKCU
# 0x80000002 : HKLM
BASIC_KEY = [
  0x80000001,
  0x80000002
  ]

####
# 순회하면서 모든 레지스트리 탐색
# 현재는 사용하지 않음
####
# SUBKEY = {
#   0x80000001 : [
#     "AppEvents",
#     "Console",
#     "Control Panel",
#     "Environment",
#     "EUDC",
#     "Keyboard Layout",
#     "Network",
#     "Printers",
#     "Software",
#     "System",
#     "Volatile Environment"
#   ],
#   0x80000002 : [
#     "AppEvents",
#     "Console",
#     "Control Panel",
#     "Environment",
#     "EUDC",
#     "Keyboard Layout",
#     "Network",
#     "Printers",
#     "Software",
#     "System",
#     "Volatile Environment"
#   ]
# }
#
# def recursive_search(basic_key, wmic, rootkey):
#   result, names = wmic.EnumKey(hDefKey=basic_key, sSubKeyName=rootkey)
#   for key in names:
#     subkey_buf = rootkey + "\\" + key
#     recursive_search(basic_key, wmic, subkey_buf)
#     print(subkey_buf)
#
# def get_registry_key():
#   wmic = wmi.WMI(namespace="default").StdRegProv
#
#   for basic_key_num in range(len(BASIC_KEY)):
#     subkey_list = SUBKEY[BASIC_KEY[basic_key_num]]
#     for subkey_num in range(len(subkey_list)):
#       result, names = wmic.EnumKey(hDefKey=BASIC_KEY[basic_key_num], sSubKeyName = subkey_list[subkey_num])
#       for key in names:
#         subkey_buf = subkey_list[subkey_num]+"\\"+key
#         recursive_search(BASIC_KEY[basic_key_num], wmic, subkey_buf)
#
#         #print(key)
####

####
## 값 가져오기
#result, value = wmic.GetStringValue(hDefKey=HKLM, sSubKeyName="SYSTEM\ControlSet001\Services\MRxDAV",sValueName="ImagePath")
#print(value)
####

def find_ioc_of_registry():
  wmic = wmi.WMI(namespace="default").StdRegProv

# names 개수가 0 또는 result 가 0 이상이면 ioc와 일치
  for basic_key_num in range(len(BASIC_KEY)):
    if GET_REGISTRY_TEST == 1:
      for data_num in range(len(get_registry_test_data)):
        result, names = wmic.EnumKey(hDefKey=BASIC_KEY[basic_key_num], sSubKeyName=get_registry_test_data[data_num])
        print("test : ",result)
        print(len(names))
    else:
      print("Not Yet")

find_ioc_of_registry()