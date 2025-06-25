# Word Frequency Analyzer
This project analyzes the most frequent words in a given English text using basic Natural Language Processing (NLP) techniques.

## 🔍 What It Does
- Loads a plain text file (e.g. Wikipedia article)
- Tokenizes the text into words
- Removes English stopwords and punctuation
- Counts word frequency using `Counter`
- Displays the top 10 most frequent words

## 📁 Project Structure
word_frequency_analyzer/

├── main.py # Main script to run the analysis

├── sample.txt # Input text file (Wikipedia content)

├── venv/ # Python virtual environment (optional)

└── README.md # Project description

## 🚀 How to Run
1. Clone the repository:
git clone https://github.com/your-username/word_frequency_analyzer.git
cd word_frequency_analyzer

2. (Optional) Create a virtual environment:
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install dependencies:
pip install nltk

4. Download required NLTK resources:
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

5. Run the script:
python main.py

## 📝 Sample Output
Top 10 most frequent words:

language: 34

processing: 28

text: 21

data: 18

model: 17

...

## 📌 Notes
- The sample text is from Wikipedia: "Natural Language Processing"
- NLTK is used for tokenization and stopword filtering

## 🛠️ Skills Demonstrated
- Python scripting
- Text preprocessing
- Tokenization
- Frequency analysis
- Working with NLTK
