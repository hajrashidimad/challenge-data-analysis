from CleanCsvFiles import Cleaning
from DataAnalysis import AnalyseData, Plot

if __name__ == "__main__":
    """Calling all the needed function"""

    df = Cleaning().import_from_csv()
    df = Cleaning().check_space(df)
    df = Cleaning().delete_duplicate(df)
    df = Cleaning().remplace_NaN_value(df)
    #df = Cleaning().clean_errors(df)
    df = Cleaning().change_HOUSE_to_Maison(df)

    AnalyseData().how_many_row_and_columns(df)
    AnalyseData().describe_of_values(df)
    # Plot().plot_home_type_by_quantity(df)
    # Plot().plot_surface_of_type_price(df)
    # Plot().proportions_of_home_type(df)
    # Plot().home_type_price_dispersion(df)
    # Plot().home_type_surface_dispersion(df)
    # Plot().distribution_of_surface(df)
    # Plot().distribution_of_price(df)
    # Plot().plot_price_area(df)
    # Plot().plot_price_room(df)
    # Plot().state_of_building(df)
    # Plot().city_dispersion(df)
    # Plot().mean_price_by_city(df)
    # Plot().most_and_less_expensive_municipality_wallonia(df)
    # Plot().median_price_municipality_wall(df)
    # Plot().price_per_square_metre_municipality_wall(df)
    # Plot().price_in_flandre(df)
    # Plot().most_and_less_expensive_municipality_flandre(df)
    # Plot().median_price_municipality_flandre(df)
    Plot().price_per_square_metre_municipality_flandre(df)
    # Plot().belguim_house_price(df)

