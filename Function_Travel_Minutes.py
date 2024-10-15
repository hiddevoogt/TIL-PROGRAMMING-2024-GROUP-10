def plot_travelminutes():
    import pandas as pd
    import plotly.express as px

    # Load the data
    df = pd.read_csv("values_named_clean_mobility_data.csv")

    # Group and aggregate data for the line plot
    travelmode_animation = df.groupby(['RegionCharacteristics', 'Period']).sum('Time_Travelled_Minutes_Per_Day').reset_index()

    # Line plot with improved labels and layout
    fig = px.line(
        travelmode_animation, 
        x='Period', 
        y='Time_Travelled_Minutes_Per_Day', 
        color='RegionCharacteristics',
        labels={
            "Period": "Time Period",
            "Time_Travelled_Minutes_Per_Day": "Travel Time (Minutes/Day)",
            "RegionCharacteristics": "Region Characteristics"
        },
        title="Travel Time Over Time by Region",
        markers=True
    )
    
    fig.update_layout(
        title_font=dict(size=20),
        title_x=0.5,  # Center the title
        xaxis_title="Period",
        yaxis_title="Average Minutes Traveled Per Day",
        legend_title="Regions",
        template="plotly_white",  # Use a clean template for aesthetics
        font=dict(family="Arial", size=14)
    )

    # Display line plot
    fig.show()

    # Group and aggregate data for the heatmap
    travelmode_heatmap = df.groupby(['RegionCharacteristics', 'Period', 'TravelModes']).sum('Time_Travelled_Minutes_Per_Day').reset_index()
    travelmode_heatmap = travelmode_heatmap[travelmode_heatmap['TravelModes'] != 'Total']
    # Get global minimum and maximum for fixed scale across all periods
    min_travel_time = travelmode_heatmap['Time_Travelled_Minutes_Per_Day'].min()
    max_travel_time = travelmode_heatmap['Time_Travelled_Minutes_Per_Day'].max()

    # Now animate the heatmap using the correct approach
    # Create an empty list to store frames for animation
    frames = []

    # Iterate over each period to create a heatmap for each period
    for period in travelmode_heatmap['Period'].unique():
        # Pivot data for the current period
        period_data = travelmode_heatmap[travelmode_heatmap['Period'] == period]
        heatmap_data = period_data.pivot_table(
            index='RegionCharacteristics', 
            columns='TravelModes', 
            values='Time_Travelled_Minutes_Per_Day'
        ).fillna(0)  # Fill missing values with 0

        # Append the current heatmap frame to the list of frames
        frames.append({
            "data": [px.imshow(
                heatmap_data, 
                labels=dict(x="Travel Modes", y="Region Characteristics", color="Travel Time (min/day)"),
                aspect="auto",
                color_continuous_scale="Viridis",
                zmin=min_travel_time,  # Set fixed minimum for color scale
                zmax=max_travel_time   # Set fixed maximum for color scale
            ).data[0]],
            "name": str(period)  # Set the frame name to the current period
        })

    # Create an initial heatmap for the first period
    initial_data = travelmode_heatmap[travelmode_heatmap['Period'] == travelmode_heatmap['Period'].min()]
    heatmap_data = initial_data.pivot_table(
        index='RegionCharacteristics', 
        columns='TravelModes', 
        values='Time_Travelled_Minutes_Per_Day'
    ).fillna(0)

    fig = px.imshow(
        heatmap_data, 
        labels=dict(x="Travel Modes", y="Region Characteristics", color="Travel Time (min/day)"),
        aspect="auto",
        color_continuous_scale="Viridis",
        zmin=min_travel_time,  # Set fixed minimum for color scale
        zmax=max_travel_time   # Set fixed maximum for color scale
    )

    # Add the frames to the figure
    fig.frames = frames

    # Update layout for better aesthetics, including a slider
    fig.update_layout(
        title="Animated Heatmap of Travel Time by Region and Travel Mode",
        title_font=dict(size=20),
        title_x=0.5,
        xaxis_title="Travel Modes",
        yaxis_title="Region Characteristics",
        template="plotly_white",
        coloraxis_colorbar=dict(title="Minutes"),
        sliders=[{
            "steps": [
                {
                    "args": [[str(period)], {"frame": {"duration": 500, "redraw": True}, "mode": "immediate"}],
                    "label": str(period),
                    "method": "animate"
                }
                for period in travelmode_heatmap['Period'].unique()
            ],
            "currentvalue": {
                "prefix": "Year: ",
                "font": {"size": 20}
            },
            "pad": {"b": 10},
        }],
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }]
    )

    # Add color bar details
    fig.update_coloraxes(colorbar_title_text='Minutes')

    # Show the figure
    fig.show()


    heatmap_data = travelmode_animation.pivot(index='RegionCharacteristics', columns='Period', values='Time_Travelled_Minutes_Per_Day')

    fig = px.imshow(heatmap_data, 
                    labels=dict(x="Period", y="RegionCharacteristics", color="Travel Time (min/day)"), 
                    aspect="auto")

    fig.show()