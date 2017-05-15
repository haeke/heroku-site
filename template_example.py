from flask import Flask, render_template
app = Flask(__name__)

name = "Fester"

@app.route('/')
def index():
    movies = [{ 'movie': 'IV A New Hope'}, {'movie': 'V The Empire Strikes Back'}, {'movie': 'VI Return of the Jedi'}, {'movie': 'I The Phantom Menace'}, {'movie': 'II  Attack of the Clones'},{'movie': 'III Revenge of the Sith'}]
    return render_template('index.html', name=name, movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
