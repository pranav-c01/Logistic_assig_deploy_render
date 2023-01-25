# from wsgiref import simple_server
from flask import Flask, request, app
from flask import Response
from flask_cors import CORS
from logistic_deploy import predObj

# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle


application = Flask(__name__)
# CORS(application)
# application.config['DEBUG'] = True

@application.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


# class ClientApi:~

#     def __init__(self):
#         self.predObj = predObj()

@application.route("/predict_api", methods=['POST'])
def predictRoute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is:     ', data)
            pred=predObj()
            res = pred.predict_log(data)

            #result = clntApp.predObj.predict_log(data)
            print('result is        ',res)
            return Response(res)
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)

@application.route("/predict", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            rate_marriage=float(request.form['rate_marriage'])
            age = float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            educ = float(request.form['educ'])
            occupation = float(request.form['occupation'])
            occupation_husb = float(request.form['occupation_husb'])
            predict_dict ={"rate_marriage": rate_marriage,
                "age": age,
                "yrs_married" : yrs_married,
                "children": children,
                "religious": religious,
                "educ":educ,
                "occupation":occupation,
                "occupation_husb":occupation_husb
    }
            pred2=predObj()
            res = pred2.predict_log(predict_dict)
            print('result is        ',res)
            # showing the diagnosed results in a UI
            return render_template('results.html',prediction=res)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    # clntApp = ClientApi()
    # host = '0.0.0.0'
    # port = 5000
    application.run(debug=True)
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()