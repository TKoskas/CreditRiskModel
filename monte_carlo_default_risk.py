import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Paramètres du modèle
V = 1000  # Valeur actuelle des actifs
D = 800  # Dette à échéance
sigma = 0.2  # Volatilité des actifs
r = 0.05  # Taux sans risque
T = 1  # Temps jusqu'à l'échéance
Recovery_rate = 0.4  # Taux de recouvrement (40%)
N_simulations = 10000  # Nombre de simulations Monte Carlo

# 1. Calcul de la probabilité de défaut (PD) via le modèle Merton
def calculate_PD(V, D, sigma, r, T):
    d1 = (np.log(V / D) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    PD = 1 - norm.cdf(d1)
    return PD

# 2. Calcul de la perte en cas de défaut (LGD) avec le taux de recouvrement
def calculate_LGD(Recovery_rate):
    LGD = 1 - Recovery_rate
    return LGD

# 3. Simulation Monte Carlo pour estimer les pertes
def monte_carlo_simulation(V, D, sigma, r, T, Recovery_rate, N_simulations):
    Z = np.random.normal(0, 1, N_simulations)  # Variable aléatoire normale
    S_T = V * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)  # Valeur des actifs à l’échéance
    default = S_T < D  # Si l’actif est inférieur à la dette, le défaut survient
    losses = default * (1 - Recovery_rate) * D  # Pertes en cas de défaut
    return losses

# 4. Calcul de la Probabilité de Défaut (PD) et Perte en cas de Défaut (LGD)
PD = calculate_PD(V, D, sigma, r, T)
LGD = calculate_LGD(Recovery_rate)

# Affichage des résultats
print(f"Probabilité de défaut (PD): {PD:.4f}")
print(f"Perte en cas de défaut (LGD): {LGD:.4f}")

# 5. Simulation de la distribution des pertes
losses = monte_carlo_simulation(V, D, sigma, r, T, Recovery_rate, N_simulations)

# Calcul de la perte moyenne du portefeuille
avg_loss = np.mean(losses)
print(f"Perte moyenne sur le portefeuille (simulée via Monte Carlo): {avg_loss:.2f}")

# Affichage de la distribution des pertes via un histogramme
plt.figure(figsize=(10, 6))
plt.hist(losses, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(avg_loss, color='red', linestyle='dashed', linewidth=2, label=f'Perte moyenne : {avg_loss:.2f}')
plt.title('Distribution des pertes en cas de défaut')
plt.xlabel('Pertes ($)')
plt.ylabel('Fréquence')
plt.legend()
plt.grid(True)
plt.show()
