import pickle
import pandas as pd
from prophet import Prophet

def deploy_forecasts(model):
    # Your code to deploy forecasts goes here
    forecast_period = 25
    
    # Create a dataframe with future dates
    future = model.make_future_dataframe(periods=forecast_period, freq='M')
    
    # Make forecasts
    forecast = model.predict(future)
    
    # Store or visualize the forecasts
    forecast_results = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast_results.to_csv('forecasts/forecast_results.csv', index=False)

if __name__ == '__main__':
    with open('models/trained_prophet_model.pkl', 'rb') as f:
        trained_model = pickle.load(f)
    
    deploy_forecasts(trained_model)
