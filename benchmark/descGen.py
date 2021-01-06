import random

f = open("gps-desc-10.n3", "w")

f.write('PREFIX math: <http://www.w3.org/2000/10/swap/math#>\n')
f.write('PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n')
f.write('PREFIX e: <http://eulersharp.sourceforge.net/2003/03swap/log-rules#>\n')
f.write('PREFIX action: <http://josd.github.io/eye/reasoning/gps/action#>\n')
f.write('PREFIX medication: <http://josd.github.io/eye/reasoning/gps/medication#>\n')
f.write('PREFIX sct: <http://snomed.info/id/>\n')
f.write('PREFIX care: <http://josd.github.io/eye/reasoning/gps/care#>\n')
f.write('PREFIX gps: <http://josd.github.io/eye/reasoning/gps/gps-schema#>\n')
f.write('\n')

for i in range(0,10):
    state1 = random.randint(1, 3)
    state2 = random.randint(state1+1, 10)
    f.write('{care:Parkinson gps:description (\n')
    f.write('     {?patient care:state care:state_' + str(state1) +'.}\n')
    f.write('     {?patient gps:medication medication:Medication_'+ str(i) +'.}\n')
    f.write('     {?patient care:state care:state_' + str(state2) +'.}\n')

    f.write('     action:take_pill_Medication_'+ str(i) + '\n')
    f.write('     "P1D"^^xsd:dayTimeDuration\n')
    f.write('     ' + str(random.randint(1, 100)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     )\n')
    f.write('} <= {\n')
    f.write('     ?patient a care:Patient.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?patient care:gender care:Male.\n')
    else:
        f.write('     ?patient care:gender care:Female.\n')
    f.write('     ?patient care:age ?age.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?age math:greaterThan 18.\n')
    f.write(' }.\n')
    f.write('\n')



f = open("gps-desc-100.n3", "w")

f.write('PREFIX math: <http://www.w3.org/2000/10/swap/math#>\n')
f.write('PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n')
f.write('PREFIX e: <http://eulersharp.sourceforge.net/2003/03swap/log-rules#>\n')
f.write('PREFIX action: <http://josd.github.io/eye/reasoning/gps/action#>\n')
f.write('PREFIX medication: <http://josd.github.io/eye/reasoning/gps/medication#>\n')
f.write('PREFIX sct: <http://snomed.info/id/>\n')
f.write('PREFIX care: <http://josd.github.io/eye/reasoning/gps/care#>\n')
f.write('PREFIX gps: <http://josd.github.io/eye/reasoning/gps/gps-schema#>\n')
f.write('\n')

for i in range(0,100):
    state1 = random.randint(1, 3)
    state2 = random.randint(state1+1, 10)
    f.write('{care:Parkinson gps:description (\n')
    f.write('     {?patient care:state care:state_' + str(state1) +'.}\n')
    f.write('     {?patient gps:medication medication:Medication_'+ str(i) +'.}\n')
    f.write('     {?patient care:state care:state_' + str(state2) +'.}\n')

    f.write('     action:take_pill_Medication_'+ str(i) + '\n')
    f.write('     "P1D"^^xsd:dayTimeDuration\n')
    f.write('     ' + str(random.randint(1, 100)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     )\n')
    f.write('} <= {\n')
    f.write('     ?patient a care:Patient.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?patient care:gender care:Male.\n')
    else:
        f.write('     ?patient care:gender care:Female.\n')
    f.write('     ?patient care:age ?age.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?age math:greaterThan 18.\n')
    f.write(' }.\n')
    f.write('\n')


f = open("gps-desc-1000.n3", "w")

f.write('PREFIX math: <http://www.w3.org/2000/10/swap/math#>\n')
f.write('PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n')
f.write('PREFIX e: <http://eulersharp.sourceforge.net/2003/03swap/log-rules#>\n')
f.write('PREFIX action: <http://josd.github.io/eye/reasoning/gps/action#>\n')
f.write('PREFIX medication: <http://josd.github.io/eye/reasoning/gps/medication#>\n')
f.write('PREFIX sct: <http://snomed.info/id/>\n')
f.write('PREFIX care: <http://josd.github.io/eye/reasoning/gps/care#>\n')
f.write('PREFIX gps: <http://josd.github.io/eye/reasoning/gps/gps-schema#>\n')
f.write('\n')

for i in range(0,1000):
    state1 = random.randint(1, 3)
    state2 = random.randint(state1+1, 20)
    f.write('{care:Parkinson gps:description (\n')
    f.write('     {?patient care:state care:state_' + str(state1) +'.}\n')
    f.write('     {?patient gps:medication medication:Medication_'+ str(i) +'.}\n')
    f.write('     {?patient care:state care:state_' + str(state2) +'.}\n')

    f.write('     action:take_pill_Medication_'+ str(i) + '\n')
    f.write('     "P1D"^^xsd:dayTimeDuration\n')
    f.write('     ' + str(random.randint(1, 100)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     )\n')
    f.write('} <= {\n')
    f.write('     ?patient a care:Patient.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?patient care:gender care:Male.\n')
    else:
        f.write('     ?patient care:gender care:Female.\n')
    f.write('     ?patient care:age ?age.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?age math:greaterThan 18.\n')
    f.write(' }.\n')
    f.write('\n')



f = open("gps-desc-10000.n3", "w")

f.write('PREFIX math: <http://www.w3.org/2000/10/swap/math#>\n')
f.write('PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n')
f.write('PREFIX e: <http://eulersharp.sourceforge.net/2003/03swap/log-rules#>\n')
f.write('PREFIX action: <http://josd.github.io/eye/reasoning/gps/action#>\n')
f.write('PREFIX medication: <http://josd.github.io/eye/reasoning/gps/medication#>\n')
f.write('PREFIX sct: <http://snomed.info/id/>\n')
f.write('PREFIX care: <http://josd.github.io/eye/reasoning/gps/care#>\n')
f.write('PREFIX gps: <http://josd.github.io/eye/reasoning/gps/gps-schema#>\n')
f.write('\n')

for i in range(0,10000):
    state1 = random.randint(1, 3)
    state2 = random.randint(state1+1, 100)
    f.write('{care:Parkinson gps:description (\n')
    f.write('     {?patient care:state care:state_' + str(state1) +'.}\n')
    f.write('     {?patient gps:medication medication:Medication_'+ str(i) +'.}\n')
    f.write('     {?patient care:state care:state_' + str(state2) +'.}\n')

    f.write('     action:take_pill_Medication_'+ str(i) + '\n')
    f.write('     "P1D"^^xsd:dayTimeDuration\n')
    f.write('     ' + str(random.randint(1, 100)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     ' + str(random.uniform(0.25, 1)) + '\n')
    f.write('     )\n')
    f.write('} <= {\n')
    f.write('     ?patient a care:Patient.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?patient care:gender care:Male.\n')
    else:
        f.write('     ?patient care:gender care:Female.\n')
    f.write('     ?patient care:age ?age.\n')
    if random.uniform(0, 1)>0.5:
        f.write('     ?age math:greaterThan 18.\n')
    f.write(' }.\n')
    f.write('\n')