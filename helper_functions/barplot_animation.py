import plotly.express as px
import pandas as pd

def barplotanimation(dataset, column, yaxis_name):
    
    """
    Creates an animated bar plot to show data by urbanization level and travel mode over time.

    Args:
        dataset (pd.DataFrame): DataFrame with columns 'RegionCharacteristics', 'TravelModes', 'Period', 
            and the specified column for the y-axis.
        column (str): Column name to display on the y-axis.
        yaxis_name (str): Label for the y-axis.

    Returns:
        None: Displays an animated bar plot with play and pause controls.

    """

    # Define the correct order for 'RegionCharacteristics'
    urbanization_order = ['Not urbanised', 'Hardly urbanised', 'Moderately urbanised', 'Strongly urbanised', 'Extremely urbanised']

    # Ensure 'RegionCharacteristics' follows this order
    dataset.loc[:, 'RegionCharacteristics'] = pd.Categorical(
        dataset['RegionCharacteristics'], 
        categories=urbanization_order, 
        ordered=True
    )

    # Group by RegionCharacteristics and TravelModes, and sum the distances
    kmtot = dataset.groupby(['RegionCharacteristics', 'TravelModes', 'Period'])[column].sum().reset_index()


    # Create the bar plot
    fig = px.bar(data_frame=kmtot,
                x='RegionCharacteristics',  # Group by urbanization level
                y=column,
                color='TravelModes',  # Different colors for each travel mode
                barmode='group',
                animation_frame = "Period",
                category_orders={"RegionCharacteristics": urbanization_order},  # Explicitly set category order
                labels={column: yaxis_name,
                        'RegionCharacteristics': 'Urbanization level'},  # Custom y-axis label                
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