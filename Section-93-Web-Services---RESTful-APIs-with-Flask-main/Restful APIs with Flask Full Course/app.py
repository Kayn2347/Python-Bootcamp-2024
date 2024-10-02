from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, Float, String
from flask_sqlachemy import SQLAchemy
from flask_marsmallow import marshmallow


app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAchemy(app)
ma = Marshmallow(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/simple')
def simple():
    return jsonify(text='Hello Simple, World!',
                   message='You have run the API successfully'), 200
                   


@app.route('/not_found')
def not_found():
    return jsonify(error='This route was not found'), 404
    app.run()

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age > 21:
         return jsonify(message=f"Sorry {name}!!!")
    else:
        return jsonify(message=f"Sorry {name}, you are not old enough to access this API")
  

@app.route('/api_variables/<string:name>/int:age>')
def api_variables(name:str, age:int):
  if age > 21:
     return jsonify(message=f"Sorry {name}!!!")
  else:
    return jsonify(message=f"Sorry {name}, you are not old enough to access this API")
  

@app.route('/countries', methods= ['GET'])
def countries():
    country_list = Country.query.all()
    result = countries_schema.dump(countries_list)
    return jsonify(result)
  

@app.route('/country_details/<int:id>', methods=["GET"])
def country_details(country_id: int):
    country = Country.query.filter_by(country_id=country_id).first()
    if country:
        result = country_schema.dump(country)
        return jsonify(result)
    return jsonify("That country does not exist!"),404


@app.route('/add_country', methods=["POST"])
def add_country():
    country_name = request.form['country_name']
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country by that name exist in DB"),409
    capital = request.form['capital']
    area = request.form['area']
    new_country = Country(country_name=country_name,capital=capital,area=area)
    db.session.add(new_country)
    db.session.commit()
    return jsonify(message='You add a new country'), 201


@app.route('/add_country1', methods=["POST"])
def add_country1():
    data = request.get_json()
    if not data:
         return jsonify("Invalid or missing JSON data"), 400
    country_name = data.get('country_name')
  check_country = Country.query.filter_by(country_name=country_name).first()
  if check_country:
      return jsonify("The country by that name exist in DB"),409
  capital = data.get('capital')
  area = data.get('area')
new_country = Country(country_name=country_name,capital=capital,area=area)
db.session.add(new_country)
db.session.commit()
return jsonify(message='You add a new country'), 201
  



#Database
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Country(db.Model):
__tablename__ = 'countries'
country_id = Column(Integer, primary_key=True)
country_name = Column(String)
capital = Column(String)
area = Column(Float)


class UserSchema(ma.Schema)
   class Meta:
       fields = ('id', 'first_name', 'last_name', 'email', 'password')


class CountrySchema(ma.Schema)
 class Meta:
     fields = ('country_id', 'country_name', 'capital', 'area',)

user_schema = UserSchema()
user_schema = UserSchema(many=True)
country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created!")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped!")

@app.cli.command('db_seed')
def db_seed():
    usa = Country(country_name='USA',
                  capital='Washington',
                  area=3796742)
    germany = Country(country_name='Germany',
      capital='Berlin',
      area=138067)
    db.session.add(usa)
    db.session.add(germany)
    test_user = User(first_name='Kayn',
                     last_name='Lourence',
                     email='test@test.com',
                     password='123456')
    db.session.add(test_user)
    db.session.commit()
    print("Database seeded")

if __name__ == '__main__':
    app.run()
