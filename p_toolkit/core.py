import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


###exceptions
class ProbabilityError(Exception):
    """An error that indicates that all probabilities are not between 0 and 1."""

def p_methods(data, pv_index=0, alpha = 0.05):
    """
    A summary dataframe with columns for the p-values, adjusted p-values for both Bonferroni and
    Benjamini-Hochberg (BH), adjusted significancelevel for Bonferroni and the critical value for BH

   Args:
        - data: dataframe or array containing at least a column of p-values to be adjusted
        - pv_index (int): original p-value column index from existing input dataframe
        - alpha (int): significance level as a value between 0 and 1

   Returns:
        Dataframe: appends to input dataframe both adjusted p-values and significance levels (Bonferroni and BH)
        in ascending raw p-value order.Includes following columns:
            - p_value: is the original raw p-value.
            - bh_value: Benjamini-Hochberg (BH) critical value
            - bH_significant (bool): True if significant p-value or False if not
            - bonf_value: Bonferroni adjusted significance level (same for all)
            - bonf_significant (bool): True if significant p-value or False if not
    """

    #### Raise an error for an impossible alpha value
    if (alpha>= 1) or (alpha<= 0):
        raise ProbabilityError("alpha needs to be between 0 and 1!")

    ####if it's a pd.dataframe, rename to col header
    if isinstance(data, pd.DataFrame):
        if isinstance(pv_index, int):
            pv_index = data.columns.get_values()[pv_index]
        data =data.rename(columns ={pv_index: "p_value"})
    ###or make a vector a pd.dataframe
    else:
        data = pd.DataFrame({"p_value": data})

    if (data["p_value"].max()> 1) or (data["p_value"].max()< 0):
        raise ProbabilityError("One or more p-values is not between 0 and 1!")

    ###set the size of the data
    m = data.shape[0]

    ###find the smallest p_value st. p<k*alpha/m (BH method):
    ##set the rank, making ties the minimum
    df =data.sort_values(by=["p_value"])
    df["rank"]=round(df.rank(axis=0, method = 'min')["p_value"])
    df["bh_value"] = alpha*df["rank"]/m
    df_temp = df
    df_temp["bh_sig"]= np.where(df_temp["p_value"] <= df_temp["bh_value"], True, False)
    df_temp =df_temp[df_temp["bh_sig"]==True]

    ###the maximum true value

    if len(df_temp["bh_sig"]) == 0:
        max_true = 0
    else:
        max_true = max(df_temp["rank"])

    ####Back to cool dataframe work!
    df["bh_significant"]=np.where(df["rank"]<=max_true, True, False)
    df["bonf_value"] = alpha/m
    df["bonf_significant"] = np.where(df["p_value"]<=df["bonf_value"], True, False)
    df = df.drop(['rank'], axis=1)
    df = df.drop(['bh_sig'], axis=1)

    return(df)


def p_adjust(data, pv_index=0, method='bonf', alpha=0.05):
    """
    A summary dataframe with columns for the p-values, adjusted p-values for both Bonferroni and
    Benjamini-Hochberg (BH), adjusted significancelevel for Bonferroni and the critical value for B

   Args:
        - data: dataframe or array containing at least a column of p-values to be adjusted
        - pv_index (int): original p-value column index from existing input dataframe
        - method: adjustment method to use. Use 'bh' or 'fdr' for Benjamini-Hochberg (BH), and 'bonf' or 'bonferroni' for Bonferroni.
        - alpha (int): significance level as a value between 0 and 1

   Returns:
        Dataframe: appends to input dataframe both adjusted p-values and significance levels (Bonfe
        in ascending raw p-value order.Includes following columns:
        - p_value: is the original raw p-value.
        - adjusted: is the corrected p-value after the adjustment method used.
    """

    if isinstance(data, pd.DataFrame):
        if isinstance(pv_index, int):
            pv_index = data.columns.get_values()[pv_index]
        data =data.rename(columns ={pv_index: "p_value"})
        ## error for non-numeric data frame column
        if not (np.issubdtype(data['p_value'].dtypes, np.number)):
            raise TypeError("Please ensure you have specified the column index of numeric p-values.")
    else:
        data = pd.DataFrame({"p_value": data})
        # set the size of the data

    ##added an exception
    if (data["p_value"].max()> 1) or (data["p_value"].max()< 0):
        raise ProbabilityError("One or more p-values is not between 0 and 1!")

    m = data.shape[0]

    # sort p-values
    df = data.sort_values(by=['p_value'])
    df["rank"] = round(df.rank(axis=0, method='min')["p_value"])
    df["bh_value"] = alpha * df["rank"] / m

    ### generate final data frame
    df["bonf_pvalue"] = np.where(df['p_value'] * m < 1, df['p_value'] * m, 1)
    df["bh_pvalue"] = df['p_value'] / df["rank"]  * m


    if method == 'bh' or method == 'fdr':
        df["adjusted"] = df['p_value'] /  df["rank"] * m
        return (df[['p_value', 'adjusted']])
    if method == 'bonf' or method == 'bonferroni':
        df["adjusted"] = df['p_value'] * m
        return (df[['p_value', 'adjusted']])
    else:
        raise ValueError("Method should be set as 'bonf' or 'bh' corrections")


def p_plot(data,pv_index=0,alpha=0.05):
    """
    This function plots all the p-values in ascending order and compares them with two lines, one representing
    the BH cutoff point and another one the Bonferroni cutoff.

    Args:
        - data: a Pandas dataframe or an array that contains the p-values that we want to adjust.
        - pv_index: (only when the input is a pandas dataframe )this argument determines the column index that contains the p-values.
        - alpha: is the signficance level for cutting off p-values.

    Returns:
        - plot: a matplotlib object with the p-values and both cut-off lines.
    """
    ####if it's a pd.dataframe, rename to col header
    if isinstance(data, pd.DataFrame):
        if isinstance(pv_index, int):
            pv_index = data.columns.get_values()[pv_index]
        data =data.rename(columns ={pv_index: "p_value"})
        if not (np.issubdtype(data['p_value'].dtypes, np.number)):
            raise TypeError("Please ensure you have specified the column index of numeric p-values.")
    ###or make a vector a pd.dataframe
    else:
        data = pd.DataFrame({"p_value": data})

    if (data["p_value"].max()> 1) or (data["p_value"].max()< 0):
        raise ProbabilityError("One or more p-values is not between 0 and 1!")

    m = len(data['p_value'])

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

def p_qq(data,pv_index=0,alpha=0.05):
    """
    This function plots all the raw p-values and compares them with a theoretical uniform distribution using a
    qq plot. This plot is created with a negative log scale, letting
    us visualize all the p-values, independent of their small magnitudes. The p-values deviated from the diagonal line,
    are the ones that are significant.

    Args:
        - data: a Pandas dataframe or an array that contains the p-values that we want to adjust.
        - pv_index: (only when the input is a pandas dataframe )this argument determines the column index that contains the p-values.
        - alpha: is the signficance level for cutting off p-values.

    Returns:
        - plot: a matplotlib object with the p-values and both cut-off lines.
    """
    ####if it's a pd.dataframe, rename to col header
    if isinstance(data, pd.DataFrame):
        if isinstance(pv_index, int):
            pv_index = data.columns.get_values()[pv_index]
        data =data.rename(columns ={pv_index: "p_value"})
        if not (np.issubdtype(data['p_value'].dtypes, np.number)):
            raise TypeError("Please ensure you have specified the column index of numeric p-values.")
    ###or make a vector a pd.dataframe
    else:
        data = pd.DataFrame({"p_value": data})

    if (data["p_value"].max()> 1) or (data["p_value"].max()< 0):
        raise ProbabilityError("One or more p-values is not between 0 and 1!")

    m = len(data['p_value'])

    data['log_transf'] = -np.log10(data['p_value'])
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
