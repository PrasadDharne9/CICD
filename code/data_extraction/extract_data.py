import psycopg2
import pandas as pd

def fetch_data_from_database():
    conn = psycopg2.connect(
        dbname='S&P_experiment',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )

    query = 'SELECT * FROM raqa_data;'
    
    data = pd.read_sql(query, conn)
    
    conn.close()
    
    return data

if __name__ == '__main__':
    fetched_data = fetch_data_from_database()
    fetched_data.to_csv('data.csv', index=False)