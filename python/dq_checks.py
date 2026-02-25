import pandas as pd

print("Running Data Quality Checks...\n")

borrowers = pd.read_csv("data/raw/borrowers.csv")
facilities = pd.read_csv("data/raw/facilities.csv")
loans = pd.read_csv("data/raw/loans.csv")
cashflows = pd.read_csv("data/raw/cashflows.csv")

def check_uniqueness(df, column, name):
duplicates = df[column].duplicated().sum()
if duplicates == 0:
print(f"[PASS] {name} uniqueness check")
else:
print(f"[FAIL] {name} uniqueness check - {duplicates} duplicates found")

def check_orphans(child_df, parent_df, key, child_name):
missing = ~child_df[key].isin(parent_df[key])
count = missing.sum()
if count == 0:
print(f"[PASS] {child_name} relationship check")
else:
print(f"[FAIL] {child_name} relationship check - {count} orphan records")

check_uniqueness(borrowers, "borrower_id", "Borrower ID")
check_uniqueness(facilities, "facility_id", "Facility ID")
check_uniqueness(loans, "loan_id", "Loan ID")

check_orphans(facilities, borrowers, "borrower_id", "Facility -> Borrower")
check_orphans(loans, facilities, "facility_id", "Loan -> Facility")
check_orphans(cashflows, loans, "loan_id", "Cashflow -> Loan")

print("\nData Quality Checks Complete.")
