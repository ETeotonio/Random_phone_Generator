import phone_number_generator
import flask

app = flask.Flask(__name__)
app.config ['DEBUG']=True

@app.route('/api/getphone',methods=['GET'])
def api_getphone():
    parameters = flask.request.args
    country  = str(parameters.get('country')).replace("\"","")
    phone_type = str(parameters.get('type')).replace("\"","")

    generate_new_phone = phone_number_generator.phone_number_generator()
    phone_number = '{'+generate_new_phone.generate_phone(country,phone_type)+'}'

    return phone_number


app.run()
