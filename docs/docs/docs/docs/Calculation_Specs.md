Calculation Specifications (v1)

Purpose
Define deterministic calculation rules derived from an Excel-style private credit model so the logic can be implemented in a database, service layer, or reporting layer.

Key Assumptions

base_rate is expressed as a decimal (example: 0.052 = 5.2%)

spread_bps is expressed in basis points (example: 450 = 4.50%)

all calculations shown are simplified for demonstration

day count convention is not applied in v1 (can be added later)

All-In Rate
Business Meaning:
Total interest rate applied to a loan for a given as-of date.

Inputs:

base_rate (from rates)

spread_bps (from dim_loan)

Rule:
all_in_rate = base_rate + (spread_bps / 10000)

Validation Checks:

spread_bps must be non-negative

base_rate must exist for the loan's base_rate_index and as-of date

Utilization
Business Meaning:
How much of the facility commitment is currently drawn.

Inputs:

par_outstanding (from fact_position)

commitment (from dim_facility)

Rule:
utilization = par_outstanding / commitment

Validation Checks:

commitment must be greater than 0

utilization should typically be between 0 and 1 (flag if greater than 1)

Accrued Interest (Simplified)
Business Meaning:
Approximate accrued interest amount for a loan as of a given date.

Inputs:

par_outstanding (from fact_position)

all_in_rate (from rule 1)

Rule (simplified):
accrued_interest = par_outstanding * all_in_rate

Note:
In a production model, this would include day count fraction and accrual period boundaries.

Validation Checks:

par_outstanding must be non-negative for active loans

accrued_interest should be non-negative



