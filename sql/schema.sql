CREATE TABLE borrowers (
borrower_id TEXT PRIMARY KEY,
borrower_name TEXT,
industry TEXT,
domicile_country TEXT,
sponsor_name TEXT
);

CREATE TABLE facilities (
facility_id TEXT PRIMARY KEY,
borrower_id TEXT,
currency TEXT,
commitment NUMERIC,
start_date DATE,
maturity_date DATE
);

CREATE TABLE loans (
loan_id TEXT PRIMARY KEY,
facility_id TEXT,
tranche TEXT,
lien TEXT,
status TEXT,
spread_bps NUMERIC,
base_rate_index TEXT
);

CREATE TABLE rates (
rate_index TEXT,
asof_date DATE,
base_rate NUMERIC
);

CREATE TABLE cashflows (
cashflow_id TEXT PRIMARY KEY,
loan_id TEXT,
cashflow_date DATE,
interest_amount NUMERIC,
principal_amount NUMERIC,
fee_amount NUMERIC
);
