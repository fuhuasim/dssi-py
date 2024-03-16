from joblib import dump, load
import pandas as pd
import numpy as np
from .data_processor import log_txf, remap_emp_length

def get_prediction(**kwargs):
    # Load the trained linear regression model
    linear_reg = load('models/mdl.joblib')
    
    # Prepare input data for prediction
    input_data = pd.DataFrame(kwargs, index=[0])[['YearsExperience']]
    
    # Make prediction
    prediction = linear_reg.predict(input_data)
    
    return prediction[0]