Platform Specification (v1)

Purpose
Define the logical and structural design of a normalized private credit analytics platform derived from spreadsheet-based workflows. This document formalizes entities, data grain, relationships, transformation logic, and calculation behavior.

**Design Principles**

Normalize entities to minimize duplication and maintain consistency
Separate raw inputs from processed analytical structures
Define deterministic calculations independent of implementation
Enforce referential and structural integrity

**Core Entities and Grain**

dim_borrower
Grain: One record per borrower
Key Fields:
borrower_id (primary key)
borrower_name
industry
domicile_country
sponsor_name

dim_facility
Grain: One record per credit facility
Key Fields:
facility_id (primary key)
borrower_id (foreign key)
currency
commitment
start_date
maturity_date

dim_loan
Grain: One record per loan / tranche
Key Fields:
loan_id (primary key)
facility_id (foreign key)
tranche
lien
status
spread_bps
base_rate_index

rates
Grain: One record per rate index per as-of date
Key Fields:
rate_index
asof_date
base_rate

fact_cashflow
Grain: One record per loan cashflow event
Key Fields:
cashflow_id (primary key)
loan_id (foreign key)
cashflow_date
interest_amount
principal_amount
fee_amount

fact_position
Grain: One record per loan per as-of date
Key Fields:
loan_id (foreign key)
asof_date
par_outstanding
cost
fair_value

**Entity Relationships**
A borrower may have multiple facilities
A facility may have multiple loans
A loan may produce multiple cashflows
A loan may have multiple position snapshots
Loans reference rate indices for pricing logic
Referential integrity must be enforced across all relationships.

**Transformation Logic (Conceptual)**
Raw data inputs are assumed to originate from spreadsheet exports.

Transformations include:
Standardize identifiers (trim spaces, consistent case)
Enforce data types (dates, numeric fields)
Remove duplicates based on primary keys
Validate foreign key dependencies
Normalize wide structures into fact-style tables where necessary
Processed tables must not contain derived calculations unless explicitly defined.

**Calculation Logic**
Calculations are defined externally in Calculation_Specs.md.
Primary derived measures:
all_in_rate = base_rate + (spread_bps / 10000)
utilization = par_outstanding / commitment
accrued_interest (simplified) = par_outstanding * all_in_rate
Calculations must be deterministic and reproducible.

**Data Quality and Integrity Rules**
Primary keys must be unique and non-null
Foreign keys must resolve to valid parent records
commitment must be positive
spread_bps must be non-negative
financial amounts must conform to defined domain rules
orphan records are not permitted
Violations must generate exceptions.

**Validation and Acceptance**
Validation procedures are defined in UAT_Test_Plan.md.

Platform outputs are considered valid when:
Structural integrity checks pass
Calculation outputs match expected values
Exceptions are documented and explainable

