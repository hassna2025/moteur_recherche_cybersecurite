import re

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ\s]", " ", texte)
    texte = re.sub(r"\s+", " ", texte)
    return texte.strip()

def tokeniser(texte):
    return texte.split()
