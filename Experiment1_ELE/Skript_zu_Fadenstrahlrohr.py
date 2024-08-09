import matplotlib.pyplot as plt

# Daten
radii = [50, 40, 30]  # Radii in mm
current_variation = [177.5, 175.9, 172.7]  # I Variation
current_uncertainty = [0.6, 1.09, 1.3]  # Unsicherheiten bei I

voltage_variation = [175.5, 189.7, 242.7]  # U Variation
voltage_uncertainty = [0.5, 1.08, 1.3]  # Unsicherheiten bei U

# Realer Wert
real_value = 175.8

# Plot für Stromvariationen (I)
plt.errorbar(radii, current_variation, yerr=current_uncertainty, fmt='o', label='I Variation', capsize=5)

# Plot für Spannungsvariationen (U)
plt.errorbar(radii, voltage_variation, yerr=voltage_uncertainty, fmt='o', label='U Variation', capsize=5)

# Reale Wert Linie
plt.axhline(y=real_value, color='red', linestyle='-', label='Realer Wert 175.8')

# Labels und Titel
plt.xlabel('Radius (mm)')
plt.ylabel('Messwert')
plt.title('Messreihe der spezifischen Ladung e/m')
plt.legend()
plt.grid()
plt.savefig('../Graphics/Fadenstrahlrohr.pdf')
# Plot anzeigen
plt.show()