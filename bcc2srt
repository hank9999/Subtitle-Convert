import json
import datetime

try:
    print("Convert Started\n")
    count = 0
    with open('3.bcc', 'r', encoding='utf-8') as f1, open('3.bcc.srt', 'w', encoding='utf-8') as f2:  # change input and output files
        bcc_raw = f1.read()
        bcc_json = json.loads(bcc_raw)
        for item in bcc_json['body'][0:]:
            count += 1
            raw_from = float("%.3f" % (item['from'] + 0.001))
            raw_to = float("%.3f" % (item['to'] + 0.001))
            bcc_from = (str(datetime.timedelta(seconds=raw_from)))
            bcc_to = (str(datetime.timedelta(seconds=raw_to)))
            f2.write(str(count) + "\n0" + bcc_from[0:bcc_from.find(".")] + "," + bcc_from[bcc_from.find(".") + 1 : bcc_from.find(".") + 4] + " --> " + "0" + bcc_to[0:bcc_to.find(".")] + "," + bcc_to[bcc_to.find(".") + 1 : bcc_to.find(".") + 4] + "\n" + str(item['content']) + "\n\n")
        print("Convert Completed\n")
except:
    print("Convert Failed")
