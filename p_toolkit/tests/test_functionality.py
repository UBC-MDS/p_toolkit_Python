###functionality tests

def test_p_bonnferoni_helper():
    ###basic tests
    assert p_bonnferoni_helper([0.07])== [0.07], "a single value doesn't change under bonnferoni"
    assert p_bonnferoni_helper([0.07,0.2])== [0.14,0.4], "p_bonnferoni_helper((0.07,0.2))== (0.14,0.4)"
    assert p_bonnferoni_helper([0.2,0.07])== [0.4,0.14], "p_bonnferoni_helper((0.2,0.07))== (0.4,0.14)"
    assert p_bonnferoni_helper([0.01, 0.02, 0.03])==[0.03, 0.06,0.09], "p_bonnferoni_helper((0.01, 0.02, 0.03))==(0.03, 0.06,0.09)"

  ### all values are between 0 and 1
    with pytest.raises(ValueError):
          p_bonferoni_helper([-3])
          p_bonferoni_helper([-3, .05])
          p_bonferoni_helper([.05, -3])
          p_bonferoni_helper([8])
          p_bonferoni_helper([8, .05])
          p_bonferoni_helper([.05,8])

###maximum return is 1
    assert p_bonnferoni_helper([0.01, 0.7])==[0.02,1], "test_p_bonnferoni_helperhas max of 1"


def test_p_bonn():
     assert p_bh_helper([0.07])== [0.07], "a single value doesn't change under bh"
     assert p_bh_helper([0.07,0.2])== [0.14,0.2], "p_bh_helper((0.07,0.2))== (0.14,0.2)"
     assert p_bh_helper([0.2,0.07])== [0.2,0.14], "p_bh_helper((0.2,0.07))== (0.2,0.14)"
     assert p_bh_helper([0.01, 0.02, 0.03])==[0.03, 0.03,0.03], "p_bh_helper((0.01, 0.02, 0.03))==(0.03, 0.03,0.03)"
     assert p_bh_helper([0.02, 0.03, 0.01])==[0.03, 0.03,0.03], "p_bh_helper((0.02, 0.03, 0.01))==(0.03, 0.03,0.03)"
     assert p_bh_helper([.02,.12,.24,.56,.6])==[0.1,0.6, 0.4,0.7, 0.6], "p_bh_helper((.02,.12,.24,.56,.6))==(0.1,0.6, 0.4,0.7, 0.6)"
     assert p_bh_helper([0.04, 0.04, 0.04,0.08])==[0.16,0.16,0.16,0.08], "p_bh_helper treats rep[eated values correctly"

### all valid probabilities
     with pytest.raises(ValueError):
         p_bh_helper([-3])
         p_bh_helper([-3, .05])
         p_bh_helper([.05, -3])
         p_bh_helper([8])
         p_bh_helper([8, .05])
         p_bh_helper([.05,8])


####p_adjust functionality
def test_p_adjust():
    ##basic vector functionality"
    d = { "p_value": [0.07], "adjusted"= [0.07]}
    df = pd.DataFrame(data = d)
    assert p_adjust(data =[0.07], method = "bonnferoni")== df, "p_adjust 1 value vector for bonnferoni"
    assert p_adjust(data =[0.07], method = "bh")== df, "p_adjust single value vector for bh"

    d = { "p_value": [0.07,0.2], "adjusted"= [0.14,0.4]}
    df = pd.DataFrame(data = d)
    assert p_adjust(data =[0.07,0.2], method = "bonnferoni")== df, "p_adjust 2 values vector for bonnferoni"

    d = { "p_value": [0.07,0.2], "adjusted"= [0.14,0.2]}
    df = pd.DataFrame(data = d)
    assert p_adjust(data =[0.07,0.2], method = "bh")== df, "p_adjust 2 values vector value for bh"

    ###basic dataframe fuinctionality
    d = {"test":["test 1"], "p_value": [0.05]}
    df = pd.DataFrame(data = d)
    ad = {"test":["test 1"], "p_value": [0.05],"adjusted"= [0.05]}
    adf=pd.DataFrame(data =ad)
    assert p_adjust(data =df, method = "bonnferoni")==adf, "bonferroni single value df under p_adjust"
    assert p_adjust(data =df, method = "bh")==adf, "bh single value df under p_adjust"

    d = {"test":["test 1", "test 2"], "p_value": [0.07,0.2]}
    df = pd.DataFrame(data = d)
    ad = {"test":["test 1", "test 2"], "p_value": [0.07,0.2],"adjusted"= [0.14, 0.4]}
    adf=pd.DataFrame(data =ad)
    assert p_adjust(data =df, method = "bonnferoni")==adf, "bonferroni 2 value df under p_adjust"

    ad = {"test":["test 1", "test 2"], "p_value": [0.07,0.2],"adjusted"= [0.14, 0.2]}
    adf=pd.DataFrame(data =ad)
    assert p_adjust(data =df, method = "bh")==adf, "bh 2 value df under p_adjust"


def test_p_methods():
    ###basic vector fuinctionality
    d = { "p_value": [0.07], "Bonnferoni_critical_value"= [0.05],"Bonnferoni_reject" =[False],"BH_critical_value"= [0.05], "BH_reject"=[False] }
    df = pd.DataFrame(data = d)
    assert p_methods(data =[0.07], alpha =0.05)== df, "p_methods 1 value vector, FALSE"

    d = { "p_value": [0.01], "Bonnferoni_critical_value"= [0.05],"Bonnferoni_reject" =[True],"BH_critical_value"= [0.05], "BH_reject"=[True] }
    df = pd.DataFrame(data = d)
    assert p_methods(data =[0.01], alpha =0.05)== df, "p_methods 1 value vector, TRUE"

    d = {"Test":["test 1", "test 2"], "p_value": [0.01,0.03], "Bonnferoni_critical_value"= [0.025,0.025],"Bonnferoni_reject" =[True,False],"BH_critical_value"= [0.025,0.05], "BH_reject"=[True, True] }
    df = pd.DataFrame(data = d)
    assert p_methods(data =[0.01,0.03], alpha =0.05)== df, "p_methods 2 values vactor "


    ###dataframe tests
    d = {"Test":["test 1"], "p_value": [0.01] }
    df = pd.DataFrame(data = d)
    ad = {"Test":["test 1"], "p_value": [0.01], "Bonnferoni_critical_value"= [0.05],"Bonnferoni_reject" =[True],"BH_critical_value"= [0.05], "BH_reject"=[True] }
    adf = pd.DataFrame(data = ad)
    assert p_methods(data =df, column = "p_value", alpha =0.05)== adf, "p_methods 2 values dataframe "

    d = {"Test":["test 1"], "p_value": [0.1] }
    df = pd.DataFrame(data = d)
    ad = {"Test":["test 1"], "p_value": [0.1], "Bonnferoni_critical_value"= [0.05],"Bonnferoni_reject" =[False],"BH_critical_value"= [0.05], "BH_reject"=[False] }
    adf = pd.DataFrame(data = ad)
    assert p_methods(data =df,column = "p_value", alpha =0.05)== adf, "p_methods 2 values dataframe "

    d = {"Test":["test 1", "test 2"], "p_value": [0.01,0.03] }
    df = pd.DataFrame(data = d)
    ad = {"Test":["test 1", "test 2"], "p_value": [0.01,0.03], "Bonnferoni_critical_value"= [0.025,0.025],"Bonnferoni_reject" =[True,False],"BH_critical_value"= [0.025,0.05], "BH_reject"=[True, True] }
    adf = pd.DataFrame(data = ad)
    assert p_methods(data =df, column = "p_value", alpha =0.05)== adf, "p_methods 2 values dataframe "
