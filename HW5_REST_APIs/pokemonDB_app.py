from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.sqlite3'
db = SQLAlchemy(app)

class PokemonModel(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    number = db.Column(db.String(4))
    name = db.Column(db.String(100))
    type = db.Column(db.String(20))
    region = db.Column(db.String(20))

    @property
    def serialize(self):
        
        return {
            'id': self.id,
            'number': self.number,
            'name': self.name,
            'type': self.type,
            'region': self.region
        }

    def __repr__(self):
        return "Pokemon: %r / %r / %r / %r \n" % (self.number, self.name, self.type, self.region)

    def __init__(self, number, name, type, region):
        self.number = number
        self.name = name
        self.type = type
        self.region = region

@app.route("/all")
def show_all():
    return render_template('show_all.html', mons = PokemonModel.query.all())

@app.route("/<int:id>")
def pokemon_details(id):
    
    pokemon = db.get_or_404(PokemonModel, id)   
    return render_template("detail.html", pokemon = pokemon) 

@app.route('/api/pokemondb')
def api_pokemondb():
  # return db query results as a JSON list
    return jsonify([pokemon.serialize for pokemon in PokemonModel.query.all()])

@app.post('/api/pokemonadd')
def api_pokemon_add():

    dataMap = request.get_json()

    #check if the entry already exists. don't let duplicates into the db
    num = dataMap['number']
    exists = PokemonModel.query.filter_by(number=num).first()

    if not exists:
        try:
            student = PokemonModel(
                number = dataMap['number'], 
                name = dataMap['name'],
                type = dataMap['type'],
                region = dataMap['region'])
            
            db.session.add(student)
            db.session.commit()

            return jsonify({"status": "success"})
        
        except Exception:
            return app.response_class(response={"status": "failure"},
                                    status=500,
                                    mimetype='application/json')
    else: # display an error if the entry already exists

        return app.response_class(response = {"status : Conflict"},
                                    status=409,
                                    mimetype='application/json' )
    

def makeDB():

    db.create_all()
    
    db.session.add(PokemonModel(number='0001', name='Bulbasaur', type='Grass, Poison', region='Kanto'))
    db.session.add(PokemonModel(number='0004', name='Charmander', type='Fire', region='Kanto'))
    db.session.add(PokemonModel(number='0007', name='Squirtle', type='Water', region='Kanto'))
    db.session.add(PokemonModel(number='0025', name='Pikachu', type='Electric', region='Kanto'))
    db.session.add(PokemonModel(number='0143', name='Snorlax', type='Normal', region='Kanto'))
    db.session.add(PokemonModel(number='0155', name='Cyndaquil', type='Fire', region='Johto'))
    db.session.add(PokemonModel(number='0158', name='Totodile', type='Water', region='Johto'))
    db.session.add(PokemonModel(number='0255', name='Torchic', type='Fire', region='Hoenn'))
    db.session.add(PokemonModel(number='0258', name='Mudkip', type='Water', region='Hoenn'))
    db.session.add(PokemonModel(number='0384', name='Rayquaza', type='Dragon, Flying', region='Hoenn'))
    db.session.add(PokemonModel(number='0387', name='Turtwig', type='Grass', region='Sinnoh'))
    db.session.add(PokemonModel(number='0390', name='Chimchar', type='Fire', region='Sinnoh'))
    db.session.add(PokemonModel(number='0487', name='Giratina', type='Ghost, Dragon', region='Sinnoh'))
    db.session.add(PokemonModel(number='0495', name='Snivy', type='Grass', region='Unova'))
    db.session.add(PokemonModel(number='0498', name='Tepig', type='Fire', region='Unova'))
    db.session.add(PokemonModel(number='0501', name='Oshawott', type='Water', region='Unova'))
    db.session.add(PokemonModel(number='0650', name='Chespin', type='Grass', region='Kalos'))
    db.session.add(PokemonModel(number='0653', name='Fennekin', type='Fire', region='Kalos'))
    db.session.add(PokemonModel(number='0656', name='Froakie', type='Water', region='Kalos'))
    db.session.add(PokemonModel(number='0722', name='Rowlet', type='Grass, Flying', region='Alola'))
    db.session.add(PokemonModel(number='0725', name='Litten', type='Fire', region='Alola'))
    db.session.add(PokemonModel(number='0728', name='Popplio', type='Water', region='Alola'))
    db.session.add(PokemonModel(number='0789', name='Cosmog', type='Psychic', region='Alola'))
    db.session.add(PokemonModel(number='0810', name='Grookey', type='Grass', region='Galar'))
    db.session.add(PokemonModel(number='0813', name='Scorbunny', type='Fire', region='Galar'))
    db.session.add(PokemonModel(number='0816', name='Sobble', type='Water', region='Galar'))
    
    db.session.commit()

if __name__ == '__main__':
    
    app.run(debug = True)
    makeDB()