#function 1


def trips_per_year_total_and_period(data):  
    #importing useful libraries 
    import pandas as pd
    import seaborn as sns
    import plotly.express as px
    import matplotlib.pyplot as plt

    #Selecting the right data to visualize
    df = data
    df_filtered = df[df['TravelModes'] == 'Total']

    #Show the plot using sns.barplot
    sns.barplot(data=df_filtered, x='Period', y='Trips_Per_Year', hue='TravelModes', errorbar=None)
    plt.title("Trips Per Year Total and Period")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.show()

#function 2
def trips_per_yearby_travel_mode_and_period(data):
    #importing useful libraries 
    import pandas as pd
    import seaborn as sns
    import plotly.express as px
    import matplotlib.pyplot as plt

    #Selecting the right data to visualize
    df = data
    df_filtered = df[df['TravelModes'] != 'Total']

    #Show the plot using sns.barplot
    sns.barplot(data=df_filtered, x='Period', y='Trips_Per_Year', hue='TravelModes', errorbar=None)
    plt.title("Trips Per Year by Travel Mode and Period")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.show()

#function 3
def line_plot_trips(data): 
    #importing useful libraries 
    import pandas as pd
    import seaborn as sns
    import plotly.express as px
    import matplotlib.pyplot as plt

    #Selecting the right data to visualize
    df = data
    df_filtered = df[df['TravelModes'] != 'Total']
    
    #Show the plot using sns.lineplot
    sns.lineplot(data=df_filtered, x='Period', y='Trips_Per_Year', hue='TravelModes', errorbar=None)
    plt.title("Trips Per Year by Travel Mode and Period")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.show()

#function 4
def area_chart_trips(data): 
    #importing useful libraries 
    import pandas as pd
    import seaborn as sns
    import plotly.express as px
    import matplotlib.pyplot as plt

    #Selecting the right data to visualize
    df = data
    df_filtered = df[df['TravelModes'] != 'Total']
    #Summing trips per year for each mode and resetting the index
    df_grouped = df_filtered.groupby(['Period', 'TravelModes']).agg({'Trips_Per_Year': 'sum'}).reset_index()
    #Group modes together
    df_pivot = df_grouped.pivot(index='Period', columns='TravelModes', values='Trips_Per_Year')
    df_pivot = df_pivot.sort_index()

    #Plot the stacked area chart with absolute values
    plt.figure(figsize=(10,6))
    plt.stackplot(df_pivot.index, df_pivot.T, labels=df_pivot.columns)
    plt.title("Trips Per Year by Travel Mode and Period")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.xlabel("Period")
    plt.ylabel("Trips Per Year")
    plt.tight_layout()
    plt.show()