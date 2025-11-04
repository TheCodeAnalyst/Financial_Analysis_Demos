Create financial_indicators.py
import numpy as np

cash_flows = [-10000, 25000, 15000, 30000]
discount_rate = 0.10 

van_result = np.npv(discount_rate, cash_flows) 
irr_result = np.irr(cash_flows) 

print("--- Résultats de l'Analyse Financière ---")
print(f"1. VAN (Valeur Actuelle Nette): {van_result:,.2f} €")
print(f"2. TRI (Taux de Rendement Interne): {irr_result:.2%}")
