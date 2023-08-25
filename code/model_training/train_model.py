import pickle
import pandas as pd
from prophet import Prophet

def train_model(data):
    df = pd.read_csv(data)
    df.rename(columns={'date_column': 'ds', 'target_column': 'y'}, inplace=True)
    
    model = Prophet()
    model.fit(df)
    
    return model

if __name__ == '__main__':
    data_path = 'data.csv'  
    
    trained_model = train_model(data_path)
    with open('models/trained_prophet_model.pkl', 'wb') as f:
        pickle.dump(trained_model, f)