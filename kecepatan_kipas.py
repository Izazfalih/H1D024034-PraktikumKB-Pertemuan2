import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Variabel input (antecedent)
suhu = ctrl.Antecedent(np.arange(0, 41), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0, 101), 'kelembaban')
# Variabel output (consequent)
kipas = ctrl.Consequent(np.arange(0, 101), 'kipas')

# Fungsi Keanggotaan Suhu
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 10, 20])
suhu['sejuk'] = fuzz.trimf(suhu.universe, [19, 22, 24])
suhu['hangat'] = fuzz.trimf(suhu.universe, [24, 27, 29])
suhu['panas'] = fuzz.trimf(suhu.universe, [29, 34, 40])

# Fungsi Keanggotaan Kelembapan
kelembaban['kering'] = fuzz.trimf(kelembaban.universe, [0, 20, 40])
kelembaban['normal'] = fuzz.trimf(kelembaban.universe, [30, 50, 70])
kelembaban['lembap'] = fuzz.trimf(kelembaban.universe, [60, 70, 80])
kelembaban['basah'] = fuzz.trimf(kelembaban.universe, [75, 90, 100])

# Fungsi Keanggotaan Kecepatan Kipas
kipas['mati'] = fuzz.trimf(kipas.universe, [0, 0, 20])
kipas['lambat'] = fuzz.trimf(kipas.universe, [10, 30, 50])
kipas['sedang'] = fuzz.trimf(kipas.universe, [40, 60, 80])
kipas['cepat'] = fuzz.trimf(kipas.universe, [70, 90, 100])

# Aturan Fuzzy
rule1 = ctrl.Rule(suhu['dingin'] & kelembaban['kering'], kipas['mati'])
rule2 = ctrl.Rule(suhu['sejuk'] & kelembaban['normal'], kipas['lambat'])
rule3 = ctrl.Rule(suhu['hangat'] & kelembaban['lembap'], kipas['sedang'])
rule4 = ctrl.Rule(suhu['panas'] & kelembaban['basah'], kipas['cepat'])

# Sistem Fuzzy
system_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
system = ctrl.ControlSystemSimulation(system_ctrl)

# Input (contoh)
system.input['suhu'] = 26
system.input['kelembaban'] = 65

# Proses
system.compute()

# Output
print("Kecepatan kipas:", system.output['kipas'])

# Visualisasi
suhu.view()
kelembaban.view()
kipas.view()

plt.show()