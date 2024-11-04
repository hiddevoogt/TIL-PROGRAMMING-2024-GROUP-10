def generate_map(filepath):

    """
    Generates a choropleth map visualizing urbanization levels across municipalities.

    Args:
        filepath (str): Path to the shapefile containing municipality data.

    Returns:
        None: Displays an interactive map of municipalities with urbanization levels.

    Notes:
        - Loads municipality data, sets and converts the coordinate reference system (CRS) if needed.
        - Fills missing urbanization ('STED') values with 0, filters for values between 0 and 5.
        - Converts the GeoDataFrame to GeoJSON for use with Plotly.
        - Creates a choropleth map with hover data, custom color scale, and integer ticks for urbanization levels.
        - Centers the map on the Netherlands with a title.
    """

    import pandas as pd
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import plotly.express as px
    import json

    # Load Gemeenten shapefile
    gemeenten = gpd.read_file(filepath)

    # Set CRS if not defined and convert to EPSG:28992
    if gemeenten.crs is None:
        gemeenten = gemeenten.set_crs(epsg=4326)
    gemeenten = gemeenten.to_crs(epsg=4326)

    # Handle missing 'STED' values if necessary
    # For example, fill NaN with a default value or remove such rows
    gemeenten['STED'] = gemeenten['STED'].fillna(0)  # Example: fill NaN with 0

    # Filter gemeenten based on 'STED' values between 0 and 5 inclusive
    gemeenten_filtered = gemeenten[(gemeenten['STED'] >= 0) & (gemeenten['STED'] <= 5)].copy()

    # Convert GeoDataFrame to GeoJSON
    gemeenten_geojson = json.loads(gemeenten_filtered.to_json())

    # Assign 'GM_CODE' as 'id' for each GeoJSON feature
    for feature in gemeenten_geojson['features']:
        feature['id'] = feature['properties']['GM_CODE']

    # Create the choropleth map with Plotly
    fig = px.choropleth_mapbox(
        gemeenten_filtered,
        geojson=gemeenten_geojson,
        locations='GM_CODE',
        color='STED',
        hover_name='GM_NAAM',
        hover_data={'STED': True, 'GM_CODE': False},
        color_continuous_scale=px.colors.sequential.OrRd[::-1],
        mapbox_style='carto-positron',
        zoom=6,
        center={"lat": 52.1326, "lon": 5.2913},
        opacity=0.8,
        labels={'STED': 'Urbanisation Level'},
        height=800,
        width=800
    )

    # Define integer tick values based on 'STED' range
    min_sted = int(gemeenten_filtered['STED'].min())
    max_sted = int(gemeenten_filtered['STED'].max())
    tick_values = list(range(min_sted, max_sted + 1))

    # Update the color bar to show only integer ticks
    fig.update_coloraxes(
        colorbar=dict(
            title="Urbanisation Level",
            tickmode='array',
            tickvals=tick_values,
            ticktext=[str(tick) for tick in tick_values],
        )
    )

    # Add a centered title and adjust layout
    fig.update_layout(
        title_text='Urbanisation level per Municipality in 2020',
        title_x=0.5,
        margin={"r":0, "t":50, "l":0, "b":0},
    )

    # Display the interactive map
    fig.show()
