import sqlite3

conn = sqlite3.connect("database/moteur_recherche.db")
cursor = conn.cursor()

with open("database/schema.sql", "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()

print("Base de données créée avec succès")
