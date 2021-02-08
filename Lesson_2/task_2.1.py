my_str = 'искать таксИ'
revers_str = my_str[::-1]
my_list = [1, 17, 24,78, 'redemption', 117.23]
my_list.append('shawshenk')
my_list.reverse()
my_tuple = ('manchester', 'united')
my_scores_1 = set('volan de mort')
my_scores_2 = frozenset('harry potter')
my_scores_1.discard('vol, an')
my_dict = {'class': 'mage', 'race': 'human', 'age': '17'}
ussr_list = [revers_str,my_list,my_tuple,my_scores_1,my_scores_2,my_dict.copy() ]
for i in ussr_list:
    print(f'{i}, is {type(i)}')