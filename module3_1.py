calls = 0
def count_calls():
    global calls
    calls+=1
    

def string_info(string="String"):
    count_calls()
    print(len(string))
    string_tuple=(len(string), string.lower(), string.upper())
    return string_tuple



print(string_info())



def is_contains(content="AaA", list_to_search=["AAA"]):
  count_calls()
  for i in list_to_search:
      print(list_to_search[i])
      #if list_to_search[i].upper() == content:
          #print({EQ})



is_contains()


#print(string_info('Capybara'))
#print(string_info('Armageddon'))
#print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
#print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
#print(calls)

