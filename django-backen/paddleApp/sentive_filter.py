import os
import re
import time
from collections import defaultdict


# 敏感词过滤
class BSFilter:


    def __init__(self):
        self.keywords = []
        self.kwsets = set([])
        self.bsdict = defaultdict(set)
        self.pat_en = re.compile(r'^[0-9a-zA-Z]+$')  # english phrase or not

    def add(self, keyword):

        keyword = keyword.lower()
        if keyword not in self.kwsets:
            self.keywords.append(keyword)
            self.kwsets.add(keyword)
            index = len(self.keywords) - 1
            for word in keyword.split():
                if self.pat_en.search(word):
                    self.bsdict[word].add(index)
                else:
                    for char in word:
                        self.bsdict[char].add(index)

    def parse(self, path):
        with open(path, 'r', encoding='UTF-8') as f:
            for keyword in f.readlines():
                self.add(keyword.strip())

    def filter(self, message, repl="*"):
        sen_text = ""
        ini_message = message.lower()
        message = message.lower()
        for word in message.split():
            if self.pat_en.search(word):
                for index in self.bsdict[word]:
                    message = message.replace(self.keywords[index], repl)
            else:
                for char in word:
                    for index in self.bsdict[char]:
                        message = message.replace(self.keywords[index], repl)

        if ini_message == message:
            sen_text = ""
        else:
            result_str = message.split(repl)
            for item in result_str:
                ini_message = ini_message.replace(item,"")
            sen_text = ini_message
        return message,sen_text

def filter_sen_txt(input_str):
    filter = BSFilter()
    filter.parse(os.getcwd() +"\paddleApp\sensi_words.txt")
    result,sen_text = filter.filter(input_str.replace('*',''),repl="*")
    return  result,sen_text
