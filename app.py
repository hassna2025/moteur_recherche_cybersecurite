from flask import Flask, render_template, request, send_file, abort
from search.search_engine import rechercher
import os

app = Flask(__name__)
CORPUS_PATH = "corpus"

@app.route("/", methods=["GET", "POST"])
def index():
    resultats = []
    requete = ""
    if request.method == "POST":
        requete = request.form.get("requete", "")
        if requete:
            resultats = rechercher(requete)
    return render_template("index.html", resultats=resultats, requete=requete)

@app.route("/fichier")
def ouvrir_fichier():
    chemin = request.args.get("chemin")
    if chemin and os.path.isfile(chemin):
        return send_file(chemin, as_attachment=False)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
