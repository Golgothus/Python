print('In this program we will take your input ' \
'and translate it to pig Latin (supposedly).')

def response():
    a = input('Type in your input here - ')
    pyg = ""
    if a.isalpha():
        for c in range (1, len(a)):
            pyg += a[c]
        pyg += a[0]
        pyg += "ay"
        return print(pyg)
    else:
        print('Please insert a response with no ' \
              'symbols/numbers')
        response()

response()