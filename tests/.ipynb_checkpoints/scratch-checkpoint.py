def test_p_adjust():
    """
    The purpose of this test is evaluating the p_adjust with more real world data using Pandas dataframes under
    different environments.
    """
    d = {"p_value": [0.07], "bonf_value": [0.05], "bonf_significant": [False], "bh_value": [0.05],
         "bh_significant": [False]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_adjust(data=[0.07], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_adjust 1 value vector, FALSE"

    d = {"p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
         "bh_significant": [True]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_adjust(data=[0.01], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_adjust 1 value vector, TRUE"

    d = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03], "bonf_value": [0.025, 0.025],
         "bonf_significant": [True, False], "bh_value": [0.025, 0.05], "bh_significant": [True, True]}
    df = pd.DataFrame(data=d)
    df = df[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_adjust(data=[0.01, 0.03], alpha=0.05)
    test = test[['p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(df), "p_adjust 2 values vector "

    ###dataframe tests
    d = {"Test": ["test 1"], "p_value": [0.01]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.01], "bonf_value": [0.05], "bonf_significant": [True], "bh_value": [0.05],
          "bh_significant": [True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_adjust(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_adjust 2 values dataframe "

    d = {"Test": ["test 1"], "p_value": [0.1]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1"], "p_value": [0.1], "bonf_value": [0.05], "bonf_significant": [False], "bh_value": [0.05],
          "bh_significant": [False]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_adjust(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_adjust 2 values dataframe "

    d = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03]}
    df = pd.DataFrame(data=d)
    ad = {"Test": ["test 1", "test 2"], "p_value": [0.01, 0.03], "bonf_value": [0.025, 0.025],
          "bonf_significant": [True, False], "bh_value": [0.025, 0.05], "bh_significant": [True, True]}
    adf = pd.DataFrame(data=ad)
    adf = adf[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    test = p_adjust(data=df, pv_index="p_value", alpha=0.05)
    test = test[['Test', 'p_value', 'bh_value', 'bh_significant', 'bonf_value', 'bonf_significant']]
    assert test.equals(adf), "p_adjust 2 values dataframe "

    # data is not empty
    with pytest.raises(TypeError):
        p_adjust()