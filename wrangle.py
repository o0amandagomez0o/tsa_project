# for presentation purposes
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

# working with dates
from datetime import datetime

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# working with dates
from datetime import datetime

import warnings
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.preprocessing import MultiLabelBinarizer

warnings.filterwarnings("ignore")


'''
*------------------*
|                  |
|     ACQUIRE      |
|                  |
*------------------*
'''

def get_data():
    """
    
    """
    
    city = pd.read_csv('GlobalLandTemperaturesByCity.csv')
    
    au = pd.DataFrame(city[city['City'] == 'Auckland']).\
    reset_index().drop(columns=['index']).\
    set_index('dt').sort_index().\
    rename(columns = {'AverageTemperature' : 'avg_temp',
                      'AverageTemperatureUncertainty' : 'avg_temp_uncertainty', 
                      'City': 'city', 'Country': 'country', 'Latitude': 'latitude', 
                      'Longitude': 'longitude'})
    
    au.index = pd.to_datetime(au.index)
    
    return au





'''
*------------------*
|                  |
|     PREPARE      |
|                  |
*------------------*
'''

def prep_auck(au):
    """
    
    """
    #drop cols
    au = au.drop(columns = ['city', 'country', 'latitude', 'longitude'])
    
    #remove outliers
    au = au['1893':]
    
    # drop col
    au = au.drop(columns = ['avg_temp_uncertainty'])
    
    # drop 09/2013 NaN
    au.dropna(inplace=True)
    
    au['weekday'] = au.index.day_name()
    
    au['month'] = au.index.month
    
    return au