import pandas as pd
class EVData:
    def __init__(self):
        # reading the csv file using read_csv, storing the data frame in variable called df
        df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
        # convert the dataframe into a dictionary and store it into a variable called data
        self.data = df.to_dict(orient='records')

    def max_electric_range(self):


ed = EVData()
print(ed.data[0])



