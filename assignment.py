import random
teams=["Barcelona (ESP)","Bayern (GER)","Benfica (POR)","Chelsea (ENG)","Juventus (ITA)","Paris (FRA)","PSV (NED)","Zenit (RUS)"]
engs=["Arsenal (ENG)","Astana (KAZ)","Atlético (ESP)","BATE (BLR)","CSKA Moskva (RUS)","Dinamo Zagreb (CRO)","Dynamo Kyiv (UKR)","Galatasaray (TUR)"
,"Gent (BEL)","Leverkusen (GER)","Lyon (FRA)","M. Tel-Aviv (ISR)","Malmö (SWE)","Man. City (ENG)","Man. United (ENG)","Mönchengladbach (GER)","Olympiacos (GRE)","Porto (POR)",
"Real Madrid (ESP)","Roma (ITA)","Sevilla (ESP)","Shakhtar Donetsk (UKR)","Valencia (ESP)","Wolfsburg (GER)"]
group=1
members=4

for eng in engs[:]:               # only modification
    if members==4:
        print("Group {} consists of;".format(group))
        members=0
        group+=1
    if members<1:
        team=random.choice(teams)
        print(team)
        members+=1
        teams.remove(str(team))
    team=random.choice(engs)
    print(team)
    members+=1
    engs.remove(str(team))