from flask import Flask, redirect, url_for, request,render_template
import pandas as pd
import json
app = Flask(__name__)
@app.route('/GetDataPandaCSV',methods = ['GET'])
def GetCSVDataPandas():
       data = request.args.get('data')
       print(data)
       lst = []
       test = pd.read_csv('word_search (3).csv')
       res = test[test['name'].str.match(data,na=False)]
       for index, row in res.iterrows():
           d = {}
           d[data] = row['frequency']
           lst.append(d)
       return json.dumps(lst)
if __name__ == '__main__':
   app.run("127.0.0.1","5005",True)