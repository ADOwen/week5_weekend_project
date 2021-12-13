from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from flask_login import current_user, login_required


from .forms import CreateCharacterForm
from app.models import MarvelCharacter

char = Blueprint('char',__name__,template_folder='char_templates')

from app.models import db

@char.route('/characters')
@login_required
def charHome():
    characters = MarvelCharacter.query.all()
    return render_template('characters.html' , characters = characters)
    

@char.route('/characters/create', methods=["GET","POST"])
@login_required
def createChar():
    form = CreateCharacterForm()
    if request.method == "POST":
            if form.validate():
                
                name = form.name.data
                description = form.description.data
                comics_appeared_in = form.comics_appeared_in.data
                super_power = form.super_power.data

                # create instance of character
                character = MarvelCharacter(name, description, comics_appeared_in, super_power, current_user.id)
                # add instance to database 
                db.session.add(character)
                # commit to database like github
                db.session.commit()
            
                return redirect(url_for('char.charHome'))

    return render_template('createchar.html', form=form)

@char.route('/api/characters')
def allProductsAPI():
    characters = MarvelCharacter.query.all()
    return jsonify([c.to_dict() for c in characters])
        


