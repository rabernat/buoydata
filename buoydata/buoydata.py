import pandas as pd
from datetime import datetime

col_names = ['id', 'mm', 'dd', 'yy',
            'lat', 'lon', 'temp',
            've', 'vn', 'spd', 
            'var_lat', 'var_lon', 'var_tmp']

def _parse_date(mm, dd, yy):
    dd = float(dd)
    mm = int(mm)
    yy = int(yy)
    day = int(dd)
    hour = int(24 * (dd - day))
    return datetime(yy, mm, day, hour)

def read_buoy_data(fname):
    """Read NOAA Global Drifter Program text data into pandas format.

    Parameters
    ----------
    fname : str

    Returns
    -------
    df : datafram
    """
    return pd.read_csv(fname, names=col_names, sep='\s+',
                 header=None, na_values=999.999,
                 parse_dates={'time': [1,2,3]},
                 date_parser=_parse_date)
