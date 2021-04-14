import pandas as pd
from source.data_quality import DataQuality
import psycopg2
import pytest
import numpy.testing as npt

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

def test_hello_world_foo():
    query_source='select company,SUM(Salary) from public.Employee group by company'
    query_target='select company,SUM(Salary) from public.Employee group by company order by company desc'
    dq = DataQuality(query_source,query_target)

    df1=dq.run_source_query()
    df2=dq.run_target_query()

    df2.sort_values(by=df2.columns)
    pd.testing.assert_frame_equal(df1,df2,check_index_type=False,check_dtype=False)


def test_hello_world_assert_is_equal_even_though_column_names_are_different():
    query_source='select company as c1,SUM(Salary) as s1 from public.Employee group by company'
    query_target='select company as c1,SUM(Salary) as s2 from public.Employee group by company'
    dq = DataQuality(query_source,query_target)

    df1=dq.run_source_query()
    df2=dq.run_target_query()
    npt.assert_almost_equal(df1,df2)
    pd.testing.assert_frame_equal(df1,df2,check_like=True,check_dtype=False,check_names=False,check_column_type=False)


def test_hello_world_numpy():
    query_source='select SUM(Salary) as s1 from public.Employee group by company'
    query_target='select SUM(Salary) as s1 from public.Employee group by company'
    dq = DataQuality(query_source,query_target)

    df1=dq.run_source_query()
    df2=dq.run_target_query()
    npt.assert_almost_equal(df1,df2)

