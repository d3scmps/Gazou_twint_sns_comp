import casanova 
from datetime import datetime, timedelta


def check_date(date_f):
    date = datetime.fromisoformat(date_f)
    nd_1 = date + timedelta(hour=1)
    nd_2 = date - timedelta(hour=1)
    if date <= nd_1 and date >= nd_2:
        return True
    return False

with open('twint_onlyof3.csv') as f1, open('sns_onlyof3.csv') as f2, open('snsItwint.csv') as f3 ,open('gazou_sansthread.csv') as f4, open('JOINT_usid_created.csv','w') as f5:
    readtwint = casanova.reader(f1)
    readsns = casanova.reader(f2)
    readinter = casanova.reader(f3)
    enr = casanova.enricher(f4,f5)
    clefs_crt = set()
    clefs_usid = set()
    # twint
    T_crt = readtwint.pos.created_at
    T_id = readtwint.pos.user_id
    S_crt = readsns.pos.created_at
    S_id = readsns.pos.user_id
    I_crt = readI.pos.created_at
    I_id = readI.pos.user_id
    E_crt = enr.pos.created_at
    E_id = enr.pos.user_id
    for row in readtwint:
        clefs_crt.add(row.T_crt)
        clefs_usid.add(row.T_id)
    for row in readsns:
        clefs_crt.add(row.S_crt)
        clefs_usid.add(row.S_id)
    for row in readinter:
        clefs_crt.add(row.I_crt)
        clefs_usid.add(row.I_id)
    for row in enr:
        if row[E_crt] in clefs_crt and row[E_id] in clefs_usid:
            enr.writerow(row) #function(sur l'heure avec interval)  