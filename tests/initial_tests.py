import pandas as pd
from source.data_quality import DataQuality
import psycopg2
import pytest

def test_hello_world_fails():
    with pytest.raises(AssertionError):
        df1=pd.DataFrame({'a':[1,2,3,4,5]})
        df2=pd.DataFrame({'a':[6,7,8,9,10]})
        pd.testing.assert_frame_equal(df1,df2)

def test_hello_world_passes():
    df1=pd.DataFrame({'a':[1,2,3,4,5]})
    pd.testing.assert_frame_equal(df1,df1)


def test_hello_world_two_query_outcomes_are_the_same():
    query='select SUM(Salary) from Employee'
    dq = DataQuality(query,query)

    df1=dq.run_source_query()
    df2=dq.run_target_query()

    pd.testing.assert_frame_equal(df1,df2)

def test_hello_world_two_query_outcomes_are_not_the_same():
    with pytest.raises(AssertionError):
        query_source='select SUM(Salary) from Employee'
        query_target='select AVG(Salary) from Employee'
        dq = DataQuality(query_source,query_target)

        df1=dq.run_source_query()
        df2=dq.run_target_query()

        pd.testing.assert_frame_equal(df1,df2)

