def plot_travelminutes():

    import pandas as pd
    import plotly.express as px
    df = pd.read_csv("values_named_clean_mobility_data.csv")

    travelmode_animation = df.groupby(['RegionCharacteristics', 'Period']).sum('Time_Travelled_Minutes_Per_Day').reset_index()

    fig = px.line(travelmode_animation, 
                x='Period', 
                y='Time_Travelled_Minutes_Per_Day', 
                color='RegionCharacteristics')

    fig.show()

    heatmap_data = travelmode_animation.pivot(index='RegionCharacteristics', columns='Period', values='Time_Travelled_Minutes_Per_Day')

    fig = px.imshow(heatmap_data, 
                    labels=dict(x="Period", y="RegionCharacteristics", color="Travel Time (min/day)"), 
                    aspect="auto")

    fig.show()

