
# This function defines the graphs that are used for measuring the effect of covid on travel hours over different levels of urbanisation

def plot_travelminutes():
    import pandas as pd
    import plotly.express as px

    """
    Generates visualizations to analyze the impact of COVID-19 on travel time across different urbanization levels.

    This function reads travel data, groups it by urbanization level and period, and creates:
        1. A line plot showing travel time over years across urbanization levels.
        2. A heatmap displaying travel time distribution over time and urbanization levels.

    Returns:
        None: Displays a line plot and a heatmap.

    Notes:
        - The line plot shows the yearly travel time trend by urbanization level.
        - The heatmap visualizes travel time distribution by period and region characteristics.
    """
    
    df = pd.read_csv("values_named_clean_mobility_data.csv")

    # Group the data for the line plot
    travelmode_animation = df.groupby(['RegionCharacteristics', 'Period']).sum('Time_Travelled_Hours_Per_Year').reset_index()

    # Code for lineplot
    fig = px.line(
        travelmode_animation, 
        x='Period', 
        y='Time_Travelled_Hours_Per_Year', 
        color='RegionCharacteristics',
        labels={
            "Period": "Time Period",
            "Time_Travelled_Hours_Per_Year": "Travel Time (Hours/Year)",
            "RegionCharacteristics": "Region Characteristics"
        },
        title="Lineplot: Travel Time Over Time by Region",
        markers=True
    )
    # Layout of graph
    fig.update_layout(
        title_font=dict(size=20),
        title_x=0.5,  
        xaxis_title="Period",
        yaxis_title="Average Hours Travelled Per Year",
        legend_title="Regions",
        template="plotly_white",  
        font=dict(family="Arial", size=14)
    )
    
    fig.show()



    # Code for heatmap


    # Fitting the code for the heatmap
    heatmap_data = travelmode_animation.pivot(index='RegionCharacteristics', columns='Period', values='Time_Travelled_Hours_Per_Year')

    fig = px.imshow(heatmap_data, 
                    labels=dict(x="Period", y="RegionCharacteristics", color="Travel Time (hours/year)"), 
                    aspect="auto", title = "Heatmap: Travel Time Over Time by Region")
    
    #Layout of the lineplot
    fig.update_layout(title_font=dict(size=20), font=dict(family="Arial", size=14),
        title_x=0.5,)

    fig.show()