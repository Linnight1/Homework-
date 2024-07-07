import string
class WordsFinder:


    def __init__(self,*args,file_names = []):
        self.args = args
        self.file_names = file_names
        for i in self.args:
            self.file_names.append(i)
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i,"r",encoding = "utf-8") as f:
                all_words[i] = (("").join(f.readlines()).replace("\n"," ").
                                translate(str.maketrans('', '', string.punctuation)).lower()).split(" ")


        return all_words

    def find(self, word):
        self.word = word
        word_dict = {}

        for key, value in WordsFinder.get_all_words(self).items():
            if self.word.lower() in value:
                word_dict[key] = value.index(word.lower()) + 1
                return word_dict

    def count(self, word):
        self.word = word
        word_dict1 = {}

        for key, value in WordsFinder.get_all_words(self).items():
            if self.word.lower() in value:
                word_dict1[key] = value.count(word.lower())
                return word_dict1



Wf = WordsFinder("Strings.txt")
print(Wf.get_all_words())
print(Wf.find("arE"))
print(Wf.count("спасибО"))