import pandas as pd
import plotly.express as px
def passenger_km_plot(df):

    df_total = df[
        (df['Population'] == 'Population 6 years or older') &
        (df['TravelMotives'] == 'Total') &
        (df['TravelModes'] == 'Total') &
        (df['Margins'] == 'Value')
    ].copy()

    df_total['Period'] = pd.to_numeric(df_total['Period'])
    df_fig = df_total[['Period', 'RegionCharacteristics', 'Distance_Travelled_PassengerKm_Per_Year']]


    fig = px.line(
        df_fig,
        x='Period',
        y='Distance_Travelled_PassengerKm_Per_Year',
        color='RegionCharacteristics',
        markers=True,
        title='Passenger Kilometers Over Time by Urbanization Level',
        labels={
            'Period': 'Year',
            'Distance_Travelled_PassengerKm_Per_Year': 'Passenger Kilometers per Year',
            'RegionCharacteristics': 'Urbanization Level'
        }
    )

    fig.update_layout(
        legend_title_text='Urbanization Level',
        legend=dict(x=1.05, y=1),
        margin=dict(t=50, b=50, l=50, r=50)
    )

    fig.show()

def passenger_prop_plot(df):
    
    df_total = df[
        (df['Population'] == 'Population 6 years or older') &
        (df['TravelMotives'] == 'Total') &
        (df['TravelModes'] == 'Total') &
        (df['Margins'] == 'Value')
    ].copy()

    df_total['Period'] = pd.to_numeric(df_total['Period'])

    df_fig = df_total[['Period', 'RegionCharacteristics', 'Distance_Travelled_PassengerKm_Per_Day']]

    fig2 = px.area(
        df_fig,
        x='Period',
        y='Distance_Travelled_PassengerKm_Per_Day',
        color='RegionCharacteristics',
        title='Proportion of Passenger Kilometers by Urbanization Level Over Time',
        labels={
            'Period': 'Year',
            'Distance_Travelled_PassengerKm_Per_Day': 'Passenger Kilometers per Day',
            'RegionCharacteristics': 'Urbanization Level'
        }
    )

    fig2.update_layout(
        legend_title_text='Urbanization Level',
        legend=dict(x=1.05, y=1),
        margin=dict(t=50, b=50, l=50, r=50),
        xaxis=dict(tickformat="%Y") 
    )
    fig2.show()