import re

def add(number_str): 
    number_str = r'{}'.format(number_str)
    if len(number_str) == 0:
        return 0
                 
    if len(number_str) == 1:
        return int(number_str)

    else:
        # extracting all numbers from the string input, both positive and negative
        num_l = re.findall(r"-?\d+", number_str)
        result = 0
        print(num_l)
        # extracting negative numbers from num_l
        neg_nums = []
        for num in num_l:
            if int(num) < 0:
                neg_nums.append(num)
        # raise exception with negative numbers
        if len(neg_nums) != 0:
            exception_msg = 'ERROR: negatives not allowed '
            for pos in range(len(neg_nums)):
                if pos != len(neg_nums) - 1:
                    exception_msg = exception_msg + neg_nums[pos] + ','
                else:
                    exception_msg = exception_msg + neg_nums[pos]
            raise Exception(exception_msg)
        for num in num_l:
            if int(num) < 1000:
                result = result + int(num)
        return result
            














