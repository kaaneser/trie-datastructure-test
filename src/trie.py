class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]
        
        current.is_end_of_word = True
    
    def search(self, prefix):
        current = self.root

        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return []
        
        return self._collect_words(current, prefix)

    def _collect_words(self, node, prefix):
        words = []
        
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            words.extend(self._collect_words(child, prefix + char))

        return words
