import roman2int_func as ri # replace with your code file
import timeit

test_rn = {'III':3, 'LVIII':58, 'MCMXCIV': 1994, "MCMLXXIV": 1974, "MMCDLIX": 2459,
           'MMMDCCCLXXXVIII':3888, 'MDCI':1601, 'CMXCIX': 999, "MMMCCXLV": 3245, "MCDXCII": 1492,
           'MMDCCXVIII':2718, 'DCCCXLII':842, 'MMMDLXX': 3570, "CDXLIV": 444, "MCMXCIX": 1999,
           'MMDCCCI':2801, 'MMMCMXL':3940, 'DCCLXXVII': 777, "MMCMLXV": 2965, "MCCCXLIX": 1349,
           'II':2, 'VIII':8, 'DCXXIII': 623, "MMCMXCVII": 2997, "MMMCXII": 3112}

def dummy_func(rn):
    return test_rn[rn]

def test_a_func(func):
    results = dict()
    for rn,val in test_rn.items():
        ret = func(rn)
        results[rn] = ret == val
        if results[rn] is False:
            print(f'funciton {func.__name__} failed on {rn} returned {ret} instead of {val}')
    return results
            
test_a_func(dummy_func) # replace with your imported function

# # test_a_func(ri.romanToInt_simple)
# test_a_func(ri.romanToInt_prev)
# test_a_func(ri.romanToInt_replace_chain)
# test_a_func(ri.romanToInt_replace)
# test_a_func(ri.romanToInt_numlist)
# test_a_func(ri.romanToInt_negmap)
# test_a_func(ri.romanToInt_lookahead)
# test_a_func(ri.romanToInt_bytwos)
# test_a_func(ri.romanToInt_replace_noalg)

func_dict = {"previous": ri.romanToInt_prev, "rep_chain" : ri.romanToInt_replace_chain, "replace" : ri.romanToInt_replace,
             "numlist" : ri.romanToInt_numlist, "negmap": ri.romanToInt_negmap, "lookahead" : ri.romanToInt_lookahead,
             "bytwos": ri.romanToInt_bytwos, "rep_noalg" : ri.romanToInt_replace_noalg}
time_dict = dict()
loop = 10000
for name, func in func_dict.items():
    time_dict[name] = timeit.timeit(stmt=lambda : test_a_func(func_dict[name]), number=loop)
sorted_items = sorted(time_dict.items(), key=lambda item: item[1])
sorted_dict = dict(sorted_items)

# print(sorted_dict)
for ky,val in sorted_dict.items():
    print(f'function: {ky}\ttime:{val:.9f}')