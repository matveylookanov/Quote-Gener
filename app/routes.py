from flask import Blueprint, render_template
from faker import Faker
from app.models import Quote
from app import db

main = Blueprint("main", __name__)
faker = Faker()

@main.route("/")
def home():
    # Генерация новой случайной цитаты при каждом обновлении страницы
    quote = Quote(
        text=faker.sentence(nb_words=10),
        author=faker.name(),
        category=faker.word(ext_word_list=['motivation', 'life', 'success', 'wisdom', 'humor'])
    )
    db.session.add(quote)
    db.session.commit()

    quotes = Quote.query.all()
    return render_template("index.html", quotes=quotes)
