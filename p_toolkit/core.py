import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def p_methods(data, pv_index=0, alpha = 0.05):
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

    ####if it's a pd.dataframe, rename to col header
    if isinstance(data, pd.DataFrame):
        data.rename({pv_index: "p_value"})
    ###or make a vector a pd.dataframe
    else:
        data = pd.DataFrame({"p_value": data})

    ###set the size of the data
    m = data.shape[0]

    ###find the smallest p_value st. p<k*alpha/m (BH method):
    ##set the rank, making ties the minimum
    df =data.sort_values(by=['p_value'])
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
        - data (dataframe): dataframe containing at least a column of p-values to be adjusted      
        - pv_index (int): original p-value column index from existing input dataframe              
        - alpha (int): significance level as a value between 0 and 1                               
                                                                                                   
   Returns:                                                                                        
        Dataframe: appends to input dataframe both adjusted p-values and significance levels (Bonfe
        in ascending raw p-value order.Includes following columns:                                 
            - bonf_val (int): Bonferroni adjusted significance level (same for all)                
            - Bonf_significant (bool): True if significant p-value or False if not                 
            - bh_val (int): Benjamini-Hochberg (BH) critical value                                 
            - BH_significant (bool): True if significant p-value or False if not                   
    """                                                                                            
                                                                                                   
    #     ####if it's a pd.dataframe, rename to col header                                         
    #     if isinstance(data, pd.DataFrame):                                                       
    #         data.rename({pv_index: "p_value"})                                                   
    #         if np.issubdtype(data['p_value'].dtypes, np.number):                                 
                                                                                                   
    #     ###or make a vector a pd.dataframe                                                       
    #     else:                                                                                    
    #         data = pd.DataFrame({"p_value": data})  
    
    if isinstance(data, pd.DataFrame):                                                             
        data.rename({pv_index: "p_value"})                                                         
        ## error for non-numeric data frame column                                                 
        if not (np.issubdtype(data['p_value'].dtypes, np.number)):                                 
            raise TypeError("Please ensure you have specified the column index of numeric p-values.")
    else:                                                                                          
        data = pd.DataFrame({"p_value": data})                                                     
        # set the size of the data                                                                 
                                                                                                   
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
                            

def p_plot(data):
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

def p_qq(data):
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

def p_bh_helper(p_values,alpha=0.05):
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

    #Sort p-values
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
