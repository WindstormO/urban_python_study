def print_params(a = 1, b = "@"строка", c = True):
  print(a, b, c)


print_params(25)
print_params(c=[1, 2, 3])

values_list=[2, "строчечка", True]
values_dict=[1: 3, 2: "строченечка", 3: False]

print_params(*values_list)
print_params(**values_dict)

values_list_2=[True, 4]
print_params(*values_list_2, 42)
