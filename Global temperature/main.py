import pandas as pd
import matplotlib.pyplot as plt

filename1 = 'ExcelFormattedGISTEMPDataCSV.csv'
temp1 = pd.read_csv(filename1)
filename2 = 'ExcelFormattedGISTEMPData2CSV.csv'
temp2 = pd.read_csv(filename2)

Onedecade = temp2.iloc[121: 131, 0: 4]
print(Onedecade)

fig, ax = plt.subplots()

ax.plot(Onedecade['Year'], Onedecade['Glob'], marker = 'v', linestyle = '--')
ax.plot(Onedecade['Year'], Onedecade['NHem'], marker = 'o')
ax.plot(Onedecade['Year'], Onedecade['SHem'], marker = 'o', linestyle = '-.')

# ax.plot(Onedecade['Year'], Onedecade['64N-90N'])
# ax.plot(Onedecade['Year'], Onedecade['44N-64N'])
# ax.plot(Onedecade['Year'], Onedecade['24N-44N'])
# ax.plot(Onedecade['Year'], Onedecade['EQU-24N'])
# ax.plot(Onedecade['Year'], Onedecade['24S-EQU'])
# ax.plot(Onedecade['Year'], Onedecade['44S-24S'])
# ax.plot(Onedecade['Year'], Onedecade['64S-44S'])
# ax.plot(Onedecade['Year'], Onedecade['90S-64S'])
ax.set_xlabel('Time (Years)')
# ax[1].set_xlabel('Time (Years)')
# ax[2].set_xlabel('Time (Years)')
ax.set_ylabel('Temperature (Celsius)')
# ax[1].set_ylabel('Temperature (Celsius)')
# ax[2].set_ylabel('Temperature (Celsius)')
ax.set_title('Global and Hemispheric Annual Means')
#plt.axis([2000.5, 2014.5, 40, 90])
plt.grid(True)
#ax.xticks([])
plt.savefig('temp.png')
plt.show()
