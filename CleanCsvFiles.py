import pandas as pd
import numpy as np

import re

class Cleaning:
    def import_from_csv(self):
        """Read csv file and return a DataFrame"""

        df = pd.read_csv('database.csv', index_col=False)
        df = df.astype(object)
        return df

    def check_space(self, df):
        """Clean space before and after string"""

        df['locality'] = df['locality'].str.lstrip()
        df['home_type'] = df['home_type'].str.lstrip()
        df['subtype'] = df['subtype'].str.lstrip()
        df['type_of_sale'] = df['type_of_sale'].str.lstrip()
        df['state_of_building'] = df['state_of_building'].str.lstrip()

        return df

    def delete_duplicate(self, df):
        """Delete all duplicated row"""
        df = df.drop_duplicates()
        print(df.shape)
        return df
    
    def remplace_NaN_value(self, df):
        """Replace all NaN value by: if string -> Not Mentioned, 
        if int or bool -> by 0"""

        df['price'] = df['price'].replace(['Nousconsulter'],np.nan)
        df["surface_of_land_area"] = df["surface_of_land_area"].str.rstrip('ares')
        df["garden_area"] = df["garden_area"].str.rstrip('ares')
        df['locality'] = df['locality'].fillna("Not Mentioned")
        df['home_type'] = df['home_type'].fillna("Not Mentioned")
        df['subtype'] = df['subtype'].fillna("Not Mentioned")
        df['price'] = df['price'].fillna(-1)
        df['type_of_sale'] = df['type_of_sale'].fillna("Not Mentioned")
        #These two lines has been updated on Saturday
        df['state_of_building'] = df['state_of_building'].replace(['AS_NEW'],['Bien neuf'])
        df['state_of_building'] = df['state_of_building'].replace(['GOOD'],['Bon'])
        df=df.fillna(0)

        df['surface_of_land_area'] = df['surface_of_land_area'].astype(float)
        df['price'] = df['price'].astype(float)
        df['garden_area'] = df['garden_area'].astype(float)
        df['equipped'] = df['equipped'].astype(float)
        df['room'] = df['room'].astype(float)
        df['area'] = df['area'].astype(float)
        df['furnished'] = df['furnished'].astype(float)
        df['open_fire'] = df['open_fire'].astype(float)
        df['terrace'] = df['terrace'].astype(float)
        df['terrace_area'] = df['terrace_area'].astype(float)
        df['facades'] = df['facades'].astype(float)
        df['swimming_pool'] = df['swimming_pool'].astype(float)
        df[df["room"] > 7] = df[df["room"] == df["room"].mean()]

        df = df.reset_index(drop= True)

        df.loc[0:4502,'surface_of_land_area'] = df.loc[0:4502,'surface_of_land_area']*100
        df.loc[0:4502,'garden_area'] = df.loc[0:4502,'garden_area']*100
        return df
    def change_HOUSE_to_Maison(self, df):
        """We see that our csv file has 2 differents name for the same thing (House and Maison),
            so we decide to change House to Maison"""

        df['home_type'] = df['home_type'].replace(['HOUSE'], ['Maison'])

        return df
    def clean_errors(self, df):
        """Delete value 5152, whitch is not correct, and check if it has 18 columns"""

        df = df.drop([5152])
        print(df.iloc[5150:5160])
        if df.shape[1] == 18:
            print('csv file has correct dimension')
        return df