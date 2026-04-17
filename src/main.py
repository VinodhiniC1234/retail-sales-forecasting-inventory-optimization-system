import pandas as pd
import os

# Get project root automatically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data():
    file_path = os.path.join(BASE_DIR, "data", "retail_sales.csv")
    
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df

def clean_data(df):
    df = df.dropna()
    df = df.sort_values("Date")
    df = df.reset_index(drop=True)
    
    return df