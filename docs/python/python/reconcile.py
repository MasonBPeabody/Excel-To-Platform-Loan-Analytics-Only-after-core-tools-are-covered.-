import pandas as pd

print("Running Reconciliation...\n")

cashflows = pd.read_csv("data/raw/cashflows.csv")

totals = cashflows[["interest_amount", "principal_amount", "fee_amount"]].sum()

print("Cashflow Totals:")
print(totals)

print("\nReconciliation Complete.")
