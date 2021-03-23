import sys


def do_output(size=1):
    print(("*" * abs(size)).center(final_size * 2 - 1))
    if abs(size) == final_size * 2 - 1 or size == -1:
        return
    do_output(size + 2)


final_size = int(sys.argv[1])
if final_size == 1:
    print("*")
    exit()
if final_size < 1:
    exit()
do_output()
do_output(-((final_size * 2 - 1) - 2))
