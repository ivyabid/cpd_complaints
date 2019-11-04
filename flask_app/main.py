from flask import Flask, request, render_template
from make_prediction import cpdp_predict

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_complaint page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_complaint/', methods=['GET', 'POST'])
def render_message():

    # user-entered features
    features= ['abuse_ct','civil_ct', 'num_awards', 'num_complaints','numwitnesses',
                    'operations_ct', 'copa_style','search','officer_age','time_on_force',
                    'officer_filed']

    # error messages to ensure correct units of measure
    messages = ["The number of abuse violations should be an integer",
                "The number of civil rights violations should be an integer",
                "The number of awards the officer has received should be an integer.",
                "The total number of complaints the officer has received should be an integer.",
                "The number of witnesses should be an integer",
                "The number of operations violations by the officer should be an integer",                
                "Would this complaint be reviewed by COPA today? (1 yes, 0 no)",
                "Is this complaint about an illegal search? (1 yes, 0 no)",
                "The age of the officer should be an integer in years",
                "The time the officer has spent on the force should be an integer in years",
                "Is this complaint made or corroborated by a police officer? (1 yes, 0 no)"]

    # hold all amounts as floats
    amounts = []

    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(features):
        user_input = request.form[ing]
        try:
            float_feature = float(user_input)
        except:
            return render_template('index.html', message=messages[i])
        amounts.append(float_feature)

    # show user final message
    final_message = cpdp_predict(amounts)
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)