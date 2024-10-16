import plotly.express as px
def barplotanimation(dataset, column, order):

    # Group by RegionCharacteristics and TravelModes, and sum the distances
    kmtot = dataset.groupby(['RegionCharacteristics', 'TravelModes', 'Period'])[column].sum().reset_index()

    # Create the bar plot
    fig = px.bar(data_frame=kmtot,
                x='RegionCharacteristics',  # Group by urbanization level
                y=column,
                color='TravelModes',  # Different colors for each travel mode
                barmode='group',
                animation_frame = "Period",
                category_orders={"RegionCharacteristics": order}  # Explicitly set category order
                )  # Order categories)  # Group bars next to each other

    # Adjust the animation speed (e.g., 2000 milliseconds per frame)
    fig.update_layout(
    updatemenus=[{
        'type': 'buttons',
        'showactive': False,
        'buttons': [{
            'label': 'Play',
            'method': 'animate',
            'args': [None, 
                        {'frame': {'duration': 2000, 'redraw': True},
                        'fromcurrent': True, 'transition': {'duration': 1000}}]
        }, {
            'label': 'Pause',
            'method': 'animate',
            'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 
                                'mode': 'immediate',
                                'transition': {'duration': 0}}]
        }]
    }]
    )

    # Show the plot
    fig.show()