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
    
    def plot_home_type_by_quantity(self, df):

        df['quantity'] = 1
        test = df.groupby(['home_type']).agg({'quantity':sum})
        res = test.apply(lambda x: x.sort_values(ascending=False).head(3))
        res.plot(kind="bar")

        plt.show()

    def plot_surface_of_type_price(self, df): 

        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'HOUSE') | (df['home_type'] == 'Maison')]
        df = df[(df['price'] > 1) & (df['price'] < 1000000)]
        df = df[(df['surface_of_land_area'] > 0)]
        scatter = sns.lmplot(x= 'price', y= 'surface_of_land_area', data= df, fit_reg=False, col='home_type',
                             hue='home_type')
        plt.xscale('log')
        plt.yscale('log')
        scatter.set_axis_labels('Prices of properties', 'Surface of properties')
        scatter.set_titles('Correlation of price by home type')
        
        plt.show()
    
    def proportions_of_home_type(self, df):

        first = (df['home_type']=='Appartement').sum()
        second = (df['home_type']=='Maison').sum()
        third = (df['home_type']=='HOUSE').sum()
        plt.pie([first, second, third],  labels=['Appartement', 'Maison', 'HOUSE'], colors=['red','blue', 'green'], 
                shadow=False, autopct='%1.1f%%', startangle=100)
        plt.axis('equal')
        plt.title('Home type proportions')
        plt.show()
    
    def home_type_price_dispertion(self, df):
        
        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'HOUSE') | (df['home_type'] == 'Maison')]
        df = df[(df['price'] > 1) & (df['price'] < 800000)]
        sns.set_style('whitegrid')
        # Violin plot
        sns.violinplot(x='home_type', y='price', data=df)
        plt.show()
    
    def home_type_surface_dispertion(self, df):

        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'HOUSE') | (df['home_type'] == 'Maison')]
        df = df[df['surface_of_land_area'] > 0]
        df = df[(df['surface_of_land_area'] > 1) & (df['surface_of_land_area'] < 2000)]
        sns.set_style('whitegrid')
        # Violin plot
        sns.violinplot(x='home_type', y='surface_of_land_area', data=df)
        plt.show()
    
    def distribution_of_surface(self, df):

        print(df['surface_of_land_area'].mean())
        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'HOUSE') | (df['home_type'] == 'Maison')]
        df = df[df['surface_of_land_area'] > 0]
        first = (df['surface_of_land_area'] > (df['surface_of_land_area'].mean())+500).sum()
        second = (df['surface_of_land_area'] < (df['surface_of_land_area'].mean())-500).sum()
        third = ((df['surface_of_land_area'] <= (df['surface_of_land_area'].mean())+500) & 
                    (df['surface_of_land_area'] <= (df['surface_of_land_area'].mean())+500)).sum()
        plt.pie([first, second, third],  labels=['Bigger then mean', 'Lesser then mean', 'Mean'], colors=['red','blue', 'green'], 
                shadow=False, autopct='%1.1f%%', startangle=100)
        plt.axis('equal')
        plt.title('Surface distribution')
        plt.show()
    
    def distribution_of_price(self, df):

        print(df['price'].mean())
        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'HOUSE') | (df['home_type'] == 'Maison')]
        df = df[df['price'] > 0]
        first = (df['price'] > (df['price'].mean())+100000).sum()
        second = (df['price'] < (df['price'].mean())-100000).sum()
        third = ((df['price'] <= (df['price'].mean())+100000) & 
                    (df['price'] <= (df['price'].mean())+100000)).sum()
        plt.pie([first, second, third],  labels=['Bigger then mean', 'Lesser then mean', 'Mean'], colors=['red','blue', 'green'], 
                shadow=False, autopct='%1.1f%%', startangle=100)
        plt.axis('equal')
        plt.title('Price distribution')
        plt.show()
        
    def state_of_building(self,df):
        type_colors = ['#78C850',  # Grass
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

        df=df[df['state_of_building'] != '0']
        sns.countplot(x='state_of_building', data=df, palette=type_colors)
        plt.xticks(rotation=-45);
        plt.show()
        
df = Cleaning().import_from_csv()
df = Cleaning().check_space(df)
df = Cleaning().delete_duplicate(df)
df = Cleaning().remplace_NaN_value(df)
#df = Cleaning().clean_errors(df)

AnalyseData().how_many_row_and_columns(df)
AnalyseData().describe_of_values(df)
#Plot().plot_home_type_by_quantity(df)
#Plot().plot_surface_of_type_price(df)
#Plot().proportions_of_home_type(df)
#Plot().home_type_price_dispertion(df)
#Plot().home_type_surface_dispertion(df)
#Plot().distribution_of_surface(df)
#Plot().distribution_of_price(df)
#Plot().state_of_building(df)