CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT,
    chemin TEXT,
    contenu TEXT,
    type TEXT,
    categorie TEXT
);

CREATE TABLE IF NOT EXISTS keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mot TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS indexation (
    document_id INTEGER,
    keyword_id INTEGER,
    frequence INTEGER,
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (keyword_id) REFERENCES keywords(id)
);

-- Tables statistiques
CREATE TABLE IF NOT EXISTS requetes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    terme TEXT,
    date_requete DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS consultations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER,
    date_consultation DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

