def single_root_words(root_word, *other_words):
  same_words=[]
  for i in other_words:
    if other_words==root_word:
      same_words.append(other_words)
      return same_words

  
