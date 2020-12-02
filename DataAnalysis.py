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

        scatter = sns.lmplot(x= 'room', y= 'price', data= df, hue= 'home_type', fit_reg=False)
        scatter.set(title='Correlation between prices and rooms')

    def plot_price_area(self, df):
        
        scatter = sns.lmplot(x= 'surface_of_land_area', y= 'price', data= df, hue= 'garden', fit_reg=False)
        scatter.set(title='Correlation between prices and area')
    
    def plot_home_type_price(self, df):

        scatter = sns.lmplot(x= 'surface_of_land_area', y= 'price', data= df, hue= 'home_type', fit_reg=False)
        scatter.set(title='Correlation between prices and area')

    def plot_locality_price(self, df): 'A changer car 10000 valeurs'
        pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
        sns.swarmplot(x='locality', y='price', data=df, palette=pkmn_type_colors)

df = Cleaning().import_from_csv()
df = Cleaning().check_space(df)
df = Cleaning().delete_duplicate(df)
df = Cleaning().remplace_NaN_value(df)
#df = Cleaning().clean_errors(df)

AnalyseData().how_many_row_and_columns(df)
AnalyseData().describe_of_values(df)
#Plot().plot_home_type_price(df)
#Plot().plot_price_room(df)
#Plot().plot_price_area(df)
Plot().plot_locality_price(df)
plt.show()