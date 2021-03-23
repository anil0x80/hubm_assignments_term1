import sys

provided_string = sys.argv[1]

number_list = [int(x) for x in provided_string.split(',') if int(x) > 0]  # parse the list to our needs
even_numbers = [x for x in number_list if x % 2 == 0]  # create new list which contains even numbers

even_numbers_sum = sum(even_numbers)  # save this so don't recalculate it again later
even_number_rate = even_numbers_sum / sum(number_list)

# ghetto work for printing
print('Even Numbers: "', end='')
print(*even_numbers, sep=",", end='"\n')  # print even numbers separated by comma, wrap inside quote marks

print("Sum of Even Numbers: ", even_numbers_sum)
print("Even Number Rate: {:.3f}".format(even_number_rate))  # match output precision as shown at quiz instruction
