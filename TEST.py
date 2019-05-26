import untangle
l={}
for i in range(1,86):
    print(i)
    s="signboard_dataset\signboard_"+str(i)+"//"+"1.xml"
    if i!=19 and i!=74 and i!=6:
        ob=untangle.parse(s)
        a=ob.SB.info.dir
        if isinstance(a,list):
            for j in range(len(ob.SB.info.dir)):
                if ob.SB.info.dir[j].text.eng.cdata:
                    print(ob.SB.info.dir[j].text.eng.cdata)

        else:
            if a.text.eng.cdata:
                print(ob.SB.info.dir.text.eng.cdata)

    elif i==19:
        print("PARKING RESERVED FOR HOSPITAL STAFF & VISITORS")
    elif i==74:
        print("WEST CAMPUS")
        print("EAST CAMPUS")
        print("JEE & GATE OFFICE")