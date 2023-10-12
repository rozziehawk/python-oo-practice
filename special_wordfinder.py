
from  wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """ extends Wordfinder, but processes data differently"""
    def __init__(self, dictionary_file):
        print("inside subclass constructor")
        super().__init__(dictionary_file)

    def ignore_line(self, line):
        ### returns true if the line being read from the file needs to be skipped
        print("inside ignore_line in subclass")
        skip_line = super().ignore_line(line)
        if (line.lstrip()[0]== "#"):
            skip_line = True
        
        return skip_line
        
    