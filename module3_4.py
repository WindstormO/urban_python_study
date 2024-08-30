def single_root_words(root_words, *other_words):
    """Функция, определяющая однокоренные слова"""
    same_words=[]
    for words in range(len(other_words)):
        if root_words in other_words:
            same_words.append(root_words)
        elif other_words[words] in root_words:
            same_words.append(root_words)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
        
