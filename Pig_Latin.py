#Pig_Latin that I learn from https://www.codecademy.com
def Pig_Latin():
    print "Pig Latin"
    string = raw_input("Input word in English :") #print a word in a double quotation marks and insert a user input to a string variable
    length = len(string)    #count a string alphabet
    if(length == 0 and string.isalpha() == False):  #check if no a alphabet in a string or is a number in a string
        print "There is no a word to input or there is number in a word"
        print "Let try again"
        Pig_Latin()
    else:
        string = string[1:length] + string[0] + 'ay' #Pig_Latin game process
        print string.lower()
Pig_Latin()
