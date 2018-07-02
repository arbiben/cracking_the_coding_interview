
class Trie:
    def __init__(self):
        self.head = Node("*")
    
    def insert(self, word):
        if len(word) == 0:
            return
        
        self.head.insert(word)

    def starts_with(self, val):
        words = []
        if val and len(val)>0:
            self.head.starts_with(val, "", words)
        return words

class Node:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.endOfWord = False

    def insert(self, word):
        if len(word) > 0 and word[0] not in self.children:
            self.children[word[0]] = Node(word[0])
        if len(word) >= 1:
            self.children[word[0]].insert(word[1:])
        else:
            self.endOfWord = True

    def starts_with(self, word, curr, word_list):
        if len(word) == 0:
            self.get_all_words(curr, word_list)
            return

        if self.endOfWord:
            word_list.append(curr)
        
        if word[0] in self.children:
            self.children[word[0]].starts_with(
                word[1:], curr+word[0], word_list)

    def get_all_words(self, curr, word_list):
        if self.endOfWord:
            word_list.append(curr)
        
        for key, val in self.children.items():
            val.get_all_words(curr+key, word_list)

