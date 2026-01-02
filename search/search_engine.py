from collections import defaultdict
from search.db_connection import get_connection
from indexing.linguistic import traiter_texte


def rechercher(requete):
    conn = get_connection()
    cursor = conn.cursor()

    # Traitement linguistique de la requête
    termes = traiter_texte(requete)

    scores = defaultdict(int)
    documents = {}

    for terme in termes:
        cursor.execute("""
            SELECT d.id, d.titre, d.chemin, i.frequence
            FROM keywords k
            JOIN indexation i ON k.id = i.keyword_id
            JOIN documents d ON d.id = i.document_id
            WHERE k.mot = ?
        """, (terme,))

        resultats = cursor.fetchall()

        for doc_id, titre, chemin, freq in resultats:
            scores[doc_id] += freq
            documents[doc_id] = (titre, chemin)

    conn.close()

    # Classement par score décroissant
    classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [
        {
            "titre": documents[doc_id][0],
            "chemin": documents[doc_id][1],
            "score": score
        }
        for doc_id, score in classement
    ]


def enregistrer_requete(requete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO requetes (terme) VALUES (?)",
        (requete,)
    )
    conn.commit()
    conn.close()
def enregistrer_consultation(document_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO consultations (document_id) VALUES (?)",
        (document_id,)
    )
    conn.commit()
    conn.close()
