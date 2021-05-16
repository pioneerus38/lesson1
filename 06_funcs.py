def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'
a = get_summ("Learn", "python").upper()
print(a)