def plot_travelminutes():
    import pandas as pd
    import plotly.express as px

    # Load the data
    df = pd.read_csv("values_named_clean_mobility_data.csv")

    # Group and aggregate data for the line plot
    travelmode_animation = df.groupby(['RegionCharacteristics', 'Period']).sum('Time_Travelled_Hours_Per_Year').reset_index()

    # Line plot with improved labels and layout
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
        title="Travel Time Over Time by Region",
        markers=True
    )
    
    fig.update_layout(
        title_font=dict(size=20),
        title_x=0.5,  # Center the title
        xaxis_title="Period",
        yaxis_title="Average Hours Travelled Per Year",
        legend_title="Regions",
        template="plotly_white",  # Use a clean template for aesthetics
        font=dict(family="Arial", size=14)
    )
    
    fig.show()



#NORMAL HEAT MAP CODE

    heatmap_data = travelmode_animation.pivot(index='RegionCharacteristics', columns='Period', values='Time_Travelled_Hours_Per_Year')

    fig = px.imshow(heatmap_data, 
                    labels=dict(x="Period", y="RegionCharacteristics", color="Travel Time (hours/year)"), 
                    aspect="auto")

    fig.show()