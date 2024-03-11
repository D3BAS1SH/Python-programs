Sentence = input("Any sentence : ")
RevWords=[x[::-1] for x in Sentence.split(' ')]
print((" ".join(RevWords)))