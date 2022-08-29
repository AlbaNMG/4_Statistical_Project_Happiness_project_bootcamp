from flask import Flask, render_template, request, redirect, url_for
import numpy as np

#see the lesson about Flask in week 12 of the bootcamp:

#instantiate a flask object-creating an empty flask app:
app = Flask(__name__)

#first door is at url "/"
@app.route('/')

# for each door you have to say which function will be executed
def main():

    return render_template('welcome.html')

#second door
@app.route('/lifeassessment', methods = ('GET','POST' ))

def life_assessment():
    #this time I want a html template as a result of my route
    #you have an amazing model and you want to display the results

    if request.method == "GET":

        return render_template('life_assessment.html')

    if request.method == "POST":

        import plotly.graph_objects as go #for the radar chart

        #preparing inputs for the graph
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        import scipy.stats as st #hypothesis testing
        from math import pi
        from sklearn import linear_model #linear regression

        #reading the dataset
        data_original=pd.read_excel('Survey.xlsx')

        #dropping the first column
        data=data_original.drop(['Marca temporal'],axis=1)
        
        #changing columns names
        data2= data.rename(columns={'Rate from 1 to 10 your quality of sleep':'Quality of sleep',
                                    'Rate from 1 to 10 your job satisfaction':'Job satisfaction',
                                    'Rate from 1 to 10 your financial situation':'Financial situation',
                                    'Rate from 1 to 10 your health':'Health',
                                    'Rate from 1 to 10 your social life':'Social life',
                                    'Rate from 1 to 10 your self-esteem':'Self-esteem',
                                    'Rate from 1 to 10 your relationship with family/ friends':'Family/ friends relationship',
                                    'Rate from 1 to 10 your average level of stress':'Stress Level',
                                    'Rate from 1 to 10 your average level of hapiness':'Happiness Level'})

        #replacing Women by "W" and Men by "M"
        data2['Gender']=data2['Gender'].replace('Woman','W').replace('Man','M')

        #defining inputs to be entered by users
        input_sleep = int(request.form['Quality of sleep_form'])
        input_job = int(request.form['Job satisfaction_form'])
        input_financial = int(request.form['Financial situation_form'])
        input_health = int(request.form['Health_form'])
        input_social = int(request.form['Social life_form'])
        input_self = int(request.form['Self-esteem_form'])
        input_family = int(request.form['Family/ friends relationship_form'])
        input_stress = int(request.form['Stress level_form'])

        #creating the radar chart. Reference: https://plotly.com/python/radar-chart/
        categories = ['Quality of sleep','Job satisfaction','Financial situation','Health','Social life', 'Self-esteem','Family/ friends relationship', 'Stress level']

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[input_sleep, input_job, input_financial, input_health, input_social,input_self,input_family,input_stress],
            theta=categories,
            fill='toself',
            name='Data User'
        ))

        fig.add_trace(go.Scatterpolar(
            r=[data2['Quality of sleep'].mean(),
                data2['Job satisfaction'].mean(),
                data2['Financial situation'].mean(),
                data2['Health'].mean(),
                data2['Social life'].mean(),
                data2['Self-esteem'].mean(),
                data2['Family/ friends relationship'].mean(),
                data2['Stress Level'].mean()],
            theta=categories,
            fill='toself',
            name='Average'
        ))

        fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 10]
            )),
        showlegend=True,title_text= 'In this chart, you can compare the ratings of the areas of your life with the average of the population: '
        )
    
        result_chart = fig.show()

        #creating the report about areas above/ below the average

        above=[]
        below=[]
        if input_sleep>=data2['Quality of sleep'].mean():
            a='Quality of sleep'
            above.append(a)
        else:
            a='Quality of sleep'
            below.append(a)

        if input_job>=data2['Job satisfaction'].mean():
            a='Job satisfaction'
            above.append(a)
        else:
            a='Job satisfaction'
            below.append(a)

        if input_financial>=data2['Financial situation'].mean():
            a='Financial situation'
            above.append(a)
        else:
            a='Financial situation'
            below.append(a)

        if input_health>=data2['Health'].mean():
            a='Health'
            above.append(a)
        else:
            a='Health'
            below.append(a)

        if input_social>=data2['Social life'].mean():
            a='Social life'
            above.append(a)
        else:
            a='Social life'
            below.append(a)

        if input_self>=data2['Self-esteem'].mean():
            a='Self-esteem'
            above.append(a)
        else:
            a='Self-esteem'
            below.append(a)
        
        if input_family>=data2['Family/ friends relationship'].mean():
            a='Family/ friends relationship'
            above.append(a)
        else:
            a='Family/ friends relationship'
            below.append(a)
        
        if input_stress>=data2['Stress Level'].mean():
            a='Stress Level'
            above.append(a)
        else:
            a='Stress Level'
            below.append(a)
        
        #cleaning the lists
        above_clean=str(above).replace('[',"").replace(']',"").replace("'","")
        below_clean=str(below).replace('[',"").replace(']',"").replace("'","")

        #to reference the result in the front end use Jinja templating syntax "{{ }}"    
        return render_template('life_assessment.html', my_result3 = result_chart, my_result4 = above_clean, my_result5 = below_clean)

@app.route('/future', methods = ('GET','POST' ))

def future_future():

    if request.method == "GET":

        return render_template('future.html')

    if request.method == "POST":

#happiness simulator

        #importing the dataset in this new function (future_future)
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        import scipy.stats as st #hypothesis testing
        from math import pi
        from sklearn import linear_model #linear regression

        #reading the dataset
        data_original=pd.read_excel('Survey.xlsx')

        #dropping the first column
        data=data_original.drop(['Marca temporal'],axis=1)
        
        #changing columns names
        data2= data.rename(columns={'Rate from 1 to 10 your quality of sleep':'Quality of sleep',
                                    'Rate from 1 to 10 your job satisfaction':'Job satisfaction',
                                    'Rate from 1 to 10 your financial situation':'Financial situation',
                                    'Rate from 1 to 10 your health':'Health',
                                    'Rate from 1 to 10 your social life':'Social life',
                                    'Rate from 1 to 10 your self-esteem':'Self-esteem',
                                    'Rate from 1 to 10 your relationship with family/ friends':'Family/ friends relationship',
                                    'Rate from 1 to 10 your average level of stress':'Stress Level',
                                    'Rate from 1 to 10 your average level of hapiness':'Happiness Level'})

        #replacing Women by "W" and Men by "M"
        data2['Gender']=data2['Gender'].replace('Woman','W').replace('Man','M')

#Multilinear regression Model

        X= data2[['Age','Quality of sleep','Job satisfaction','Financial situation','Health','Social life','Self-esteem','Family/ friends relationship','Stress Level']]
        y=data2['Happiness Level']

        model= linear_model.LinearRegression()
        result=model.fit(X,y)

        #defining inputs to be entered by users
        input_age_prediction = int(request.form['Age_prediction'])
        input_sleep_prediction = int(request.form['Quality of sleep_prediction'])
        input_job_prediction = int(request.form['Job satisfaction_prediction'])
        input_financial_prediction = int(request.form['Financial situation_prediction'])
        input_health_prediction = int(request.form['Health_prediction'])
        input_social_prediction = int(request.form['Social life_prediction'])
        input_self_prediction = int(request.form['Self-esteem_prediction'])
        input_family_prediction = int(request.form['Family/ friends relationship_prediction'])
        input_stress_prediction = int(request.form['Stress level_prediction'])

        #using the model to predict
        result2=result.predict([[input_age_prediction,
                                input_sleep_prediction,
                                input_job_prediction,
                                input_financial_prediction,
                                input_health_prediction,
                                input_social_prediction,
                                input_self_prediction,
                                input_family_prediction,
                                input_stress_prediction]])

        #rounding the prediction to 1 decimal number and cleaning
        import numpy as np
        result2_round=np.around(result2,2)
        result2_clean=str(result2_round).replace('[',"").replace(']',"")

    return render_template('future.html', my_result2=result2_clean)

# here we are running the app which contains all the logic/ routes defined
app.run(debug=True)