def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels= {a,e,i,o,u}
    vowel_indexs={}
    index=0
    for letter in s:
        if letter in vowels:
            vowel_index.add(index)
    replacements = len(vowel_indexs)-1
    if replacements < 1:
        return s
    swap_index = len(vowel_indexs)
    for num in range(swap_index/2):
        temp = s[swap_index] 
        s[swap_index] = s[num]
        s[num] = temp 
        swap_index -= 1
    
    return s

    
