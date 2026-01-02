import sqlite3

DB_PATH = "database/moteur_recherche.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
