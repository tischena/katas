def rotate_list_func(input_list, input_num):
    output_list = []
    if input_num >= 1:
        first_part = input_list[-input_num:]
        leftover_num = len(input_list) - input_num
        second_part = input_list[:leftover_num]
        output_list = first_part + second_part
    elif input_num <= -1:
        first_part = input_list[-input_num::]
        second_part = input_list[:-input_num]
        output_list = first_part + second_part
    else:
        output_list = input_list
    return output_list