import spacy
from nltk.stem.snowball import SnowballStemmer

nlp = spacy.load("fr_core_news_sm")
stemmer = SnowballStemmer("french")

def charger_stopwords(path="data/stopwords_fr.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return set(m.strip() for m in f.readlines())

STOPWORDS = charger_stopwords()

def traiter_texte(texte):
    doc = nlp(texte)
    termes = []

    for token in doc:
        if token.is_alpha:
            lemme = token.lemma_.lower()

            if lemme not in STOPWORDS and len(lemme) > 2:
                radical = stemmer.stem(lemme)
                termes.append(radical)

    return termes
