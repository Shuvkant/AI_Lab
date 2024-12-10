"""
11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
    """
sentence=str(input("Enter the sentence "))
for each in sentence:
    counter=sentence.count(sentence)
    print(f"{each} {counter}")

