import pandas as pd
class EVData:
    def __init__(self):
        # reading the csv file using read_csv, storing the data frame in variable called df
        self.df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
        # convert the dataframe into a dictionary and store it into a variable called data
        self.data = self.df.to_dict(orient='records')
        # A dictionary for keeping track of electric ranges and their frequencies
        self.ranges = {}
        for item in self.data:
            if item['Electric Range'] in self.ranges:
                self.ranges[item['Electric Range']] += 1
            else:
                self.ranges[item['Electric Range']] = 1

    #Return the highest electric range
    def max_electric_range(self):
        return max(list(self.ranges.keys()))

    #Return the lowest electric range
    def min_electric_range(self):
        return min(list(self.ranges.keys()))

    #Return the average electric range
    def avg_electric_range(self):
        return self.df['Electric Range'].mean()

    #Return the median electric range
    def median_electric_range(self):
        return self.df['Electric Range'].median()

    #Return the mode electric range
    def mode_electric_range(self):
        return max(self.ranges, key=self.ranges.get)


ed = EVData()
print(ed.min_electric_range())



