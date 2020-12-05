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
    
    def sorted_by_city_in_wallonia(self, df):
        """We use this function to take only wallonia's city...Need DataFrame and return Dataframe"""

        df = df[(df['price'] > 1) & (df['price'] < 800000)]
        df = df[(df['locality'] == 'Nivelles') | (df['locality'] == 'Saint-Nicolas') | (df['locality'] == 'Arlon') | 
                (df['locality'] == 'Tournai') | (df['locality'] == 'Namur') | (df['locality'] == 'Virton') | 
                (df['locality'] == 'Marche-en-Famenne') | (df['locality'] == 'Verviers') | (df['locality'] == 'Soignies') | 
                (df['locality'] == 'Bastognes') | (df['locality'] == 'Ath') | (df['locality'] == 'Waremme') | 
                (df['locality'] == 'Liège') | (df['locality'] == 'Huy') | (df['locality'] == 'Thuin') | 
                (df['locality'] == 'Dinant') | (df['locality'] == 'Mouscron') | (df['locality'] == 'Neufchâteau') |
                (df['locality'] == 'Philippeville') | (df['locality'] == 'Mons') | (df['locality'] == 'Charleroi')]

        return df

class Plot: 
    
    def plot_home_type_by_quantity(self, df):
        """Give us the possibility to see witch home type is the most commun
        need Dataframe and show a plot"""

        df['quantity'] = 1
        test = df.groupby(['home_type']).agg({'quantity':sum})
        res = test.apply(lambda x: x.sort_values(ascending=False).head(3))
        res.plot(kind="bar")

        plt.show()

    def plot_surface_of_type_price(self, df):
        """Give us the possibility to see prices of properties by surface
        need Dataframe and show a plot""" 

        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'Villa') | (df['home_type'] == 'Maison')]
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
        """Give us the possibility to see proportions of home type
        need Dataframe and show a plot"""

        first = (df['home_type']=='Appartement').sum()
        second = (df['home_type']=='Maison').sum()
        third = (df['home_type']=='Villa').sum()
        plt.pie([first, second, third],  labels=['Appartement', 'Maison', 'Villa'], colors=['red','blue', 'green'], 
                shadow=False, autopct='%1.1f%%', startangle=100)
        plt.axis('equal')
        plt.title('Home type proportions')
        plt.show()
    
    def home_type_price_dispersion(self, df):
        """Give us the possibility to see the price dispersion of home type
        need Dataframe and show a plot"""
        
        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'Villa') | (df['home_type'] == 'Maison')]
        df = df[(df['price'] > 1) & (df['price'] < 800000)]
        sns.set_style('whitegrid')
        # Violin plot
        sns.violinplot(x='home_type', y='price', data=df)
        plt.show()
    
    def home_type_surface_dispersion(self, df):
        """Give us the possibility to see the surface dispersion of home type
        need Dataframe and show a plot"""

        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'Villa') | (df['home_type'] == 'Maison')]
        df = df[df['surface_of_land_area'] > 0]
        df = df[(df['surface_of_land_area'] > 1) & (df['surface_of_land_area'] < 2000)]
        sns.set_style('whitegrid')
        # Violin plot
        sns.violinplot(x='home_type', y='surface_of_land_area', data=df)
        plt.show()
    
    def distribution_of_surface(self, df):
        """Give us the possibility to see the distribution of surface 
        to be able to know witch one to ignore
        need Dataframe and show a plot"""

        print(df['surface_of_land_area'].mean())
        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'Villa') | (df['home_type'] == 'Maison')]
        df = df[df['surface_of_land_area'] > 0]
        first = (df['surface_of_land_area'] > (df['surface_of_land_area'].mean())+500).sum()
        second = (df['surface_of_land_area'] < (df['surface_of_land_area'].mean())-500).sum()
        third = ((df['surface_of_land_area'] <= (df['surface_of_land_area'].mean())+500) & 
                    (df['surface_of_land_area'] <= (df['surface_of_land_area'].mean())+500)).sum()
        plt.pie([first, second, third],  labels=['Bigger than mean', 'Lesser than mean', 'Mean'], colors=['red','blue', 'green'], 
                shadow=False, autopct='%1.1f%%', startangle=100)
        plt.axis('equal')
        plt.title('Surface distribution')
        plt.show()
    
    def distribution_of_price(self, df):
        """Give us the possibility to see the distribution of price 
        to be able to know witch one to ignore
        need Dataframe and show a plot"""

        print(df['price'].mean())
        df = df[(df['home_type'] == 'Appartement') | (df['home_type'] == 'Villa') | (df['home_type'] == 'Maison')]
        df = df[df['price'] > 0]
        first = (df['price'] > (df['price'].mean())+100000).sum()
        second = (df['price'] < (df['price'].mean())-100000).sum()
        third = ((df['price'] <= (df['price'].mean())+100000) & 
                    (df['price'] <= (df['price'].mean())+100000)).sum()
        plt.pie([first, second, third],  labels=['Bigger than mean', 'Lesser than mean', 'Mean'], colors=['red','blue', 'green'], 
                shadow=False, autopct='%1.1f%%', startangle=100)
        plt.axis('equal')
        plt.title('Price distribution')
        plt.show()
        
    def state_of_building(self,df):
        type_colors = ['#78C850', 
                    '#F08030',  
                    '#6890F0',  
                    '#A8B820',  
                    '#A8A878',  
                    '#A040A0', 
                    '#F8D030',  
                    '#E0C068',  
                    '#EE99AC',  
                    '#C03028',  
                    '#F85888',  
                    '#B8A038',  
                    '#705898',  
                    '#98D8D8',  
                    '#7038F8',  
                   ]

        df=df[df['state_of_building'] != '0']
        sns.countplot(x='state_of_building', data=df, palette=type_colors)
        plt.xticks(rotation=-45)
        plt.show()
    
    def city_dispersion(self, df):
        """We had a problem with our csv file, first half of locality was only street name so
        we couldn't find whitch city it was, so we decided to look only to the second half"""

        df_city = df.loc[4503:]
        df = df[(df['price'] > 1) & (df['price'] < 800000)]
        df_city['quantity'] = 1
        test = df_city.groupby(['locality']).agg({'quantity':sum})
        res = test.apply(lambda x: x.sort_values(ascending=False))
        res.plot(kind="bar")

        plt.show()
    
    def mean_price_by_city(self, df):
        """With this function we will be able to see mean price of all city
        need Dataframe and show a plot"""

        df_city = df.loc[4503:]
        df = df[(df['price'] > 1) & (df['price'] < 800000)]
        test = df_city.groupby(['locality']).agg({'price':['mean']})
        res = test.apply(lambda x: x.sort_values(ascending=False))
        res.plot(kind="bar")

        plt.show()

    def most_and_less_expensive_municipality_wallonia(self, df):
        """With this function we will be able to see mean price of all wallonian city
        need Dataframe and show a plot"""

        df = AnalyseData().sorted_by_city_in_wallonia(df)
        test = df.groupby(['locality']).agg({'price':['mean']})
        res = test.apply(lambda x: x.sort_values(ascending=False))
        
        res.plot(kind="bar")

        plt.show()
    
    def median_price_municipality_wall(self, df):
        """With this function we will be able to see median price of all wallonian city
        need Dataframe and show a plot"""
        
        df = AnalyseData().sorted_by_city_in_wallonia(df)
        test = df.groupby(['locality']).agg({'price':['median']})
        res = test.apply(lambda x: x.sort_values(ascending=False))
        
        res.plot(kind="bar")

        plt.show()
    
    def price_per_square_metre_municipality_wall(self, df):
        """With this function we will be able to see price per square metre of all wallonian city
        need Dataframe and show a plot"""

        df = AnalyseData().sorted_by_city_in_wallonia(df)
        df = df[(df['surface_of_land_area'] > 1)]
        df['square_meter'] = df['price']/df['surface_of_land_area']
        print(df.head())
        test = df.groupby(['locality']).agg({'square_meter':['mean']})
        res = test.apply(lambda x: x.sort_values(ascending=False))
        
        res.plot(kind="bar")

        plt.show()
        
        
        #Updated on Saturday
    def compare_state_of_building_withprice(self,df):
        
        df=df[(df['state_of_building']=='Bien neuf') | (df['state_of_building'] == 'Besoin de travaux') | (df['state_of_building'] == 'Rénové')|         (df['state_of_building'] == 'Bon')]
        df = df[df['price'] > 0]
        ax = sns.stripplot(x='state_of_building', y='price', data=df, jitter=0.4, size=10 ,  hue='state_of_building' , linewidth=1)
        plt.title("State of building comparison wiht price", loc="left")
        fig = plt.gcf()


        fig.set_size_inches(12, 8)
        print(df.dtypes)
        df=df.sort_values('price')  
        #updated on Saturday
    def price_in_flandre(self,df):
        df_city = df.loc[4503:]
        df = df[(df['locality'] == 'Hal-Vilvorde')| (df['locality'] == 'Audenarde')| (df['locality'] == 'Hasselt')| (df['locality'] == 'Gand')|         (df['locality'] == 'Alost')| (df['locality'] == 'Ostende')| (df['locality'] == 'Huy')| (df['locality'] == 'Bruges') | (df['locality'] ==         'Anvers')]
        df = df[df['price'] > 0]
        ax = sns.stripplot(x='locality', y='price', data=df, jitter=0.4, size=10 ,  hue='locality' , linewidth=1)
        plt.title("State of building comparison wiht price", loc="left")
        fig = plt.gcf()


        fig.set_size_inches(16, 12)
        
        
        
        
df = Cleaning().import_from_csv()
df = Cleaning().check_space(df)
df = Cleaning().delete_duplicate(df)
df = Cleaning().remplace_NaN_value(df)
#df = Cleaning().clean_errors(df)
df = Cleaning().change_HOUSE_to_Maison(df)

AnalyseData().how_many_row_and_columns(df)
AnalyseData().describe_of_values(df)
#Plot().plot_home_type_by_quantity(df)
#Plot().plot_surface_of_type_price(df)
#Plot().proportions_of_home_type(df)
#Plot().home_type_price_dispersion(df)
#Plot().home_type_surface_dispersion(df)
#Plot().distribution_of_surface(df)
#Plot().distribution_of_price(df)
#Plot().state_of_building(df)
#Plot().city_dispersion(df)
#Plot().mean_price_by_city(df)
#Plot().most_and_less_expensive_municipality_wallonia(df)
#Plot().median_price_municipality_wall(df)
Plot().price_per_square_metre_municipality_wall(df)
#Plot().price_in_flandre(df)