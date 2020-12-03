from CleanCsvFiles import Cleaning

import seaborn as sns
import matplotlib.pyplot as plt

class AnalyseData:
    def how_many_row_and_columns(self, df):
        """Print how many row and columns we have"""

        print(df.shape)
    
    def describe_of_values(self, df):
        """Look at variable in target"""

        print(df.describe())

class Plot:   
    def plot_price_room(self, df):
        """To create a plot with axe x number of room and y price"""

        scatter = sns.lmplot(x= 'room', y= 'price', data= df, hue= 'home_type',col= 'home_type', fit_reg=False)
        scatter.set(title='Correlation between prices and rooms')

    def plot_price_area(self, df):
        
        scatter = sns.lmplot(x= 'surface_of_land_area', y= 'price', data= df, hue= 'garden', fit_reg=False)
        scatter.set(title='Correlation between prices and area')
    
    def plot_home_type_by_quantity(self, df):

        #scatter = sns.lmplot(x= 'surface_of_land_area', y= 'price', data= df, hue= 'home_type',col= 'home_type', fit_reg=False)
        #scatter.set(title='Correlation between prices and area')
        df['quantity'] = 1
        test = df.groupby('home_type')['quantity'].sum()
        test.plot(kind="bar")
        #g = sns.FacetGrid(df, col="home_type", hue= 'home_type')
        #g.map(plt.scatter, "surface_of_land_area", 'price')
        #g.add_legend()

        plt.show()

    def plot_locality_price(self, df): 

        df = df[(df['home_type'] == 'Appartement')]
        df = df[df['price'] > 1]
        df = df[(df['surface_of_land_area'] > 0) & (df['surface_of_land_area'] < 15000)]
        scatter = sns.factorplot(x= 'price', y= 'surface_of_land_area', data= df, fit_reg=False, log=True)
        #scatter.set_yscale('log')
        scatter.set(title='Correlation between prices and rooms')
        plt.show()
        

df = Cleaning().import_from_csv()
df = Cleaning().check_space(df)
df = Cleaning().delete_duplicate(df)
df = Cleaning().remplace_NaN_value(df)
#df = Cleaning().clean_errors(df)

AnalyseData().how_many_row_and_columns(df)
AnalyseData().describe_of_values(df)
#Plot().plot_home_type_by_quantity(df)
#Plot().plot_price_room(df)
#Plot().plot_price_area(df)
Plot().plot_locality_price(df)
#plt.ylim(0, None)
#plt.xlim(0, None)