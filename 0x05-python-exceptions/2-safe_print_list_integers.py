#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for val in range(x):
        try:
            print("{:d}".format(val))
        except ValueError:
            continue
        except IndexError:
            break
        else:
            count += 1
    return count
