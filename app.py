from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask import jsonify
from flask_mysqldb import MySQL
import os
# import request
# import json
from modul import Module
app = Flask(__name__)

app.config['MYSQL_HOST'] = '153.92.10.74'
app.config['MYSQL_USER'] = 'rootu5030462_sipeta'
app.config['MYSQL_PASSWORD'] = '&GpQvZp!IOc7'
app.config['MYSQL_DB'] = 'u5030462_sipeta'
mysql = MySQL(app)

# init object flask restfull
api = Api(app)

# init cors
CORS(app)

# modul = Module('data/materials2.xlsx')//


@app.route('/')
def gas():
    return 'Connected!'


@app.route('/petshop', methods=['GET'])
def petshop():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM petshops')
    mysql.connection.commit()
    petshops = [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
    cursor.close()
    return jsonify(petshops)


@app.route('/petshop/<id>', methods=['GET'])
def singlePetshop(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM petshops WHERE id = %s', (id,))
    mysql.connection.commit()
    petshop = [dict(zip([column[0] for column in cursor.description], row))
               for row in cursor.fetchall()]
    cursor.close()
    return jsonify(petshop)


@app.route('/petshop', methods=['POST'])
def createPetshop():
    name = request.form['name']
    capacity = request.form['capacity']
    total_employee = request.form['total_employee']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    grooming_price = request.form['grooming_price']
    animal_care_price = request.form['animal_care_price']
    address = request.form['address']
    gmaps_link = request.form['gmaps_link']
    open_hours = request.form['open_hours']
    image_url = request.form['image_url']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO petshops (name, capacity, total_employee, latitude, longitude, grooming_price, animal_care_price, address, gmaps_link, open_hours, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                   (name, capacity, total_employee, latitude, longitude, grooming_price, animal_care_price, address, gmaps_link, open_hours, image_url))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'status': 'success'})


@app.route('/petshop/<id>', methods=['PUT'])
def updatePetshop(id):
    name = request.form['name']
    capacity = request.form['capacity']
    total_employee = request.form['total_employee']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    grooming_price = request.form['grooming_price']
    animal_care_price = request.form['animal_care_price']
    address = request.form['address']
    gmaps_link = request.form['gmaps_link']
    open_hours = request.form['open_hours']
    image_url = request.form['image_url']

    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE petshops SET name = %s, capacity = %s, total_employee = %s, latitude = %s, longitude = %s, grooming_price = %s, animal_care_price = %s, address = %s, gmaps_link = %s, open_hours = %s, image_url = %s WHERE id = %s ''',
                   (name, capacity, total_employee, latitude, longitude, grooming_price, animal_care_price, address, gmaps_link, open_hours, image_url, id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'status': 'success'})


@app.route('/petshop/<id>', methods=['DELETE'])
def deletePetshop(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM petshops WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'status': 'success'})


@app.route('/recommendation')
def main():
    res = {}
    lat = float(request.args.get('latitude'))
    longit = float(request.args.get('longitude'))
    criteria = request.args.get('criteria')
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT  id, `name`, capacity kapasitas, total_employee dokter, grooming_price harga, distance jarak, latitude lat, longitude `long` FROM petshops')
    mysql.connection.commit()
    petshops = [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
    cursor.close()

    modul = Module(petshops)

    modul.updateDistance(float(lat), float(longit))
    data = criteria.split(",")
    res = modul.getBobotKriteria(data)

    # res =  [2,1,3] to string (2,1,3)
    query = 'SELECT * FROM petshops WHERE id IN ('
    for i in range(len(res)):
        if i == len(res)-1:
            query += str(res[i])
        else:
            query += str(res[i]) + ','
    query += ')'
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    petshopRecommendation = [dict(zip([column[0] for column in cursor.description], row))
                             for row in cursor.fetchall()]
    cursor.close()
    return jsonify(petshopRecommendation)


if __name__ == "__main__":
    app.run(debug=True)
