from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pymongo

#MONGODB ATLAS URL
DB_URI = 'mongodb+srv://fyp_admin:fyp_pwd@cluster0-oov30.mongodb.net/test?retryWrites=true'


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')


@app.route("/detect/")
def detect():
    return render_template('detect.html')

@app.route("/predict/")
def predict():
    return render_template('detect.html')

@app.route("/accounts/")
def accounts():
    return render_template('accounts.html')


from rpy2.robjects import r, pandas2ri


@app.route("/search/",methods=["GET", "POST"])
def search():
    client = pymongo.MongoClient(DB_URI)
    db = client.test2
    if request.method == 'POST':
            search_value = request.form['search'];
            # search_value = request.form.get('search')
            print(search_value)
            # datainflu = connect_db.retrieve_analysedData_influenza("influenza")
            data = retrieve_analysedData(db.analysedData,search_value)
            #print(data.count())
            count = retrieve_CountData(db.analysedData,search_value)
            print(count)
            if (count==0):
                return render_template('search.html', nodata="no results found")
            else:
                return render_template('search.html', myvalue=data, disease=search_value, disease_header="DISEASE",epoch_header="EPOCH",observed_header="OBSERVED",alarm_header="ALARM")
    else:
        data = retrieve_ALLanalysedData(db.analysedData)
        totdisease,influenza,gastro,conjunc,respiratory = retrieve_ALLnumCases()
        return render_template('search.html', myvalue=data, disease_header="DISEASE",epoch_header="EPOCH",observed_header="OBSERVED",alarm_header="ALARM",totcases=totdisease,cases_influenza=influenza,cases_gastro=gastro,cases_conjunc=conjunc,cases_respi=respiratory)

def retrieve_analysedData(diseaseDB,value):
    collection = diseaseDB
    #input_analysedData = collection.find({})
    input_analysedData = collection.find({"disease": value})
    return input_analysedData

def retrieve_ALLanalysedData(diseaseDB):
    collection = diseaseDB
    #input_analysedData = collection.find({})
    input_analysedData = collection.find({})
    return input_analysedData

def retrieve_CountData(diseaseDB,value):
    collection = diseaseDB
    item_count = collection.count_documents({"disease": value})
    return item_count

def retrieve_ALLnumCases():
    client = pymongo.MongoClient(DB_URI)
    db = client.test2
    collection = db.totalData
    #input_analysedData = collection.find({})
    totDisease = collection.find({"disease": "All_diseases"})
    totinfluenza = collection.find({ "disease" : "influenza" })
    totgastro = collection.find({"disease": "gastroenteritis"})
    totconjunc = collection.find({"disease": "conjunctivitis"})
    totRespiratory = collection.find({"disease": "respiratoryinfection"})
    return totDisease,totinfluenza,totgastro,totconjunc,totRespiratory


if __name__ =='__main__':
  app.run(debug=True)



