import pickle
import pandas as pd
import numpy as np

# read in the model
my_model = pickle.load(open("modelrfc.p","rb"))

# create a function to take in user-entered amounts and apply the model
def cpdp_predict(amounts_float, model=my_model):
    if amounts_float[10]==1:
        off_false = 0
        off_true=1

    if amounts_float[10]==0:
        off_false = 1
        off_true=0

    # inputs into the model
    input_df = [[amounts_float[0],amounts_float[1],amounts_float[2],amounts_float[3],
                    amounts_float[4],amounts_float[5],amounts_float[6],
                    amounts_float[7],1,amounts_float[8],amounts_float[9],
                    off_false,off_true,0]]

    # make a prediction
    prediction = my_model.predict(input_df)[0]

    # return a message
    message_array = ["It probably won't result in discipline",
    'It might result in discipline!']

    return message_array[prediction]
