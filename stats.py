l_list = "q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0 ! £ $ % ^ & * ( ) : @ ~ < > ? [ ] ; ' # , . / |    "
lettercount = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0, 'a': 0, 's': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0, 'z': 0, 'x': 0, 'c': 0, 'v': 0, 'b': 0, 'n': 0, 'm': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0, '!': 0, '£': 0, '$': 0, '%': 0, '^': 0, '&': 0, '*': 0, '(': 0, ')': 0, ':': 0, '@': 0, '~': 0, '<': 0, '>': 0, '?': 0, '[': 0, ']': 0, ';': 0, "'": 0, '#': 0, ',': 0, '.': 0, '/': 0, '|': 0}
new_list = []

def count_words(foo):
    count = 0
    word_count = foo.split()
    for i in range (0, len(word_count)):
        count += 1
    return count
    #print(f"{count} words found in the document")
    
def count_characters(foo):
    new_l_list = l_list.split()
    for occurence in foo:
        lowercase_letter = occurence.lower()
        for letter in new_l_list:
            if lowercase_letter == letter:
                lettercount[letter] += 1
    return lettercount
    
            
def print_report(letter_dict, wordcount, bookname):
    for key, value in letter_dict.items():
        new_list.append({"char": key, "num": value})
    #sort_on(new_list)
    new_list.sort(reverse=True, key=sort_on)
    
    ##Results below for printing the Report
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {bookname}")
    print ("----------- Word Count ----------")
    print (f"Found {wordcount} total words")
    print ("--------- Character Count -------")
    for i in range(0,len(new_list)):
        print (f"{new_list[i]["char"]}: {new_list[i]["num"]}")
    print("============= END ===============")

def sort_on(e):
    return e["num"]
    