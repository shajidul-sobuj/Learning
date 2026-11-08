# ---------------------------------------------------------------------------------------------
# serial bad diye, key dhore, jekono order ee parameters pass kora jay

def full_name(first, last):
    name = f'{first} {last}'
    return name

# name = full_name('sobuj', 'kazi')   # normally serial wise parameter pass kore
# print(name)

# name = full_name(last='sobuj', first='kazi')   # key dhore parameter pass kore
# print(name)

# ___________________________________________________________________________________________--

# args er moto uncount parameters pass kora jay

def name_gula(**names):
    for key, val in names.items():
        print(key ," -> ", val)
    print(names)

name_gula(first='sobuj', last='kazi', nick='sajid')


# https://codeforces.com/contests/2284