import difflib #importing the difflib module

def wordfile_reader(): #read the wordlist.txt file
    words_list = []
    with open('wordlist.txt', 'r') as wordlist: #reading the wordlist.txt file
        for wordrow in wordlist:
            wordrow = wordrow.rstrip() #removing the \n from the end of the word
            words_list.append(wordrow) #appending words to the words_list list
    return words_list #returning the words list



def main(): #main function

    while True: #while loop to keep the program running

        correct_words = wordfile_reader() #calling the wordfile_reader function and assigning it to the correct_words variable

        text_input = input('Write text to check your spelling: ("end" breaks) ') #asking the user to write a text

        if text_input == 'end': #if the user writes 'end' the program breaks
            break

        incorrect_words = []  #list of incorrect words

        text_input = text_input.split(' ') #splitting the text into words

        for word in text_input: #looping through the words in the text
            if word.lower() in correct_words: #checking if the word is in the correct_words list
                print(f'{word} ', end='') #if the word is in the list, it prints the word
            else:
                incorrect_words.append(word) #appending the incorrect words to the incorrect_words list
                print(f'*{word}* ', end='') #printing the incorrect words with * in front and * in back
            

        print()
        print()
        print('Correction suggestions: ')

        for incorrect_word in incorrect_words: #looping through the incorrect_words list
            correction_list = difflib.get_close_matches(incorrect_word, correct_words) #creating a list of the closest matches for the incorrect word
            correction_suggestion = ', '.join(correction_list) #joining the list of closest matches of the incorrect word into a string
            print(f'{incorrect_word}: {correction_suggestion}')  #printing the incorrect word and the correction suggestions


        print()
    

    print()
    print('Program ended. Thank you for using the spellchecker!')
    print()



if __name__ == "__main__": #running the program file
    print()
    print('Welcome to the spellchecker!')
    print()


    main()#calling the main function