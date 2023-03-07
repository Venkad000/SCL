import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


sp_dif = ctrl.Antecedent(np.arange(0, 255, 1),'Speed difference')
acc = ctrl.Antecedent(np.arange(0, 255, 1),'Acceleration')
th_cnt = ctrl.Consequent(np.arange(0, 255, 1),'Throttle control')


sp_dif['NL']= fuzz.trapmf(sp_dif.universe,[0,0,31,61])
sp_dif['NM']= fuzz.trimf(sp_dif.universe,[31,61,95])
sp_dif['NS']= fuzz.trimf(sp_dif.universe,[61,95,127])
sp_dif['ZE']= fuzz.trimf(sp_dif.universe,[95,127,159])
sp_dif['PS']= fuzz.trimf(sp_dif.universe,[127,159,191])
sp_dif['PM']= fuzz.trimf(sp_dif.universe,[159,191,223])
sp_dif['PL']= fuzz.trapmf(sp_dif.universe,[191,223,255,255])

acc['NL']= fuzz.trapmf(acc.universe,[0,0,31,61])
acc['NM']= fuzz.trimf(acc.universe,[31,61,95])
acc['NS']= fuzz.trimf(acc.universe,[61,95,127])
acc['ZE']= fuzz.trimf(acc.universe,[95,127,159])
acc['PS']= fuzz.trimf(acc.universe,[127,159,191])
acc['PM']= fuzz.trimf(acc.universe,[159,191,223])
acc['PL']= fuzz.trapmf(acc.universe,[191,223,255,255])

th_cnt['NL']= fuzz.trapmf(th_cnt.universe,[0,0,31,61])
th_cnt['NM']= fuzz.trimf(th_cnt.universe,[31,61,95])
th_cnt['NS']= fuzz.trimf(th_cnt.universe,[61,95,127])
th_cnt['ZE']= fuzz.trimf(th_cnt.universe,[95,127,159])
th_cnt['PS']= fuzz.trimf(th_cnt.universe,[127,159,191])
th_cnt['PM']= fuzz.trimf(th_cnt.universe,[159,191,223])
th_cnt['PL']= fuzz.trapmf(th_cnt.universe,[191,223,255,255])




sp_dif['NL'].view()
acc.view()
th_cnt.view()


r1 = ctrl.Rule(sp_dif['NL'] & acc['ZE'],th_cnt['PL'])
r2 = ctrl.Rule(sp_dif['ZE'] & acc['NL'],th_cnt['PL'])
r3 = ctrl.Rule(sp_dif['NM'] & acc['ZE'],th_cnt['PM'])
r4 = ctrl.Rule(sp_dif['NS'] & acc['PS'],th_cnt['PS'])
r5 = ctrl.Rule(sp_dif['PS'] & acc['NS'],th_cnt['NS'])
r6 = ctrl.Rule(sp_dif['PL'] & acc['ZE'],th_cnt['NL'])
r7 = ctrl.Rule(sp_dif['ZE'] & acc['NS'],th_cnt['PS'])
r8 = ctrl.Rule(sp_dif['ZE'] & acc['NM'],th_cnt['PM'])
#r1.view()

tipping_ctrl = ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)


tipping.input['Speed difference'] = 100
tipping.input['Acceleration'] = 70

# Crunch the numbers
tipping.compute()

print(tipping.output['Throttle control'])
th_cnt.view(sim=tipping)