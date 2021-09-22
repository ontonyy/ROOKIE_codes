import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], stdout=subprocess.PIPE, universal_newlines=True).stdout
profile_names = (re.findall(r"(.*)\r", command_output))
wifi_list = list()
print(command_output)
print(profile_names)
if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()

        profile_info = subprocess.run(["netsh", "wlan", "show", "profiles", name], stdout=subprocess.PIPE, universal_newlines=True).stdout
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile['ssid'] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profiles", name, "key=clear"], stdout=subprocess.PIPE, universal_newlines=True).stdout
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)
        
for x in range(len(wifi_list)):
    print(wifi_list[x])
