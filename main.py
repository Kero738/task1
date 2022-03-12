import cobra
from cobra import Model, Reaction, Metabolite
model=Model('example')
RE1=Reaction('RE1')
RE1.name='RE1'
RE1.lower_bound=0
RE1.upper_bound=1000

RE2=Reaction('RE2')
RE2.name='RE2'
RE2.lower_bound=0
RE2.upper_bound=1000

RE0=Reaction('RE0')
RE0.name='RE0'
RE0.lower_bound=1
RE0.upper_bound=1

RE4=Reaction('RE4')
RE4.name='RE4'
RE4.lower_bound=0
RE4.upper_bound=1000

ATP_R=Reaction('ATP_R')
ATP_R.name='ATP_R'
ATP_R.lower_bound=0
ATP_R.upper_bound=1000

RE3=Reaction('RE3')
ATP_R.name='v3'
ATP_R.lower_bound=.9
ATP_R.upper_bound=.9
A= Metabolite(
    'A',compartment='c')
B=Metabolite(
    'B',compartment='c')
C= Metabolite(
    'C',compartment='c')
ATP= Metabolite(
    'ATP',compartment='c')
RE1.add_metabolites({A:-1,B:1})

RE2.add_metabolites({B:-1,C:1})

RE0.add_metabolites({A:1})

RE4.add_metabolites({C:-1})

ATP_R.add_metabolites({A:-1,ATP:1})

RE3.add_metabolites({ATP:-1})

model.add_reactions([RE0,RE1,ATP_R,RE2,RE3,RE4])

model.objective = 'M'

model.optimize()
model.summary()