import pandas as pd

def test_hello_world_fails():
    df1=pd.DataFrame({'a':[1,2,3,4,5]})
    df2=pd.DataFrame({'a':[6,7,8,9,10]})
    pd.testing.assert_frame_equal(df1,df2)

def test_hello_world_passes():
    df1=pd.DataFrame({'a':[1,2,3,4,5]})
    pd.testing.assert_frame_equal(df1,df1)