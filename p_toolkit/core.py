import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def p_methods():
    """
    A summary dataframe with columns for the p-values, adjusted p-values for both Bonferroni and
    Benjamini-Hochberg (BH), adjusted significancelevel for Bonferroni and the critical value for BH

   Args:
        - data (dataframe): dataframe containing at least a column of p-values to be adjusted
        - pv_index (int): original p-value column index from existing input dataframe
        - alpha (int): significance level as a value between 0 and 1

   Returns:
        Dataframe: appends to input dataframe both adjusted p-values and significance levels (Bonferroni and BH)
        in ascending raw p-value order.Includes following columns:
            - bonf_val (int): Bonferroni adjusted significance level (same for all)
            - Bonf_significant (bool): True if significant p-value or False if not
            - bh_val (int): Benjamini-Hochberg (BH) critical value
            - BH_significant (bool): True if significant p-value or False if not
    """
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

    m = len(data['p_value'])
    alpha = data['value'][0]

    data = data.sort_values('p_value',ascending=True)
    data['rank'] = np.arange(1,len(data['p_value'])+1)
    data['critical_value'] = data['rank']*alpha/m

    fig = plt.clf()
    plt.scatter(data['rank'],data['p_value'],color='black')
    plt.axhline(y=alpha,label='Bonferroni')
    plt.plot(data['rank'],data['critical_value'],label='BH',color='red')
    plt.legend()
    plt.title("Bonferroni vs BH")
    plt.xlabel("Rank")
    plt.ylabel("p(k)")
    return fig

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
    m = len(data['p_value'])
    alpha = data['value'][0]

    data['log_transf'] = -np.log10(sample_df['p_value'])
    data = data.sort_values('p_value',ascending=True)
    data['rank'] = np.arange(1,len(data['p_value'])+1)
    data['log_exp'] = -np.log10(data['rank']/m)

    fig = plt.clf()
    plt.scatter(data['log_exp'],data['log_transf'],color='black')
    plt.plot(data['log_exp'],data['log_exp'])
    plt.title("QQ")
    plt.xlabel("Expected -log10(p)")
    plt.ylabel("Observed -log10(p)")
    return fig

def p_bh_helper():
    """
    Applies Benjamini-Hochberg (BH) correction to the original p-values

    Args:
        - p_values (int): original p-value column index from existing input dataframe
        - alpha (int): significance level or false discovery rate as a value between 0 and 1

    Returns:
        - Vector: returns the Benjamini-Hochberg (BH) adjusted p-value
    """
	# initialize parameters
	q = alpha

	# Sort p-values
	p_values = np.sort(p_values)
	n = len(p_values)
	i = np.arange(1, n+1)

	# Adjusted p-values that must be below the significance level
	adj_bh = p_values * n / rank

	# Rank to handle equal p-values
	helper_df = pd.DataFrame(p_values)
	rank = round(helper_df.rank(axis=0, method = 'min')[0])

    bh_df = pd.DataFrame()
	bh_df['index'] = i
	bh_df['rank'] = rank
	bh_df['p_value'] = p_values
	bh_df['adjusted_pval'] = adj_bh

	return bh_df

def p_bonferroni_helper():
    """
    Applies Bonferroni correction to the original p-values

    Args:
        - pvals (int): original p-value column index from existing input dataframe
        - alpha (int): significance level as a value between 0 and 1

    Returns:
        - vector: returns the Bonferroni adjusted p-value
    """
	# vector output
	adj_bonf = alpha / pvals

	# dataframe output
	bonf_df = pd.DataFrame()
	bonf_df['p_value'] = p_values
	bonf_df['adjusted_pval'] = adj_bonf

	return bonf_df
