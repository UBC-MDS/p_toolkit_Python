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
    pass

def p_qq():
    pass

def p_matrix():
    pass

def p_summary():
    pass



import pytest

def test_p_methods():
    assert
