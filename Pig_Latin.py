def Pig_Latin():
    print "Pig Latin"
    string = raw_input("Input word in English :")
    length = len(string)
    if(length == 0 and string.isalpha() == False):
        Pig_Latin()
    else:
        string = string[1:length] + string[0] + 'ay'
        print string.lower()
Pig_Latin()
