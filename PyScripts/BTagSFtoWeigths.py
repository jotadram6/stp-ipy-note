def W0n(SF):
    "SF: list of scale factors"
    W=1
    for i in xrange(len(SF)):
        W*=(1-SF[i])
    return W

def W1n(SF):
    "SF: list of scale factors"
    TW=0
    for j in xrange(len(SF)):
        W=1
        for i in xrange(len(SF)):
            if i==j: continue
            W*=(1-SF[i])
        TW+=W*SF[j]
    return TW

def W2n(SF):
    "SF: list of scale factors"
    TW=0
    for j in xrange(len(SF)):
        W=1
        for i in xrange(len(SF)):
            if i==j: continue
            W*=SF[i]
        TW+=W*(1-SF[j])
    return TW

#Second definition tested, first definition changes (1-SF[j])->SF[j] and SF[k]->(1-SF[k])
#def W2n(SF):
#    "SF: list of scale factors"
#    TTW=0
#    for k in xrange(len(SF)):
#        TW=0
#        for j in xrange(len(SF)):
#            if j==k: continue
#            W=1
#            for i in xrange(len(SF)):
#                if i==j or i==k: continue
#                W*=SF[i]
#            TW+=W*(1-SF[j])
#        TTW+=TW*SF[k]
#    return TTW

def TotalW(SF):
    "SF: list of scale factors"
    return 1-W0n(SF)-W1n(SF)-W2n(SF)
