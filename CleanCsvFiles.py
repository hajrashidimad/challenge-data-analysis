import pandas as pd
import numpy as np

import re

class CleaningEbu:
    def import_from_csv(self):
        """Read csv file and return a DataFrame"""

        properties = pd.read_csv('/Users/ebu/Desktop/becode_projects/Thomas/challenge-data-analysis/challenge-data-analysis/database.csv')
        properties = properties.astype(object)
        return properties

    def check_space(self, properties):
        """Clean space before and after string"""

        properties['locality'] = properties['locality'].str.lstrip()
        properties['home_type'] = properties['home_type'].str.lstrip()
        properties['subtype'] = properties['subtype'].str.lstrip()
        properties['type_of_sale'] = properties['type_of_sale'].str.lstrip()
        properties['state_of_building'] = properties['state_of_building'].str.lstrip()

        return properties

    def delete_duplicate(self, df):
        """Delete all duplicated row"""
        df = df.drop_duplicates()
        return df
    
    def remplace_NaN_value(self, df):
        """Replace all NaN value by: if string -> Not Mentioned, 
        if int or bool -> by 0"""

        df["surface_of_land_area"] = df["surface_of_land_area"].str.rstrip('ares')
        df["garden_area"] = df["garden_area"].str.rstrip('ares')
        df['locality'] = df['locality'].fillna("Not Mentioned")
        df['home_type'] = df['home_type'].fillna("Not Mentioned")
        df['subtype'] = df['subtype'].fillna("Not Mentioned")
        df['price'] = df['price'].fillna(-1)
        df['type_of_sale'] = df['type_of_sale'].fillna("Not Mentioned")
        df=df.fillna(0)
        return df
    
    def clean_errors(self, df):
        """Delete value 5152, whitch is not correct, and check if it has 18 columns"""

        df = df.drop([5152])
        print(df.iloc[5150:5160])
        if df.shape[1] == 18:
            print('csv file has correct dimension')
        return df