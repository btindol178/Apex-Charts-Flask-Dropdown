# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, render_template,request
import pandas as pd

app = Flask(__name__)

df_scatter = pd.DataFrame({
      'values':  [10, 41, 35, 51, 49, 62, 69, 91, 148],
      'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
   })
@app.route('/')
@app.route('/apexdropdown',methods=['GET','POST'])
def apextutorialdropdown():
    # Bring in csv... print it.. pd.read_csv for example 
    print(type(df_scatter['values'])) # series 
    print(df_scatter.dtypes)
    #############################################
    # Change columns to list.. 
    #values = [10, 41, 35, 51, 49, 62, 69, 91, 148]
    #months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    values = df_scatter['values'].to_list()
    months = df_scatter['months'].to_list()

    #print(values2)
    dataObject = {
        "values":values,
        "months":months
    }
    if request.method == 'POST':
        
        var1 = int(request.form['id']) # Need to make the column same type as eachother int is values column in df
        print(type(var1))
        print(var1)

        df2 = df_scatter[df_scatter['values'] != var1]#.astype(str) # was used to make the int column string to match types
        print(df_scatter)
        print(df2)
        
        values = df2['values'].to_list()
        months = df2['months'].to_list()
        dataObject = {
        "values":values,
        "months":months}

        return render_template('home/apex-chart-tutorial2.html',dataObject=dataObject)
    return render_template('home/apex-chart-tutorial2.html',dataObject=dataObject)
if __name__=="__main__":
    app.run(debug=True)
