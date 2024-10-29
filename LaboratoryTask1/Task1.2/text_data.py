import re

class TextData:
    def __init__(self, text: str, fileName: str):
        self.fileName = fileName
        self.text = text
        self.numberOfVowels = self.countVowels()
        self.numberOfConsonants = self.countConsonants()
        self.numberOfLetters = self.numberOfVowels + self.numberOfConsonants
        self.numberOfSentences = self.countSentences()
        self.longestWord = self.findLongestWord()

    def countVowels(self) -> int:
        return sum(1 for char in self.text.lower() if char in 'aeiou')

    def countConsonants(self) -> int:
        return sum(1 for char in self.text.lower() if char.isalpha() and char not in 'aeiou')

    def countSentences(self) -> int:
        return len(re.findall(r'[.!?]', self.text))

    def findLongestWord(self) -> str:
        words = re.findall(r'\b\w+\b', self.text)
        longestWord = ""
        for word in words:
            if len(word) > len(longestWord):
                longestWord = word
        return longestWord

    def __str__(self):
        return (
            f"File Name: {self.fileName}\n"
            f"Text: {self.text}\n"  
            f"Number of Vowels: {self.numberOfVowels}\n"
            f"Number of Consonants: {self.numberOfConsonants}\n"
            f"Number of Letters: {self.numberOfLetters}\n"
            f"Number of Sentences: {self.numberOfSentences}\n"
            f"Longest Word: {self.longestWord}\n"
        )