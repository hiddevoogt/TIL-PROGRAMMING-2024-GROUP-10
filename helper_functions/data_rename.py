import pandas as pd

def make_named_clean_dataset(dataset_unnamed):

    """
    Cleans and renames columns in a dataset, mapping codes to descriptive names for readability.

    Args:
        dataset_unnamed (pd.DataFrame): DataFrame with unnamed columns that need to be mapped to 
            descriptive labels.

    Returns:
        pd.DataFrame: A cleaned DataFrame with renamed columns, mapped values for easier interpretation, 
            and filtered data for specific conditions.
    
    Notes:
        - Columns for travel motives, population groups, travel modes, margins, region characteristics, 
          and periods are mapped to readable names.
        - Filters the dataset to include only "Population 6 years or older" and data with "Value" in 
          the margins column.
        - Retains data with "urbanised" in the 'RegionCharacteristics' column.
        - Drops rows with missing values and returns the cleaned DataFrame.
    """
    
    data = dataset_unnamed

    # Map travelmotives
    travel_motives_mapping = {
        "2030170": "Travel to/from work, (non)-daily commute",
        "2030190": "Services/care",
        "2030200": "Shopping, groceries, fun shopping",
        "2030210": "Attending education/courses",
        "2030220": "Visits including staying overnight",
        "2030230": "Leisure, sports",
        "2030240": "Touring/walking",
        "2030250": "Other",
        "2820740": "Professionally",
        "T001080": "Total"
    }

    # Map population
    population_mapping = {
        "A048710": "Population 6 years or older",
        "A048709": "Population: 12 years or older"
    }

    # Map tavelmodes
    travel_modes_mapping = {
        "T001093": "Total",
        "A048583": "Passenger car (driver)",
        "A048584": "Passenger car (passenger)",
        "A018981": "Train",
        "A018982": "Bus/tram/metro",
        "A018984": "Bike",
        "A018985": "Walking",
        "A018986": "Other"
    }

    # Map margins
    margins_mapping = {
        "MW00000": "Value",
        "MOG0095": "Lower bound 95% confidence interval",
        "MBG0095": "Upper bound 95% confidence interval"
    }

    # Map regions
    region_char_mapping = {
        "NL01    ": "The Netherlands",
        "LD01    ": "Noord-Nederland (LD)",
        "LD02    ": "Oost-Nederland (LD)",
        "LD03    ": "West-Nederland (LD)",
        "LD04    ": "Zuid-Nederland (LD)",
        "PV20    ": "Groningen (PV)",
        "PV21    ": "Fryslân (PV)",
        "PV22    ": "Drenthe (PV)",
        "PV23    ": "Overijssel (PV)",
        "PV24    ": "Flevoland (PV)",
        "PV25    ": "Gelderland (PV)",
        "PV26    ": "Utrecht (PV)",
        "PV27    ": "Noord-Holland (PV)",
        "PV28    ": "Zuid-Holland (PV)",
        "PV29    ": "Zeeland (PV)",
        "PV30    ": "Noord-Brabant (PV)",
        "PV31    ": "Limburg (PV)",
        "1018850 ": "Extremely urbanised",
        "1018905 ": "Strongly urbanised",
        "1018955 ": "Moderately urbanised",
        "1019005 ": "Hardly urbanised",
        "1019052 ": "Not urbanised"
    }

    # Map periods
    periods_mapping = {
        "2018JJ00": "2018",
        "2019JJ00": "2019",
        "2020JJ00": "2020",
        "2021JJ00": "2021",
        "2022JJ00": "2022",
        "2023JJ00": "2023"
    }

    # Map the column names
    data.rename(columns={
        "TravelMotives": "TravelMotivesCode",
        "Population": "PopulationCode",
        "TravelModes": "TravelModesCode",
        "Margins": "MarginsCode",
        "RegionCharacteristics": "RegionCharacteristicsCode",
        "Periods": "PeriodsCode",
        "Trips_1": "Trips_Per_Day",
        "DistanceTravelled_2": "Distance_Travelled_PassengerKm_Per_Day",
        "TimeTravelled_3": "Time_Travelled_Minutes_Per_Day",
        "Trips_4": "Trips_Per_Year",
        "DistanceTravelled_5": "Distance_Travelled_PassengerKm_Per_Year",
        "TimeTravelled_6": "Time_Travelled_Hours_Per_Year"
    }, inplace=True)

    # Map the columns with the difined maps
    data['TravelMotives'] = data['TravelMotivesCode'].map(travel_motives_mapping)

    data['Population'] = data['PopulationCode'].map(population_mapping)

    data['TravelModes'] = data['TravelModesCode'].map(travel_modes_mapping)

    data['Margins'] = data['MarginsCode'].map(margins_mapping)

    data['RegionCharacteristics'] = data['RegionCharacteristicsCode'].map(region_char_mapping)

    data['Period'] = data['PeriodsCode'].map(periods_mapping)

    # List of original code columns to drop
    code_columns = [
        'TravelMotivesCode',
        'PopulationCode',
        'TravelModesCode',
        'MarginsCode',
        'RegionCharacteristicsCode',
        'PeriodsCode'
    ]

    # Drop the code columns
    data.drop(columns=code_columns, inplace=True)

    # List of numerical columns
    numeric_columns = [
        'Trips_Per_Day',
        'Distance_Travelled_PassengerKm_Per_Day',
        'Time_Travelled_Minutes_Per_Day',
        'Trips_Per_Year',
        'Distance_Travelled_PassengerKm_Per_Year',
        'Time_Travelled_Hours_Per_Year'
    ]

    # Convert columns to numeric, coercing errors to NaN
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    data = data[data['RegionCharacteristics'].str.contains('urbanised', case=False, na=False)]

    # Only keep the values and only show population of 6 years and older
    data = data[(data['Margins'] == 'Value') & (data['Population'] == 'Population 6 years or older') ]

    clean_data = data.dropna()
    print("Named And Cleaned Data After Dropping Missing Values:", clean_data.shape, "\n")

    return clean_data