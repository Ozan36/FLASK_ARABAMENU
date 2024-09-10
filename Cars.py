# flask, hata yazma ve json sınıfı oluşturur 
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request,render_template
# JSON formatında menü oluşturur
Cars = [  
    {'id': 36, 'marka': 'BMW', 'model': 2018, 'renk': 'LACİVERT', 'kilometresi': 50000},
    {'id': 44, 'marka': 'AUDI', 'model': 2020, 'renk': 'BEYAZ', 'kilometresi': 60000},
    {'id': 34, 'marka': 'MERCEDES', 'model': 2022, 'renk': 'GRİ', 'kilometresi': 40000},
    {'id': 76, 'marka': 'PORSCHE', 'model': 2018, 'renk': 'KIRMIZI', 'kilometresi': 70000},
    {'id': 75, 'marka': 'RENAULT', 'model': 2021, 'renk': 'MAVİ', 'kilometresi': 80000},
    {'id': 6, 'marka': 'FIAT', 'model': 2012, 'renk': 'SİYAH', 'kilometresi': 100000},
    {'id': 1, 'marka': 'VOLVO', 'model': 2015, 'renk': 'SARI', 'kilometresi': 90000},
    ]
#flask adlandırılır
app = Flask(__name__)
# Get metodu ile tüm araba listesi yazdırılır
@app.route('/', methods=['GET'])
def araba():
    return jsonify({'Cars': Cars})

# Araba Id sine göre yazdırılır
@app.route('/ozan/api/Cars/<int:Cars_id>', methods=['GET'])
def secilenAraba(Cars_id):
    #ID karşılaştırması yapar ve girilen değeri alır
    selected_car = [car for car in Cars if car['id'] == Cars_id] 
    
    if not selected_car:
        return jsonify({'Cars': 'Girilen Ide ye Göre Araba bulunamadı'}), 404
    return jsonify({'Cars': selected_car})

#Manuel olarak hata yazdırır
def bulunmadi(error):
    return make_response(jsonify({'HTTP 404 Hata': 'The content you looks for does not exist. Please check your request.'}), 404)
if __name__ == '__main__':
    app.run(debug=True)