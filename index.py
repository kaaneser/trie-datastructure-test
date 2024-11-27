from src.load_dataset import load_dataset
from src.visualize import visualize_trie
from src.trie import Trie

def main():
    filepath = 'dataset/unigram_freq.csv'
    trie = load_dataset(filepath, limit=200)
    
    visualize_trie(trie)

    print("\nAutocomplete Test")
    prefix = input("Add a prefix: ")

    suggestions = trie.search(prefix)

    if suggestions:
        print(f"The words can be completed for the prefix '{prefix}':")
        
        for word in suggestions:
            print(word)
        
    else:
        print(f"Couldn't find any matching words for the prefix '{prefix}'")

if __name__ == '__main__':
    main()