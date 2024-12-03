import pandas as pd
import requests
from sqlalchemy import create_engine
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Step 1: Data Ingestion
logging.info("Fetching EV data...")
ev_data = pd.read_csv("station_data_dataverse.csv")
external_data = requests.get("https://api.example.com/weather").json()

# Step 2: Data Transformation
logging.info("Transforming data...")
ev_data['avg_charging_speed'] = ev_data['kwhTotal'] / ev_data['chargeTimeHrs']
combined_data = pd.merge(ev_data, pd.DataFrame(external_data), on='location', how='inner')

# Step 3: Data Storage
logging.info("Storing data in database...")
engine = create_engine('sqlite:///ev_database.db')
combined_data.to_sql('ev_data', con=engine, if_exists='replace', index=False)

# Step 4: Data Visualization
logging.info("Creating visualizations...")
import matplotlib.pyplot as plt
combined_data['avg_charging_speed'].plot(kind='hist')
plt.title('Average Charging Speed Distribution')
plt.show()
