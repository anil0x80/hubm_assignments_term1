import sys

final_size = int(sys.argv[1])

upper_diamond = [print((((2 * n) - 1) * '*').center(final_size * 2 - 1)) for n in range(1, final_size + 1)]
lower_diamond = [print((((2 * i) - 1) * '*').center(final_size * 2 - 1)) for i in range(final_size - 1, 0, -1)]
