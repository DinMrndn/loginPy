class Known:
    isUnknown = True
def checkIfIn():
    Known.isUnknown = True
    splitter = sentence.lower().split(" ")
    number = 0
    try:
        while number != 10000:
            #checks and write the words
            nounCheck(splitter[number])
            adjectiveCheck(splitter[number])
            adverbCheck(splitter[number])
            conjunctionCheck(splitter[number])
            verbCheck(splitter[number])
            articleCheck(splitter[number])
            #append word to text documents
            if Known.isUnknown:
                print(splitter[number] + " = ?")
                newWord = int(input("Unknown Word! Is this a/an:\n1. Noun\n2. Adverb\n3. Adjective\n4. Conjunction\n5. Verb\n6. Article\n:"))
                if newWord == 1:
                    file = open("noun.txt", "a")
                    file.write(splitter[number] + "\n")
                    file.close()
                elif newWord == 2:
                    file = open("adverb.txt", "a")
                    file.write(splitter[number] + "\n")
                    file.close()
                elif newWord == 3:
                    file = open("adjective.txt", "a")
                    file.write(splitter[number] + "\n")
                    file.close()
                elif newWord == 4:
                    file = open("conjunction.txt", "a")
                    file.write(splitter[number] + "\n")
                    file.close()
                elif newWord == 5:
                    file = open("verb.txt", "a")
                    file.write(splitter[number] + "\n")
                    file.close()
                elif newWord == 6:
                    file = open("article.txt", "a")
                    file.write(splitter[number] + "\n")
                    file.close()
            number += 1
            Known.isUnknown = True
    except:
        print("Done")

isUnknown = True

def nounCheck(word):
    with open('noun.txt') as Dfile:
        if word in Dfile.read():
            print(word + " = Noun")
            Known.isUnknown = False
def adjectiveCheck(word):
    with open('adjective.txt') as Dfile:
        if word in Dfile.read():
            print(word + " = Adjective")
            Known.isUnknown = False
def adverbCheck(word):
    with open('adverb.txt') as Dfile:
        if word in Dfile.read():
            print(word + " = Adverb")
            Known.isUnknown = False
def conjunctionCheck(word):
    with open('conjunction.txt') as Dfile:
        if word in Dfile.read():
            print(word + " = Conjunction")
            Known.isUnknown = False
def verbCheck(word):
    with open('verb.txt') as Dfile:
        if word in Dfile.read():
            print(word + " = Verb")
            Known.isUnknown = False
def articleCheck(word):
    with open('article.txt') as Dfile:
        if word in Dfile.read():
            print(word + " = Article")
            Known.isUnknown = False

while True:
    sentence = input("Enter a sentence.\n:")
    checkIfIn()
    if input("Do you want to continue: y/n:").lower() == "n":
        break