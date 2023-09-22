from itertools import islice
# def print_first_n_set_values( set_tb_printed, num_to_print ):
#     print(f'First {num_to_print} SET values:')
#     print(f'  { {list_elem for list_elem in list(set_tb_printed)[:num_to_print]  } }')
    
def take(n, iterable):
    print(list(islice(iterable, n)))
    
