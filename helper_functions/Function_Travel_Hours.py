
# This function defines the graphs that are used for measuring the effect of covid on travel hours over different levels of urbanisation

def plot_travelminutes():
    import pandas as pd
    import plotly.express as px

    
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