class TextAnalyzer:
    def __init__(self, text):
        formattedText = text.lower() \
        .replace(".", " ") \
        .replace(","," ") \
        .replace("?"," ") \
        .replace("!"," ")
        self.text = formattedText
        
    def freqAll(self):
        dictionary = {}
        list_word = []
        list_word = self.text.split()
        for key in set(list_word):  # SET se utiliza para eliminar duplicados
            dictionary[key] = list_word.count(key)
            
        return dictionary
        
        
    def freqOf(self, word):
        words_freqAll = self.freqAll()
        if word in words_freqAll.keys():
            return words_freqAll[word]
        else: 
            print("Word not found")