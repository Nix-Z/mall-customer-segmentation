import pandas as pd
import numpy as np
from datavisualization import visualize_data

def engineer_features():
    data = visualize_data()

    # Drop unnecessary features
    data.drop(['CustomerID', 'Gender', 'Age'], axis=1, inplace=True)

    # Save cleansed data
    data.to_csv('mall_customer_cleansed_data.csv', index=False)

    return data

engineer_features()
