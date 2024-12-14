"""
11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
    """
sentence=str(input("Enter the sentence "))
characters=set()
for char in sentence:
    if char in characters:
        continue
    else:
        print(f"{char}->{sentence.count(char)}")
        characters.add(char)
    
