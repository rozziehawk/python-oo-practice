"""Word Finder: finds random words from a dictionary."""
from random import randint


class WordFinder:
    """Look up a random word in a dictionary read from a file"""

    def __init__(self, dictionary_file):
        #print("base class constructor")
        self.dictionary_list = []
        self.num_words = 0;

        self.file = open(dictionary_file, "r")
        #print("calling create_dictionary_list")
        self.create_dictionary_list()
        
    
    def create_dictionary_list(self):
        """create a list from the words in a file, stripping white space (including new lines)"""
        #print("inside create_dictionary_list (base class)")
        for line in self.file:
            #self.proces_line(line)
            #self.dictionary_list.append(line.strip()) #remove white space/newlines
            if (not self.ignore_line(line)):
                self.dictionary_list.append(self.process_line(line))
                self.num_words +=1
            else:
                continue

        self.file.close()

    def ignore_line(self, line):
        ### returns true if the line being read from the file needs to be skipped
        #print("inside ignore_line in base class")
        skip_line = False
        if (len(line) == 0 or line.isspace()):
            #print(f"skipping line (base) --> {line}")
            skip_line = True
        return skip_line

    def process_line(self, line): # created in case derived class needs to process data differently
        line = line.strip()
        return(line)



    def get_random_word(self):
        """look up a random word in our word list"""
        index = randint(0, self.num_words - 1)
        #print(f"Index: {index}")
        return(self.dictionary_list[index])

