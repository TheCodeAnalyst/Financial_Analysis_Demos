import numpy as np
import numpy_financial as npf 

cash_flows = [-10000, 25000, 15000, 30000]
discount_rate = 0.10 
van_result = npf.npv(discount_rate, cash_flows) 
irr_result = npf.irr(cash_flows) 

print("--- 1. Analyse de la Rentabilité (VAN/TRI) ---")
print(f"  VAN: {van_result:,.2f} € | TRI: {irr_result:.2%}")
print("-" * 35)


project_A_returns = [0.20, 0.10, 0.30, 0.15, 0.25]
project_B_returns = [0.18, 0.19, 0.21, 0.20, 0.22] 

std_dev_A = np.std(project_A_returns)
std_dev_B = np.std(project_B_returns)

print("--- 2. Analyse des Risques (Ecart-type) ---")
print(f"Projet A: Ecart-type (Risque) est: {std_dev_A:.4f}")
print(f"Projet B: Ecart-type (Risque) est: {std_dev_B:.4f}")
print("-" * 35)
