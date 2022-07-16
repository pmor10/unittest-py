# Debugging

# linting
# ide/ editor
# pdb

# testing with print
# def add(num1, num2):
#     print('************TEST TEST TEST**************', num1, num2)
#     return num1 + num2


# add(4, 'abd')
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 'dafaf')
