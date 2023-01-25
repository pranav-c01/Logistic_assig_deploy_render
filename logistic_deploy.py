#Let's start with importing necessary libraries
import pickle
import numpy as np
import pandas as pd

class predObj:

    def predict_log(self, dict_pred):
        with open("standard_scaler.sav", 'rb') as f:
            scalar = pickle.load(f)

        with open("model.pkl", 'rb') as f:
            model = pickle.load(f)
        data_df = pd.DataFrame(dict_pred,index=[1,])
        scaled_data = scalar.transform(data_df)
        predict = model.predict(scaled_data)
        if predict[0] ==0 :
            result = '0'
        else:
            result = '1'

        return result



