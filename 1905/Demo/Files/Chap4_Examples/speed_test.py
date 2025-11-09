import timeit

city_code_dict = {
    'HNL': 'Honolulu',
    'ITO': 'Hilo',
    'LHR': 'London/Heathrow',
    'ARN': 'Stockholm/Arlanda',
    'HKG': 'Hong Kong',
    'YYZ': 'Toronto',
    'CDG': 'Paris/Charles de Gaulle',
    'NRT': 'Tokyo/Narita',
    'GCM': 'Grand Cayman BWI',
    'CUR': 'Curacao Netherland Antilles'}
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY']

def codes_via_loop():
    are_keys = []
    not_keys = []
    for code in codelist:
        if code in city_code_dict:
            are_keys.append(code)
        else:
            not_keys.append(code)
    # print('are keys in city_code_dict', are_keys)
    # print('not keys in city_code_dict', not_keys)
    temp_keys = ','.join(are_keys)
    temp_keys = ','.join(not_keys)


def codes_via_comp():
    are_keys = [code for code in codelist if code in city_code_dict]
    not_keys = [code for code in codelist if code not in city_code_dict]
    # print('are keys in city_code_dict', are_keys)
    # print('not keys in city_code_dict', not_keys)
    temp_keys = ','.join(are_keys)
    temp_keys = ','.join(not_keys)

def codes_via_gen():
    are_keys = (code for code in codelist if code in city_code_dict)
    not_keys = (code for code in codelist if code not in city_code_dict)
    # print('are keys in city_code_dict', are_keys)
    # print('not keys in city_code_dict', not_keys)
    # print('are keys in city_code_dict', ','.join(are_keys))
    # print('not keys in city_code_dict', ','.join(not_keys))
    temp_keys = ','.join(are_keys)
    temp_keys = ','.join(not_keys)

def codes_via_sets():
    are_keys = list(set(codelist) & set(city_code_dict))
    not_keys = list(set(codelist) - set(city_code_dict))
    # print('are keys in city_code_dict', are_keys)
    # print('not keys in city_code_dict', not_keys)
    temp_keys = ','.join(are_keys)
    temp_keys = ','.join(not_keys)

# codes_via_loop()
# codes_via_comp()
# codes_via_gen()
# codes_via_sets()

num = 100000
times = dict()
times['loop'] = timeit.timeit(stmt=lambda : codes_via_loop, number=num)
times['comp'] = timeit.timeit(stmt=lambda : codes_via_comp, number=num)
times['gen'] = timeit.timeit(stmt=lambda : codes_via_gen, number=num)
times['sets'] = timeit.timeit(stmt=lambda : codes_via_sets, number=num)

for m, t in times.items():
    print(f'the {m} menthod took {t:.6f}')
