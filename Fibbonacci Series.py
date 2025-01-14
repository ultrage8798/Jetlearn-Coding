
def reverse_string(words):
    if len(words)==0:
        return ""
    else:
        return words[-1]+reverse_string(words[:-1])
    
print(reverse_string("vikram"))

    