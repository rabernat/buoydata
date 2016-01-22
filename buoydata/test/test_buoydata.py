from buoydata import buoydata
import pandas as pd
import datetime as datetime
import pytest

def test_parse_date():
    mm, dd, yy = '2', '2.5', '2000'
    date = buoydata._parse_date(mm,dd,yy)
    assert date == datetime.datetime(2000, 2, 2, 12, 0)

@pytest.fixture(scope='session')
def datafile(tmpdir_factory):
    data = """
 7702986    3  8.000 1988    -1.320   274.848    25.473   999.999   999.999   999.999  0.25315E-04  0.33929E-04  0.45179E-02"""
    fn = tmpdir_factory.mktemp('data').join('buoydata.dat')
    fn.write(data)
    return str(fn)

def test_read_buoy_data(datafile):
    df = buoydata.read_buoy_data(datafile)
    assert isinstance(df, pd.DataFrame)
    assert len(df)==1
    row = df.loc[0]
    for colname in ['time', 'lat', 'lon', 'temp', 've', 'vn', 'spd',
            'var_lat', 'var_lon', 'var_tmp']:
        assert colname in row
    assert row.id == 7702986
