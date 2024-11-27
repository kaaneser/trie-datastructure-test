
#  Auto Completion System Using Trie Data Structure

  

This project is an example of a system that uses the Trie data structure to implement auto-completion and word suggestion. The system suggests possible words based on user input by leveraging a word list and the Trie structure.

  

###  About the Project

  

This project demonstrates how to use **Trie** data structure for:

-  Word insertion

-  Prefix search

-  Auto-completion suggestions

-  Visualizing the Trie structure

  

###  Use Cases

  

-  **Search engines**: Improving results with word suggestions

-  **Spell checking and correction**: Suggesting alternative words for misspelled input

-  **Profanity filtering**: Detecting and blocking inappropriate words

  

##  Installation

  

To use this project, follow these steps:

  

1.  **Clone the Repository**

```
git clone https://github.com/kaaneser/trie-datastructure-test.git
```

2.  **Install the Required Dependencies**

To install the necessary Python libraries, run the following command:

```
pip install -r requirements.txt
```
3. **Download the Dataset**

The word data used in this project is obtained from Rachael Tatman's dataset from Kaggle here: [rtatman/english-word-frequency](https://www.kaggle.com/datasets/rtatman/english-word-frequency?resource=download)

4. **Run the Project**

Run the `index.py` file to start the project. This command will load the words from specified dataset and build the Trie structure to perform auto-completion:
```
python index.py
```

## Project Structure

-   **index.py**: The entry point of the program, which loads the dataset using the `load_dataset` function and visualizes the Trie using the `visualize_trie` function.
-   **trie.py**: This file contains the definition of the Trie data structure, including methods for adding words, searching for prefixes, and collecting words in the Trie.
-   **visualize.py**: This file handles the visualization of the Trie structure using `matplotlib` and `networkx`.
-   **load_dataset.py**: This file is responsible for loading the dataset and populating the Trie structure with the words.

## Contributing

This project is open-source and contributions are welcome. Feel free to fork the repository and submit your contributions.

## License

This project is licensed under the MIT License.