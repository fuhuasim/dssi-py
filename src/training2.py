import argparse
import pandas as pd
import numpy as np
import datetime
import logging

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from joblib import dump, load

import data_processor

logging.basicConfig(level=logging.INFO)

def run(data_path, model_path):
    logging.info('Loading Data...')
    df = pd.read_csv(data_path)
    
    X = df[['YearsExperience']]
    y = df['Salary']
    
    logging.info('Start Train-Test Split...')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    logging.info('Start Training...')
    linear_reg = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ])
    
    linear_reg.fit(X_train, y_train)
    
    logging.info('Evaluate...')
    mse = mean_squared_error(y_test, linear_reg.predict(X_test))
    logging.info('Mean Squared Error: %.2f', mse)
    
    logging.info('Saving Model...')
    dump(linear_reg, model_path+'mdl.joblib')
    
    logging.info('Training completed.')
    return None

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--data_path", type=str)
    argparser.add_argument("--model_path", type=str)
    args = argparser.parse_args()
    run(args.data_path, args.model_path)