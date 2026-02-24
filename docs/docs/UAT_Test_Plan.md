UAT Test Plan (v1)

Purpose
Validate that platform tables, relationships, and calculations match expected results derived from the source (simulated Excel exports) and conform to defined business rules.

Scope

Entities: borrower, facility, loan, rates, cashflows, positions

Checks: completeness, uniqueness, referential integrity, calculation correctness, basic reasonableness

Test Data
Source files:

data/raw/borrowers.csv

data/raw/facilities.csv

data/raw/loans.csv

data/raw/rates.csv

data/raw/cashflows.csv

Acceptance Criteria Summary

No broken relationships between borrower -> facility -> loan -> cashflows/positions

Key identifiers are unique and non-null

Required fields are present and correctly typed

Calculations follow Calculation_Specs.md rules

Exceptions are logged and explainable

Tests

T001 - Borrower ID uniqueness
Objective: Ensure borrower_id uniquely identifies each borrower.
Method: Confirm no duplicate borrower_id values.
Pass Criteria: 0 duplicates.

T002 - Facility ID uniqueness
Objective: Ensure facility_id uniquely identifies each facility.
Method: Confirm no duplicate facility_id values.
Pass Criteria: 0 duplicates.

T003 - Loan ID uniqueness
Objective: Ensure loan_id uniquely identifies each loan/tranche.
Method: Confirm no duplicate loan_id values.
Pass Criteria: 0 duplicates.

T004 - Required fields non-null
Objective: Ensure critical fields are populated.
Fields:

borrowers: borrower_id, borrower_name

facilities: facility_id, borrower_id, currency, commitment, start_date, maturity_date

loans: loan_id, facility_id, spread_bps, base_rate_index
Pass Criteria: No nulls in required fields.

T005 - Referential integrity: facility -> borrower
Objective: Every facility must map to a valid borrower.
Method: facilities.borrower_id must exist in borrowers.borrower_id
Pass Criteria: 0 orphan facilities.

T006 - Referential integrity: loan -> facility
Objective: Every loan must map to a valid facility.
Method: loans.facility_id must exist in facilities.facility_id
Pass Criteria: 0 orphan loans.

T007 - Referential integrity: cashflow -> loan
Objective: Every cashflow must map to a valid loan.
Method: cashflows.loan_id must exist in loans.loan_id
Pass Criteria: 0 orphan cashflows.

T008 - Rate coverage
Objective: Each loan base_rate_index must have a matching rate in rates for required as-of dates.
Method: loans.base_rate_index must exist in rates.rate_index
Pass Criteria: 0 missing rate_index mappings.

T009 - All-In Rate calculation
Objective: Validate all_in_rate formula implementation.
Rule: all_in_rate = base_rate + (spread_bps/10000)
Method: Spot-check at least 3 loans across at least 2 dates.
Pass Criteria: Calculated all_in_rate matches expected values within rounding tolerance (0.000001).

T010 - Utilization reasonableness
Objective: Flag utilization outside normal bounds.
Rule: utilization = par_outstanding / commitment
Method: Confirm utilization is not negative; flag if > 1 for review.
Pass Criteria: No negative utilization; any > 1 documented as exception.

Defect Management

Record defects with: test_id, description, severity, root_cause_hypothesis, owner, status

Retest after fixes and record outcome

Sign-Off

Business owner confirms outputs align with business intent

Technology owner confirms tests passed and exceptions are understood
