import sys


def getoutput(*nums):
    out = ""
    for it in nums:
        for count, dig in enumerate(it):
            out += str(dig) + (" + " if count + 1 != len(it) else "")
    return out


number = int(sys.argv[1])
exp = int(sys.argv[2])
result = number ** exp
result_backup = result

sums = []
total_sum = 0
total_digits = []
while len(str(total_sum)) != 1 or total_sum == 0:
    res = [int(i) for i in str(result)]
    total_sum = sum(res)
    total_digits.append(res)
    result = total_sum
    sums.append(total_sum)

output = "{}^{} = {} = ".format(number, exp, result_backup)
for i, digit in enumerate(total_digits):
    output += getoutput(digit)
    output += " = "
    output += str(sums[i]) + (" = " if i + 1 != len(total_digits) else "")

print(output)
