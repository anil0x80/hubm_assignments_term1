import sys

lucky_numbers = [int(i) for i in sys.argv[1].split(",") if int(i) > 0]

for idx, i in enumerate(lucky_numbers):
    to_remove = i - 1 if i != 1 else i
    for item in lucky_numbers:
        if to_remove < len(lucky_numbers):
            del lucky_numbers[to_remove]
            if i != 1:
                to_remove -= 1
        to_remove += i

print(*lucky_numbers)
