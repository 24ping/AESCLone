import numpy as np

def switch_col(sub_col):
    sub_col = hexTodec(sub_col)
    list_col = []
    list_row = []
    switch_col = {1: [], 2: [], 3: [], 4: []}
    add_result= [0, 0, 0, 0]
    # in the next i am choosing the col and the row for which i will perform the proudct of them both
    for key in sub_col:
        list_col.append(sub_col[key])
        list_row.append(sub_col[1][key-1])
        list_row.append(sub_col[2][key-1])
        list_row.append(sub_col[3][key-1])
        list_row.append(sub_col[4][key-1])
        # below we have a problem the value increases to above 1000
        mul_result = np.multiply(list_col, list_row)
        add_result = np.add(mul_result, add_result)
        add_result = add_result.tolist()# this is used to convert teh vectors to lists
        switch_col.update({key: add_result[0]})
        list_col = []
        list_row = []
    return switch_col


def hexTodec(hex_col):
    dec_col = {1: [], 2: [], 3: [], 4: []}
    dec_list = []
    for key in hex_col:
        for elements in hex_col[key]:
            dec_val = int(elements, 16)
            dec_list.append(dec_val)
        dec_col.update({key: dec_list})
        dec_list = []
    return dec_col


fourth = {1: [' 09 ', ' 00 ', ' C5 ', ' 6B '], 2: [' 4A ', ' AF ', ' 5A ', ' 77 '], 3: [' 4C ', ' 7C ', ' C9 ', ' B1 '], 4: [' A0 ', ' 00 ', ' 7B ', ' CD ']}
fifth = switch_col(fourth)
print(fifth)
# the first result = {1: [81, 0, 14972, 17120], 2: [81, 30625, 26132, 17120], 3: [15053, 41785, 66533, 38891], 4: [32173, 41785, 88304, 80916]}