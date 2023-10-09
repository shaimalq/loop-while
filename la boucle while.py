marrakech=1000000
agadir=500000
nbr=0
while marrakech>agadir:
    marrakech=marrakech+50000
    agadir=agadir*1.08
    nbr=nbr+1
print("agadir depassera marrakech apres",nbr,"ans")
