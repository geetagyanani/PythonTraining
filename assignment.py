import random
participants=["Barcelona (ESP)","Bayern (GER)","Benfica (POR)","Chelsea (ENG)","Juventus (ITA)","Paris (FRA)","PSV (NED)","Zenit (RUS)"]
engs=["Arsenal (ENG)","Astana (KAZ)","Atlético (ESP)","BATE (BLR)","CSKA Moskva (RUS)","Dinamo Zagreb (CRO)","Dynamo Kyiv (UKR)","Galatasaray (TUR)"
,"Gent (BEL)","Leverkusen (GER)","Lyon (FRA)","M. Tel-Aviv (ISR)","Malmö (SWE)","Man. City (ENG)","Man. United (ENG)","Mönchengladbach (GER)","Olympiacos (GRE)","Porto (POR)",
"Real Madrid (ESP)","Roma (ITA)","Sevilla (ESP)","Shakhtar Donetsk (UKR)","Valencia (ESP)","Wolfsburg (GER)"]
group=1
membersInGroup=4

for eng in engs[:]:               # only modification
    if membersInGroup==4:
        print("Group {} consists of;".format(group))
        membersInGroup=0
        group+=1
    if membersInGroup<1:
        person=random.choice(participants)
        print(person)
        membersInGroup+=1
        participants.remove(str(person))
    person=random.choice(engs)
    print(person)
    membersInGroup+=1
    engs.remove(str(person))