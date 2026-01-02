import os
from PyPDF2 import PdfReader

def lire_txt(chemin):
    with open(chemin, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def lire_pdf(chemin):
    texte = ""
    reader = PdfReader(chemin)
    for page in reader.pages:
        texte += page.extract_text() or ""
    return texte

def extraire_documents(dossier_corpus):
    documents = []

    for racine, _, fichiers in os.walk(dossier_corpus):
        categorie = os.path.basename(racine)

        for fichier in fichiers:
            chemin = os.path.join(racine, fichier)

            if fichier.endswith(".txt"):
                contenu = lire_txt(chemin)
                type_doc = "txt"

            elif fichier.endswith(".pdf"):
                contenu = lire_pdf(chemin)
                type_doc = "pdf"

            else:
                continue

            documents.append({
                "titre": fichier,
                "chemin": chemin,
                "contenu": contenu,
                "type": type_doc,
                "categorie": categorie
            })

    return documents
