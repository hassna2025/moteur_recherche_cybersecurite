import sqlite3
from collections import Counter

DB_PATH = "database/moteur_recherche.db"

class StatisticsService:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def documents_par_categorie(self):
        self.cursor.execute("""
            SELECT categorie, COUNT(*) 
            FROM documents 
            GROUP BY categorie
        """)
        return self.cursor.fetchall()

    def mots_cles_frequents(self, limite=10):
        self.cursor.execute("""
            SELECT k.mot, SUM(i.frequence) AS total
            FROM keywords k
            JOIN indexation i ON k.id = i.keyword_id
            WHERE LENGTH(k.mot) > 3
            GROUP BY k.mot
            ORDER BY total DESC
            LIMIT ?
            """, (limite,))
        return self.cursor.fetchall()


    def documents_plus_pertinents(self, limite=5):
        self.cursor.execute("""
            SELECT d.titre, SUM(i.frequence) as score
            FROM documents d
            JOIN indexation i ON d.id = i.document_id
            GROUP BY d.id
            ORDER BY score DESC
            LIMIT ?
        """, (limite,))
        return self.cursor.fetchall()


    

    def close(self):
        self.conn.close()
