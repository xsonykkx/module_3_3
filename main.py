def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(True)
print_params(6, 'привет', False)
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = ['hello world', 52, False]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'Hello']
print_params(*values_list_2, 42)