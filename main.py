import json
data=''
with open("data_file.json", "r",encoding='utf-8') as read_file:
    data = json.load(read_file)
print(data[0][4])