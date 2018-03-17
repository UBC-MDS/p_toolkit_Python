## Required packages

import os
import sys
import pytest
import numpy as np
import pandas as pd

import matplotlib as plt
plt.use('Agg')

sys.path.insert(0, os.path.abspath("../p_toolkit"))

from core import *


# -----------------------------------------------------------------------------
# p_adjust tests
# -----------------------------------------------------------------------------

def test_p_adjust_wrong_method_string():
    """
    Testing for entering an invalid string as a method.
    """

    try:
        d = [0.02,0.3]
        df = pd.DataFrame(data=d)
        p_adjust(data=df,  pv_index=0, method='bonferrro', alpha=0.05)
    except(ValueError):
        assert True
    else:
        assert False

def test_p_adjust_vector_1_value_bonf():
    """
    Testing p_adjust with a vector of 1 value and using bonferroni method.
    """

    d = {"p_value": [0.07], "adjusted": [0.07]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07], method="bonf")), "p_adjust 1 values vector for bonferoni"

def test_p_adjust_vector_1_value_bh():
    """
    Testing p_adjust with a vector of 1 value and using bh method.
    """

    d = {"p_value": [0.07], "adjusted": [0.07]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07], method="bh")), "p_adjust 1 values vector for bh"

def test_p_adjust_vector_2_values_bonf():
    """
    Testing p_adjust with a vector of 2 values and using bonferroni method.
    """

    d = {"p_value": [0.07, 0.2], "adjusted": [0.14, 0.4]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07, 0.2], method="bonf")), "p_adjust 2 values vector for bonferoni"

def test_p_adjust_vector_2_values_bh():
    """
    Testing p_adjust with a vector of 2 values and using bh method.
    """

    d = {"p_value": [0.07, 0.2], "adjusted": [0.14, 0.2]}
    df = pd.DataFrame(data=d)
    df = df[["p_value", "adjusted"]]
    assert df.equals(p_adjust(data=[0.07, 0.2], method="bh")), "p_adjust 2 values vector value for bh"

def test_p_adjust_character_col_index():
    """
    Testing for error string when col index of dataframe contains character values
    """

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

def test_p_methods_errors_probabilities_less_than_zero():
    """
    Testing for errors with invalid probabilities less than zero.
    """

    try:
        err_str = {"p_value": [0.5,.3,-.02]}
        p_methods((err_str), 0, 0.01)
    except(TypeError):
        assert True
    else:
        assert False

def test_p_methods_errors_alpha_less_than_zero():
    """
    Testing for errors with invalid alpha less than zero.
    """

    try:
        err_str = {"p_value": [0.5,.3,.02]}
        p_methods((err_str), 0, -.01)
    except(ProbabilityError):
        assert True
    else:
        assert False

def test_p_methods_errors_alpha_greater_than_one():
    """
    Testing for errors with invalid alpha greater than one.
    """

    try:
        err_str = {"p_value": [0.5,.3,.02]}
        p_methods((err_str), 0, 3)
    except(ProbabilityError):
        assert True
    else:
        assert False

def test_p_methods_1_value_vector_false_signficance():
    """
    Testing 1 value vector as input for p_methods with false significance.
    """

    d = {"p_value": [0.07], "bonf_value": [0.05], "bonf_significant": [False], "bh_value": [0.05],
         "bh_significant": [False]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=[0.07], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_methods 1 value vector, FALSE"

def test_p_methods_1_value_vector_true_signficance():
    """
    Testing 1 value vector as input for p_methods with true significance.
    """

    d = {"p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
         "bh_significant": [True]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=[0.01], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_methods 1 value vector, TRUE"

def test_p_methods_2_value_vector():
    """
    Testing 2 values vector as input for p_methods.
    """

    d = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03], "bonf_value": [0.025, 0.025],
         "bonf_significant": [True, False], "bh_value": [0.025, 0.05], "bh_significant": [True, True]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=[0.01, 0.03], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_methods 2 values vector "

def test_p_methods_1_value_dataframe_true_signficance():
    """
    Testing 1 values dataframe with true signficance.
    """

    d = {"Test": ["test 1"], "p": [0.01]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
          "bh_significant": [True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

def test_p_methods_1_value_dataframe_false_signficance():
    """
    Testing 1 values dataframe with false signficance.
    """

    d = {"Test": ["test 1"], "p_value": [0.1]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.1], "bonf_value": [0.05], "bonf_significant": [False], "bh_value": [0.05],
          "bh_significant": [False]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

def test_p_methods_2_values_dataframe():
    """
    Testing 2 values dataframe.
    """

    d = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03], "bonf_value": [0.025, 0.025],
          "bonf_significant": [True, False], "bh_value": [0.025, 0.05], "bh_significant": [True, True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_methods(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_methods 2 values dataframe "

def test_p_methods_empty_data():
    """
    Testing not empty data.
    """
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
        p_plot(p_methods(data=[0.01], alpha=0.05))
    except(SyntaxError):
        assert False
    else:
        assert True

def test_p_qq_integration_test():
    """
    Integration test using the p_qq function with p_methods as input.
    """
    try:
        p_qq(p_methods(data=[0.01], alpha=0.05))
    except(SyntaxError):
        assert False
    else:
        assert True
