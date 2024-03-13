import re

# 讀取所有檔案內的內容 此為非預設路徑
with open(r'E:\BS\BlueStacks_nxt\bluestacks.conf', 'r') as file:
    data = file.read()

# 找目標模擬器的正規表達式
BS_name = "BlueStacks App Player"
prefix_pattern = rf'(.+).display_name="{BS_name}"'

# 找目標模擬器
m = re.search(prefix_pattern, data)
prefix = m.group(1)
print(prefix)

# 找 port 的正規表達式
port_pattern = rf'{prefix}.status.adb_port="(\d+)"'

# 找 port
m = re.search(port_pattern, data)
port = int(m.group(1))
print(port)
