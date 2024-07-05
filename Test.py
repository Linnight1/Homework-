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
                all_words[i] = ((("").join(f.readlines()).translate(str.maketrans('', '', string.punctuation)).lower())).split(" ")


        return all_words

Wf = WordsFinder("Strings.txt")
print(Wf.get_all_words())
