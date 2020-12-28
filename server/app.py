from flask import Flask,jsonify,request,render_template
import server.utils as utils
app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response=jsonify({
        'locations':utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    location=request.form['location']
    sqft=float(request.form['total_sqft'])
    area_type=int(request.form['area_type'])
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({
    'estimated_price':utils.get_estimated_price(location,area_type,sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__=='__main__':
    app.run(debug=True)
