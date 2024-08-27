calls = 0
def count_calls():
  global calls+=1


def string_info(string):
  count_calls()


def is_contains(string, list_to_search):
  count_calls()


print(f"Количество вызванных функций: {calls}")
