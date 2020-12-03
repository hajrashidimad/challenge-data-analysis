from CleanCsvFiles import Cleaning
from matplotlib.colors import LogNorm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class AnalyseData:
    def how_many_row_and_columns(self, df):
        """Print how many row and columns we have"""

        print(df.shape)
    
    def describe_of_values(self, df):
        """Look at variable in target"""

        print(df.describe())

class Plot: 
    
    def plot_home_type_by_quantity(self, df):

        df['quantity'] = 1
        test = df.groupby('home_type')['quantity'].sum()
        test.sort_values()
        print(test)
        test.plot(kind="bar")

        plt.show()

    def plot_surface_of_type_price(self, df): 

        df = df[(df['home_type'] == 'Appartement')]
        df = df[df['price'] > 1]
        df = df[(df['surface_of_land_area'] > 0)]
        scatter = sns.lmplot(x= 'price', y= 'surface_of_land_area', data= df, fit_reg=False)
        scatter.set(title='Correlation between prices and surface of appartement')
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('Price of properties')
        # plt.ylabel('Surface of properties')
        plt.show()
    def plot_price_room(self,df):
        df = df[(df["price"] > 1) & (df["room"] > 1)]
        cor = df.corr()
        ax = sns.heatmap(cor, center=0)
        plt.show()

df = Cleaning().import_from_csv()
df = Cleaning().check_space(df)
df = Cleaning().delete_duplicate(df)
df = Cleaning().remplace_NaN_value(df)
#df = Cleaning().clean_errors(df)

AnalyseData().how_many_row_and_columns(df)
AnalyseData().describe_of_values(df)
# Plot().plot_home_type_by_quantity(df)
# Plot().plot_surface_of_type_price(df)
Plot().plot_price_room(df)
plt.show()