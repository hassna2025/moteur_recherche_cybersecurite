import sqlite3
from collections import Counter
from extraction import extraire_documents
from linguistic import traiter_texte

DB_PATH = "database/moteur_recherche.db"
CORPUS_PATH = "corpus"

def indexer_corpus():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    documents = extraire_documents(CORPUS_PATH)

    for doc in documents:
        cursor.execute("""
            INSERT INTO documents (titre, chemin, contenu, type, categorie)
            VALUES (?, ?, ?, ?, ?)
        """, (
            doc["titre"],
            doc["chemin"],
            doc["contenu"],
            doc["type"],
            doc["categorie"]
        ))

        doc_id = cursor.lastrowid

        termes = traiter_texte(doc["contenu"])
        frequences = Counter(termes)

        for terme, freq in frequences.items():
            cursor.execute("""
                INSERT OR IGNORE INTO keywords (mot)
                VALUES (?)
            """, (terme,))

            cursor.execute("""
                SELECT id FROM keywords WHERE mot = ?
            """, (terme,))
            mot_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO indexation (document_id, keyword_id, frequence)
                VALUES (?, ?, ?)
            """, (doc_id, mot_id, freq))

    conn.commit()
    conn.close()
    print("✅ Indexation linguistique avancée terminée")

if __name__ == "__main__":
    indexer_corpus()
