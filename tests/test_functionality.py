## Required packages

import os
import sys
import pytest

import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal
from inspect import getmembers, isfunction

sys.path.insert(0, os.path.abspath("../p_toolkit"))

# print(sys.path)

from core import *

###Functionality tests

# def test_p_bon_helper():
#     """
#     The purpose of this test is performing numerical tests on the outputs from the p_bonnferoni_helper function. We test
#     different combinations of inputs and check their corresponding outputs:
#
#     - The first block tests the Bonferroni adjustment.
#     - The second one handls the cases with one of the values higher than 1, impossible for p-values.
#     - The third block checks how the maximum value of 1 is handled in the function.
#     """
#     ###basic tests
#     assert p_bonferroni_helper([0.07]) == [0.07], "a single value doesn't change under bonnferoni"
#     assert p_bonferroni_helper([0.07,0.2]) == [0.14,0.4], "p_bonnferoni_helper((0.07,0.2))== (0.14,0.4)"
#     assert p_bonferroni_helper([0.2,0.07]) == [0.4,0.14], "p_bonnferoni_helper((0.2,0.07))== (0.4,0.14)"
#     assert p_bonferroni_helper([0.01, 0.02, 0.03]) == [0.03, 0.06,0.09], "p_bonnferoni_helper((0.01, 0.02, 0.03))==(0.03, 0.06,0.09)"
#
#     ### all values are between 0 and 1
#     with pytest.raises(ValueError):
#           p_bonferroni_helper([-3])
#           p_bonferroni_helper([-3, .05])
#           p_bonferroni_helper([.05, -3])
#           p_bonferroni_helper([8])
#           p_bonferroni_helper([8, .05])
#           p_bonferroni_helper([.05,8])
#
#     ###maximum return is 1
#     assert p_bonferroni_helper([0.01, 0.7]) == [0.02,1], "test_p_bonnferoni_helper has max of 1"

	###formatting tests
	# https://github.com/datalyze-solutions/pandas-qt/blob/master/tests/test_DataFrameModel.py
	# https://data-lessons.github.io/library-python/03-data-types-and-format/
	#assert not data.empty
	#assert data is dataFrame
	#assert pvals == dtype(int32)
	# assert alpha == dtype(int32)


# def test_p_bh():
#     """
#     The purpose of this test is performing numerical tests on the outputs from the p_bh_helper function. We test
#     different combinations of inputs and check their corresponding outputs:
#
#     - The first block tests the BH adjustment.
#     - The second one handles the cases with one of the values higher than 1, impossible for p-values.
#     """
#     assert p_bh_helper([0.07]) == [0.07], "a single value doesn't change under bh"
#     assert p_bh_helper([0.07,0.2]) == [0.14,0.2], "p_bh_helper((0.07,0.2))== (0.14,0.2)"
#     assert p_bh_helper([0.2,0.07]) == [0.2,0.14], "p_bh_helper((0.2,0.07))== (0.2,0.14)"
#     assert p_bh_helper([0.01, 0.02, 0.03]) == [0.03, 0.03,0.03], "p_bh_helper((0.01, 0.02, 0.03))==(0.03, 0.03,0.03)"
#     assert p_bh_helper([0.02, 0.03, 0.01]) == [0.03, 0.03,0.03], "p_bh_helper((0.02, 0.03, 0.01))==(0.03, 0.03,0.03)"
#     assert p_bh_helper([.02,.12,.24,.56,.6]) == [0.1,0.6, 0.4,0.7, 0.6], "p_bh_helper((.02,.12,.24,.56,.6))==(0.1,0.6, 0.4,0.7, 0.6)"
#     assert p_bh_helper([0.04, 0.04, 0.04,0.08]) == [0.16,0.16,0.16,0.08], "p_bh_helper treats rep[eated values correctly"
#
#     ### all valid probabilities
#     with pytest.raises(ValueError):
#         p_bh_helper([-3])
#         p_bh_helper([-3, .05])
#         p_bh_helper([.05, -3])
#         p_bh_helper([8])
#         p_bh_helper([8, .05])
#         p_bh_helper([.05,8])
#
# 	# ###formatting tests
# 	# # https://github.com/datalyze-solutions/pandas-qt/blob/master/tests/test_DataFrameModel.py
# 	# assert not data.empty
# 	# assert data is dataFrame
# 	# assert BH_significant == type(numpy.bool_)
# 	# assert Bonf_significant == type(numpy.bool_)
#     #
# 	# ###formatting tests
# 	# # https://github.com/datalyze-solutions/pandas-qt/blob/master/tests/test_DataFrameModel.py
# 	# assert not data.empty
# 	# assert data is dataFrame
# 	# assert pvals == dtype(int32)
# 	# assert alpha == dtype(int32)

####p_adjust functionality
# def test_p_adjust():
#     """
#     The purpose of this test is evaluating the p_adjust with more real world data using Pandas dataframes under
#     different environments.
#     """
#     ##basic vector functionality"
#     d = { "p_value": [0.07], "adjusted": [0.07]}
#     df = pd.DataFrame(data = d)
#     assert p_adjust(data =[0.07], method = "bonf") == df, "p_adjust 1 value vector for bonnferoni"
#     assert p_adjust(data =[0.07], method = "bh") == df, "p_adjust single value vector for bh"
#
#     d = { "p_value": [0.07,0.2], "adjusted": [0.14,0.4]}
#     df = pd.DataFrame(data = d)
#     assert p_adjust(data =[0.07,0.2], method = "bonf") == df, "p_adjust 2 values vector for bonnferoni"
#
#     d = { "p_value": [0.07,0.2], "adjusted": [0.14,0.2]}
#     df = pd.DataFrame(data = d)
#     assert p_adjust(data =[0.07,0.2], method = "bh") == df, "p_adjust 2 values vector value for bh"
#
#     ###basic dataframe fuinctionality
#     d = {"test":["test 1"], "p_value": [0.05]}
#     df = pd.DataFrame(data = d)
#     ad = {"test":["test 1"], "p_value": [0.05],"adjusted": [0.05]}
#     adf = pd.DataFrame(data =ad)
#     assert p_adjust(data =df, method = "bonf") == adf, "bonferroni single value df under p_adjust"
#     assert p_adjust(data =df, method = "bh") == adf, "bh single value df under p_adjust"
#
#     d = {"test":["test 1", "test 2"], "p_value": [0.07,0.2]}
#     df = pd.DataFrame(data = d)
#     ad = {"test":["test 1", "test 2"], "p_value": [0.07,0.2],"adjusted": [0.14, 0.4]}
#     adf = pd.DataFrame(data =ad)
#     assert p_adjust(data =df, method = "bonf") == adf, "bonferroni 2 value df under p_adjust"
#
#     ad = {"test":["test 1", "test 2"], "p_value": [0.07,0.2],"adjusted": [0.14, 0.2]}
#     adf = pd.DataFrame(data =ad)
#     assert p_adjust(data =df, method = "bh") == adf, "bh 2 value df under p_adjust"
#
# 	# ###formatting tests
# 	# # https://github.com/datalyze-solutions/pandas-qt/blob/master/tests/test_DataFrameModel.py
# 	# assert not data.empty
# 	# assert data is dataFrame



def test_p_methods():
    """
    The purpose of this test is evaluating the p_adjust with more real world data using Pandas dataframes under
    different environments.
    """
    d = { "p_value": [0.07], "bonf_value": [0.05],"bonf_significant" :[False],"bh_value": [0.05], "bh_significant":[False] }
    df = pd.DataFrame(data = d)
    df = df[['p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    test =  p_methods(data =[0.07], alpha =0.05)
    test = test[['p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    assert test.equals(df), "p_methods 1 value vector, FALSE"

    d = { "p_value": [0.01], "bonf_value": [0.05],"bonf_significant" :[True],"bh_value": [0.05], "bh_significant":[True] }
    df = pd.DataFrame(data = d)
    df = df[['p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    test =  p_methods(data =[0.01], alpha =0.05)
    test = test[['p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    assert test.equals(df), "p_methods 1 value vector, TRUE"


    d = {"Test":["test 1", "test 2"], "p_value": [0.01,0.03], "bonf_value": [0.025,0.025],"bonf_significant" :[True,False],"bh_value": [0.025,0.05], "bh_significant":[True, True] }
    df = pd.DataFrame(data = d)
    df = df[['p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    test =  p_methods(data =[0.01,0.03], alpha =0.05)
    test = test[['p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    assert test.equals(df), "p_methods 2 values vector "


    ###dataframe tests
    d = {"Test":["test 1"], "p_value": [0.01] }
    df = pd.DataFrame(data = d)
    ad = {"Test":["test 1"], "p_value": [0.01], "bonf_value": [0.05],"bonf_significant" :[True],"bh_value": [0.05], "bh_significant":[True] }
    adf = pd.DataFrame(data = ad)
    adf = adf[['Test','p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    test =  p_methods(data =df, pv_index = "p_value", alpha =0.05)
    test = test[['Test','p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    d = {"Test":["test 1"], "p_value": [0.1] }
    df = pd.DataFrame(data = d)
    ad = {"Test":["test 1"], "p_value": [0.1], "bonf_value": [0.05],"bonf_significant" :[False],"bh_value": [0.05], "bh_significant":[False] }
    adf = pd.DataFrame(data = ad)
    adf = adf[['Test','p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    test =  p_methods(data =df,pv_index = "p_value", alpha =0.05)
    test = test[['Test','p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    d = {"Test":["test 1", "test 2"], "p_value": [0.01,0.03] }
    df = pd.DataFrame(data = d)
    ad = {"Test":["test 1", "test 2"], "p_value": [0.01,0.03], "bonf_value": [0.025,0.025],"bonf_significant" :[True,False],"bh_value": [0.025,0.05], "bh_significant":[True, True] }
    adf = pd.DataFrame(data = ad)
    adf = adf[['Test','p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    test =  p_methods(data =df, pv_index = "p_value", alpha =0.05)
    test = test[['Test','p_value','bh_value','bh_significant','bonf_value','bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

	###formatting tests
	# # https://github.com/datalyze-solutions/pandas-qt/blob/master/tests/test_DataFrameModel.py
	# assert not data.empty
	# assert data is dataFrame


###Plotting tests

def test_p_qq():
    """
    The purpose of this test is evaluating if the matplotlib object created with p_qq has the correct layers compared to the required
    plot. The test will cover the same things we checked with R:

    - The output is a matplotlib object.
    - The axis labels are correct. In this case if the labels are "Observed -log(p)" and "Expected -log(p)".
    - The chart type used is correct. In this case, if it is a scatter plot combined with a line.
    - The series used for plotting are the correct ones. "theoretical_pvalues" and "theoretical_pvalues".

    ## We couldn't find a way to extract information from the axes on the matplotlib object. With R, everything is stored
    ## on a list. We will get deeper this week to solve this issue and add the test announced before.
    """

    ##fig = p_qq(X,y)
    ##assert type(fig) == matplotlib.figure.Figure, "the object includes a matplotlib figure "

def test_p_plot():
    """
    The purpose of this test is evaluating if the matplotlib object created with p_plot has the correct layers compared to the required
    plot. The test will cover the same things we checked with R:

    - The output is a matplotlib object.
    - The axis labels are correct. In this case if the labels are "p(k)" and "k".
    - The chart type used is correct. In this case, if it is a scatter plot combined with two lines.
    - The series used for plotting are the correct ones. "pvalue" and "k".

    ## We couldn't find a way to extract information from the axes on the matplotlib object. With R, everything is stored
    ## on a list. We will get deeper this week to solve this issue and add the test announced before.
    """

    ##fig = p_plot(X,y)
    ##assert type(fig) == matplotlib.figure.Figure, "the object includes a matplotlib figure "
