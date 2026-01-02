from statistics import StatisticsService

stats = StatisticsService()

print("\n📊 TABLEAU DE BORD ADMINISTRATEUR\n")

print("📁 Documents par catégorie :")
for cat, nb in stats.documents_par_categorie():
    print(f"- {cat} : {nb}")

print("\n🔑 Mots-clés les plus fréquents :")
for mot, nb in stats.mots_cles_frequents():
    print(f"- {mot} ({nb})")

print("\n🔥 Documents les plus pertinents :")
for doc, score in stats.documents_plus_pertinents():
    print(f"- {doc} (score {score})")


stats.close()
