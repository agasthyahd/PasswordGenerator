import pandas
import string
import random


if __name__ == '__main__':

    s = string.ascii_lowercase
    # print(s)
    s2 = string.ascii_uppercase

    s3 = string.digits
    # print(s3)

    pass_len = int(input('Enter the length of your password.\n'))
    pass_list = []
    pass_list.extend(list(s)*10)
    pass_list.extend(list(s2)*10)
    pass_list.extend(list(s3)*10)

    random.shuffle(pass_list)


    pass_generated = "".join(pass_list[0:(pass_len)])

    printsent='Password generated!\nYour password is {}';
    print(printsent.format(pass_generated))
