import sys

all_data = []  # will store data type [message_id, {}]
input_file = open(sys.argv[1], "r", encoding="utf8")

for line in sorted(input_file.readlines()):
    data = line.split("\t")
    message_id = data[0]
    packet_id = data[1]
    message = data[2]
    found = False
    for it in all_data:
        if it[0] == message_id:
            found = True
            it[1][packet_id] = message
    if found is False:
        all_data.append([message_id, {packet_id: message}])

input_file.close()

output_file = open(sys.argv[2], "w", encoding="utf8")

for i, data in enumerate(sorted(all_data)):
    output_file.write("Message {}\n".format(i + 1))
    message_id = data[0]
    dic = data[1]
    for packet_id in sorted(dic, key=int):  # get sorted by key dictionary
        output_file.write(message_id + "\t" + packet_id + "\t" + dic[packet_id] + ("\n" if "\n" not in dic[packet_id] else ""))


output_file.close()