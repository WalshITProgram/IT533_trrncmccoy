# Create an empty list:
csv_file = open("SalesJan2009.csv")

for file in csv_file:
    tmp_file = file.split(",")
    tmp_file[0] = tmp_file[0][1:-1]
    tmp_file[1] = tmp_file[1][1:-1]
    tmp_file[2] = tmp_file[2][1:-1]
    tmp_file[3] = tmp_file[3][1:-1]
    tmp_file[4] = tmp_file[4][1:-1]
    tmp_file[5] = tmp_file[5][1:-1]
    tmp_file[6] = tmp_file[6][1:-1]
    tmp_file[7] = tmp_file[7][1:-2]
    tmp_file1 = tmp_file[0]
    tmp_file2 = tmp_file[1]
    tmp_file3 = tmp_file[2]
    tmp_file4 = tmp_file[3]
    tmp_file5 = tmp_file[4]
    tmp_file6 = tmp_file[5]
    tmp_file7 = tmp_file[6]
    tmp_file8 = tmp_file[7]
    tmp_file9 = tmp_file1 + " " + tmp_file2 + " " + tmp_file3 + " " + tmp_file4 + " " + tmp_file5 + " " + tmp_file6 + " " + tmp_file7 +  " " + tmp_file8
    print(tmp_file9)
import json

json_file = open("config.json")
config_data = json.load(json_file)

print(config_data)

