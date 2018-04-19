import wmi

####
# registry ioc
# TODO : 집가서 수정할 것
#
#Microsoft\MediaPlayer\{E6696105-E63E-4EF1-939E-15DDD83B669A}
#Software\Microsoft\ShipTr
#Software\Microsoft\CurrentHalInf
#Software\Microsoft\CurrentPnpSetup
#HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\MR
#HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\MRxNet\ImagePath
####

BASIC_KEY = [
  0x80000001,
  0x80000002
  ]

SUBKEY = {
  0x80000001 : [
    "AppEvents",
    "Console",
    "Control Panel",
    "Environment",
    "EUDC",
    "Keyboard Layout",
    "Network",
    "Printers",
    "Software",
    "System",
    "Volatile Environment"
  ],
  0x80000002 : [
    "AppEvents",
    "Console",
    "Control Panel",
    "Environment",
    "EUDC",
    "Keyboard Layout",
    "Network",
    "Printers",
    "Software",
    "System",
    "Volatile Environment"
  ]
}

####
def recursive_search(basic_key, wmic, rootkey):
  result, names = wmic.EnumKey(hDefKey=basic_key, sSubKeyName=rootkey)
  for key in names:
    subkey_buf = rootkey + "\\" + key
    recursive_search(basic_key, wmic, subkey_buf)
    print(subkey_buf)

def get_registry_key():
  wmic = wmi.WMI(namespace="default").StdRegProv

  for basic_key_num in range(len(BASIC_KEY)):
    subkey_list = SUBKEY[BASIC_KEY[basic_key_num]]
    for subkey_num in range(len(subkey_list)):
      result, names = wmic.EnumKey(hDefKey=BASIC_KEY[basic_key_num], sSubKeyName = subkey_list[subkey_num])
      for key in names:
        subkey_buf = subkey_list[subkey_num]+"\\"+key
        recursive_search(BASIC_KEY[basic_key_num], wmic, subkey_buf)

        #print(key)

####

####
## 값 가져오기
#result, value = c.GetStringValue(hDefKey=HKLM, sSubKeyName="SYSTEM\ControlSet001\Services\MRxDAV",sValueName="ImagePath")
#print(value)
####
get_registry_key()
