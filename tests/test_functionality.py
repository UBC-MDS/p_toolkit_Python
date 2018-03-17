## Required packages

import os
import sys
import pytest

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath("../p_toolkit"))

from core import *


###Functionality tests

###p_adjust functionality
def test_p_adjust():
    """
    The purpose of this test is evaluating the p_adjust with more real world data using Pandas dataframes under
    different environments.
    """

    ##basic vector functionality"
    d = {"p_value": [0.07], "adjusted": [0.07]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07], method="bonf")), "p_adjust 1 values vector for bonferoni"
    assert df.equals(p_adjust(data=[0.07], method="bh")), "p_adjust 1 values vector for bh"


    d = {"p_value": [0.07, 0.2], "adjusted": [0.14, 0.4]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07, 0.2], method="bonf")), "p_adjust 2 values vector for bonferoni"

    d = {"p_value": [0.07, 0.2], "adjusted": [0.14, 0.2]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07, 0.2], method="bh")), "p_adjust 2 values vector value for bh"

    # error string col index of dataframe contains character values
    try:
        err_str = {"p_value": ['str']}
        p_adjust((err_str), 0, "bonf", 0.05)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_adjust_errors_probabilities_greater_than_one():
    """
    Testing for errors with invalid probabilities greater than one
    """
    try:
        err_str = {"p_value": [0.5,3,.02]}
        p_adjust((err_str), 0, "bonf", 0.05)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_adjust_errors_probabilities_less_than_zero():
    """
    Testing for errors with invalid negative probabilities
    """
    try:
        err_str = {"p_value": [0.5,.3,-.02]}
        p_adjust((err_str), 0, "bh", 0.05)
    except(TypeError):
        assert True
    else:
        assert False

# -----------------------------------------------------------------------------
# p_methods tests
# -----------------------------------------------------------------------------

def test_p_methods_errors_probabilities_greater_than_one():
    """
    Testing for errors with invalid probabilities greater than one.
    """
    try:
        err_str = {"p_value": [0.5,3,.02]}
        p_methods((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

    try:
        err_str = {"p_value": [0.5,.3,-.02]}
        p_methods((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

    try:
        err_str = {"p_value": [0.5,.3,.02]}
        p_methods((err_str), 0, -.01)
    except(ProbabilityError):
        assert True
    else:
        assert False

    try:
        err_str = {"p_value": [0.5,.3,.02]}
        p_methods((err_str), 0, 3)
    except(ProbabilityError):
        assert True
    else:
        assert False

def test_p_methods():
    """
    The purpose of this test is evaluating the p_adjust with more real world data using Pandas dataframes under
    different environments.
    """
    d = {"p_value": [0.07], "bonf_value": [0.05], "bonf_significant": [False], "bh_value": [0.05],
         "bh_significant": [False]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=[0.07], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_methods 1 value vector, FALSE"

    d = {"p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
         "bh_significant": [True]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=[0.01], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_methods 1 value vector, TRUE"

    d = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03], "bonf_value": [0.025, 0.025],
         "bonf_significant": [True, False], "bh_value": [0.025, 0.05], "bh_significant": [True, True]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=[0.01, 0.03], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_methods 2 values vector "

    ###dataframe tests
    d = {"Test": ["test 1"], "p_value": [0.01]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
          "bh_significant": [True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    d = {"Test": ["test 1"], "p": [0.01]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
          "bh_significant": [True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index=1, alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    d = {"Test": ["test 1"], "p": [0.01]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
          "bh_significant": [True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    d = {"Test": ["test 1"], "p_value": [0.1]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.1], "bonf_value": [0.05], "bonf_significant": [False], "bh_value": [0.05],
          "bh_significant": [False]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    d = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03], "bonf_value": [0.025, 0.025],
          "bonf_significant": [True, False], "bh_value": [0.025, 0.05], "bh_significant": [True, True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

    # data is not empty
    with pytest.raises(TypeError):
        p_methods()

# -----------------------------------------------------------------------------
# p_qq tests
# -----------------------------------------------------------------------------

def test_p_qq_errors_probabilities_less_than_zero():
    """
    Testing for errors with probabilities less than zero.
    """

    # error string col index of dataframe contains character values
    try:
        err_str = {"p_value": ['str']}
        p_adjust((err_str), 0, "bonf", 0.05)
    except(TypeError):
        assert True
    else:
        assert False


def test_p_qq_errors_probabilities_less_than_zero():
    """
    Testing for errors with probabilities less than zero.
    """
    try:
        err_str = {"p_value": [0.5,3,.02]}
        p_qq((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_qq_errors_probabilities_greater_than_one():
    """
    Testing for errors with probatilities greater than one.
    """

    try:
        err_str = {"p_value": [0.5,.3,-.02]}
        p_qq((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

# -----------------------------------------------------------------------------
# p_plot tests
# -----------------------------------------------------------------------------

def test_p_plot_errors_probabilities_greater_than_one():
    """
    Testing for errors with invalid probabilities greater than one.
    """
    try:
        err_str = {"p_value": [0.5,3,.02]}
        p_plot((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_plot_errors_probabilities_less_than_zero():
    """
    Testing for errors with invalid negative probabilities.
    """

    try:
        err_str = {"p_value": [0.5,.3,-.02]}
        p_plot((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_plot_errors_alpha_less_than_zero():
    """
    Testing for errors with invalid negative alpha.
    """
    try:
        err_str = {"p_value": [0.5,.3,.02]}
        p_plot((err_str), 0, -.01)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_plot_errors_alpha_greater_than_one():
    """
    Testing for errors with invalid alpha greater than one.
    """
    try:
        err_str = {"p_value": [0.5,.3,.02]}
        p_plot((err_str), 0, 3)
    except(TypeError):
        assert True
    else:
        assert False

# -----------------------------------------------------------------------------
# Integration tests
# -----------------------------------------------------------------------------

def test_p_plot_integration_test():
    """
    Integration test using the p_plot function with p_methods as input.
    """
    try:
        p_plot(p_methods(list(np.linspace(0.01,1,30))))
    except(SyntaxError):
        assert False
    else:
        assert True

def test_p_qq_integration_test():
    """
    Integration test using the p_qq function with p_methods as input.
    """
    try:
        p_qq(p_methods(list(np.linspace(0.01,1,30))))
    except(SyntaxError):
        assert False
    else:
        assert True
