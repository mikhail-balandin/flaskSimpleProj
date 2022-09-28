#mkdir app\templates
#nano templates/index.html
from flask import Flask
from flask import render_template

menu = ['Установка', 'Первое приложение', 'Обратная связь']

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", maintitle='Главная', title="Привет!")

@app.route("/about")
def about():
    return render_template("about.html", maintitle='О сайте', title="О сайте", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
