import sys
import json
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

name_list = [];
era_list = [];
summary_list = []
json_list = []
test = "blah"

with open('compiledSummaryInfo.csv', 'rb') as src:
    reader = csv.reader(src)
    # for row in reader:
    #     print row
    for row in reader:
        if row[0] != "phil_id":
            era_list.append(row[2])
            summary_list.append(row[3])

with open('sortedInfoboxDataEdited.json') as json_data:
    d = json.load(json_data)
    for x in range(0,380):
        name_list.append(d["philosophers"][x]["name"].strip())
        json_list.append(d["philosophers"][x])
    for x in range(0,380):
        try:
            influences = d["philosophers"][x]["influences"].split(",")
            # phil = " ".join(influences.split())
            for y in range(0, len(influences)):
                for z in range(0, len(name_list)):
                    if name_list[z] == influences[y].strip():
                        break;
                    if z == len(name_list) - 1 and name_list[z] != influences[y].strip():
                        name_list.append(influences[y].strip())
        except:
            test = "blah"
        try:
            # influenced = d["philosophers"][x]["influenced"].encode('utf-8').strip().split(",")
            influenced = d["philosophers"][x]["influenced"].split(",")
            # phil = " ".join(influenced.split())
            for y in range(0, len(influenced)):
                for z in range(0, len(name_list)):
                    if name_list[z] == influenced[y].strip():
                        break;
                    if z == len(name_list) - 1 and name_list[z] != influenced[y].strip():
                        name_list.append(influenced[y].strip())
        except:
            test = "blah"

#this is for making the links.csv
f = open('links.csv', 'w')
f.write("phil1id,source,phil2id,target" + "\n")
for x in range(0,380):
    try:
        influences = d["philosophers"][x]["influences"].split(",")
        # phil = " ".join(influences.split())
        for y in range(0, len(influences)):
            phil1id = name_list.index(influences[y].strip())
            source = influences[y]
            phil2id = d["philosophers"][x]["id"]
            target = d["philosophers"][x]["name"]
            # f.write(str(phil1id) + ",\"\"\"" + source + "\"\"\"," + str(phil2id) + ",\"\"\"" + target + "\"\"\"," + "\n")
            f.write(str(phil1id) + "," + source + "," + str(phil2id) + "," + target + "," + "\n")

    except:
        test = "blah"
    try:
        # influenced = d["philosophers"][x]["influenced"].encode('utf-8').strip().split(",")
        influenced = d["philosophers"][x]["influenced"].split(",")
        # phil = " ".join(influenced.split())
        for y in range(0, len(influenced)):
            phil1id = d["philosophers"][x]["id"]
            source = d["philosophers"][x]["name"]
            phil2id = name_list.index(influences[y])
            target = influences[y]
            # f.write(str(phil1id) + ",\"\"\"" + source + "\"\"\"," + str(phil2id) + ",\"\"\"" + target + "\"\"\"," + "\n")
            f.write(str(phil1id) + "," + source + "," + str(phil2id) + "," + target + "," + "\n")

    except:
        test = "sucks"
f.close()

#this is for making the nodes.csv
# f = open('nodes.csv', 'w')
# f.write("phil_id,name,era,summary" + "\n")
# for x in range(0, 380):
#     # f.write(str(x) + "," + name_list[x] + "," + summary_list[x] + "," + json_list[x] + "\n")
#     f.write(str(x) + "," + str(name_list[x]) + "," + str(era_list[x]) + "," + str(summary_list[x]) + "\n")
#
# for x in range(380,len(name_list)):
#     f.write(str(x) + "," + name_list[x] + "," + "Unknown Era" + "," + "No summary available" + "\n")
#
# f.close
