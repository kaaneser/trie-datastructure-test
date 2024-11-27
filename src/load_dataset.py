import csv
from src.trie import Trie

def load_dataset(filepath, limit=100):
    trie = Trie()

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for i, row in enumerate(reader):
            if i >= limit:
                break

            word = row[0].strip()
            trie.insert(word)
    return trie