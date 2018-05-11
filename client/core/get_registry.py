import wmi

GET_REGISTRY_TEST = 0

####
# AppEvents\EventLabels 는 데이터가 일치하는지 확인하기 위한 값
if GET_REGISTRY_TEST == 0:
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
class registry:
    match_list = []
    ioc_registry_list = []

    def find_ioc_of_registry(self):
        wmic = wmi.WMI(namespace="default").StdRegProv

        if GET_REGISTRY_TEST == 1:
            for basic_key_num in range(len(BASIC_KEY)):
                for data_num in range(len(get_registry_test_data)):
                    result, names = wmic.EnumKey(hDefKey=BASIC_KEY[basic_key_num], sSubKeyName=get_registry_test_data[data_num])
                    print("target : ",get_registry_test_data[data_num])
                    print("result : ",result)
                    print(len(names))
                    print("==================")
            return "registry ioc find test"

    # 테스트 코드가 아닐 때 실행
        with open(".\\core\\ioc_list\\ioc_registry_list.txt") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                self.ioc_registry_list.append(line)

        for basic_key_num in range(len(BASIC_KEY)):
            for data_num in range(len(self.ioc_registry_list)):
                result, match_number = wmic.EnumKey(hDefKey=BASIC_KEY[basic_key_num], sSubKeyName=self.ioc_registry_list[data_num])

            # names 개수가 0 또는 result 가 0 이상이면 ioc와 일치
            if len(match_number) > 0:
                root_key = ""
                if 0x80000001 == BASIC_KEY[basic_key_num]:
                    root_key = "HKEY_CURRENT_USER"
                else :
                    root_key = "HKEY_LOCAL_MACHINE"
                self.match_list.append(root_key + "\\" + self.ioc_registry_list[data_num])

        return self.match_list

if 1 == GET_REGISTRY_TEST:
  test_class = registry()
  test_class.find_ioc_of_registry()