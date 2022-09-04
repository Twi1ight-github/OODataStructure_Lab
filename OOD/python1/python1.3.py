def highlight(sentense, word):
    return sentense.replace(word, "["+word+"]")


print("*** Reading E-Book ***")
text,hl = input("Text , Highlight : ").split(",")
print(highlight(text,hl))




    