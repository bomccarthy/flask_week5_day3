from flask import render_template, request, redirect, url_for
from app import app

from .forms import PokemonInputForm
from app.models import User
from .pokeFunc import getPokemon

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose', methods=["GET", "POST"])
def choose():
    form = PokemonInputForm()
    if request.method == "POST":
        if form.validate():
            pokemon = form.pokemon.data
            pokemon_dict = getPokemon(pokemon)
            if isinstance(pokemon_dict, str):
                pass
            else:
                return render_template('pokecard.html', pokemon_dict=pokemon_dict)
    try:
        return render_template('choose.html', form=form, pokemon_dict=pokemon_dict)
    except:
        return render_template('choose.html', form=form)

@app.route('/pokecard')
def pokecard():
    return render_template('pokecard.html')

@app.route('/future')
def future():
    return render_template('future.html')

