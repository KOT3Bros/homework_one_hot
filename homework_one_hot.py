'''
Задача 44: В ячейке ниже представлен код генерирующий
DataFrame,которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?
'''

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI': lst})
print(df)
# print(pd.get_dummies(df['whoAmI']))

def convert_to_one_hot(data):
    colums_names = list(set(data))
    dict_for_one_hot_df = {column_name: (data == column_name).astype(int) for column_name in colums_names}
    one_hot_df = pd.DataFrame(dict_for_one_hot_df)
    print(one_hot_df)

convert_to_one_hot(df['whoAmI'])