import sys

input_file, output_file = open(sys.argv[1], "r", encoding="utf8"), open(sys.argv[2], "w", encoding="utf8")

previous_id, counter = 0, 1
for line in sorted(input_file.readlines(), key=lambda x: (int(x.split()[0]), int(x.split()[1]))):
    if line.split()[0] != previous_id:
        output_file.write("Message {}\n".format(counter))
        counter += 1
        previous_id = line.split()[0]
    output_file.write(line.replace("\t", " ") + ("\n" if "\n" not in line else ""))

input_file.close()
output_file.close()
