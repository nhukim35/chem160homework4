from cards import*
ntrials=1000
winlist=[]
for i in range(ntrials):
    adeck=deck()
    adeck
    bdeck=deck()
    bdeck
    adeck.shuffle()
    bdeck.shuffle()
    ascore=0
    bscore=0
    while adeck.cardsleft()>0:
        acard=adeck.dealcard()
        bcard=bdeck.dealcard()
    if acard.value()==bcard.value():
        ascore=bscore
    if acard.value()>bcard.value():
        ascore=ascore+2
    if bcard.value()>acard.value():
        bscore=bscore+2
    if ascore>bscore:
        winlist.append(ascore-bscore)
    if ascore<bscore:
        winlist.append(bscore-ascore)
    if ascore==bscore:
        winlist.append(ascore-bscore)
print("0",winlist.count(0)/ntrials)
print("2",winlist.count(2)/ntrials)
print("4",winlist.count(4)/ntrials)
print("6",winlist.count(6)/ntrials)
