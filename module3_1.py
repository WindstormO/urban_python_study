calls = 0
def count_calls():
    global calls
    calls+=1
    

def string_info(string="String"):
    count_calls()
    print(len(string))
    string_tuple=(len(string), string.lower(), string.upper())
    return string_tuple


def is_contains(content="", list_to_search=[""]):
  result = False
  count_calls()
  for item in list_to_search[:]:
    if item.lower()==content.lower():
        result = True
  return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

