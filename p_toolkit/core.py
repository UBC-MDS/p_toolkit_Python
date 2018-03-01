def p_methods():
    pass

def p_adjust():
    """
    This function executes an specific p-value adjustment method.

    Args:
        - data: a Pandas dataframe or a 1-d Numpy array.
        - col: if the input is a dataframe, col refers to the column name of the dataframe that has the p-values.
        - alpha: significance level for both methods.
        - method: method used for the adjustment ("bh" or "bonf")

    Returns:
        - data frame: data frame with the following columns:
            raw_p_value: original p-values.
            adjusted_p_value: p-values after the adjustment.
            signficant: boolean values determining if each p-value is significant.
            critical_value: it's the calculated critical value to compare with the cut-off.
    """
    pass

def p_plot():
    """
    This function plots all the p-values in ascending order and compares them with two lines, one representing
    the BH cutoff point and another one the Bonferroni cutoff.

    Args:
        - ad_object: the Pandas dataframe output from the p_methods function.

    Returns:
        - plot: a matplotlib object with the p-values and both cut-off lines.
    """
    pass

def p_qq():
    """
    This function plots all the raw p-values and compares them with a theoretical uniform distribution using a
    qq plot. This plot is created with a negative log scale, letting
    us visualize all the p-values, independent of their small magnitudes. The p-values deviated from the diagonal line,
    are the ones that are significant.

    Args:
        - ad_object: the Pandas dataframe output from the p_methods function.

    Returns:
        - plot: a matplotlib object with the qq plot. 
    """
    pass

def p_matrix():
    pass

def p_summary():
    pass



import pytest

def test_p_methods():
    assert
