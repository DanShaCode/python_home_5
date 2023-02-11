def Abc_Remove(text):
    print()
    text = text.split()
    text = [i for i in text[:] if i != 'абв']
    return text


