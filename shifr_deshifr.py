import os
from random import randint as rand
class shifr:
    """"Returns coded string"""
    tog=''
    def shifrovka(self,text_for_coding):
        text = text_for_coding.split()
        text_coded = []
        for i in text:
            word_coded = []
            buf = list(i)
            for i1 in buf:
                _buf=bin(ord(i1))
                word_coded.append(_buf)
            data = self.tog.join(word_coded)
            text_coded.append(data)
        text_coded = self.tog.join(text_coded)
        return text_coded




