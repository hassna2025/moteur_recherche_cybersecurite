from search.search_engine import rechercher

if __name__ == "__main__":
    print("🔎 Moteur de recherche – CyberSécurité")
    requete = input("Entrez votre requête : ")

    resultats = rechercher(requete)

    if not resultats:
        print("❌ Aucun résultat trouvé")
    else:
        print("\n✅ Résultats :\n")
        for r in resultats:
            print(f"- {r['titre']} | score : {r['score']}")
