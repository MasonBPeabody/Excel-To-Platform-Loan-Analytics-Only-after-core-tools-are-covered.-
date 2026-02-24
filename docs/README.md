**Excel to Platform – Private Credit Loan Analytics**
-----------------------------------------------------------------------------------
**Overview**
This repository demonstrates how spreadsheet-driven financial workflows can be translated into platform-ready data architecture, structured specifications, and validation controls.

The project simulates a private credit analytics environment using normalized relational design principles. It models borrowers, facilities, loans, rates, positions, and cashflows to illustrate how Excel-based logic can be formalized into deterministic system behavior suitable for scalable enterprise platforms.

**Problem Context**
Financial institutions frequently rely on complex Excel models that embed business logic, calculations, and data dependencies within spreadsheets. While flexible, these models introduce structural risk, ambiguous definitions, and scalability constraints.

**This project illustrates how such workflows can be decomposed into:**
Explicit data definitions
Normalized entities and relationships
Deterministic calculation rules
Data quality and reconciliation controls
Core Components

**Data Model**
**A normalized schema representing core private credit entities:**
dim_borrower
dim_facility
dim_loan
rates
fact_cashflow
fact_position

**Entity relationships and grain are formalized in the ERD.**
**Governance Layer**
A structured data dictionary defines semantic meaning, data types, grain, sources, and validation rules. This prevents business logic from being implicitly encoded within calculations.

**Calculation Framework**
Calculation_Specs.md documents deterministic rules derived from spreadsheet-style analytics, separating business meaning from implementation.

**Validation & Integrity Controls**
**The repository includes examples of:**
Referential integrity checks
Uniqueness controls
Reconciliation logic
Data quality validation patterns

**These mirror real-world platform assurance practices.**
**Why This Matters**
This prototype mirrors the architectural and analytical challenges encountered when evolving legacy Excel and Power Query workflows into robust enterprise platforms.

**It emphasizes:**
Data modeling discipline
Logic formalization
Specification-driven design
Platform-oriented validation

**Repository Structure**
docs/
Contains platform specifications, calculation rules, data dictionary, ERD, and UAT framework.
data/
Simulated raw datasets representing spreadsheet-style inputs.
sql/
Normalized schema and integrity validation queries.
python/
Example validation and reconciliation utilities.

**Screenshots (Validation & Controls)**

The following examples illustrate how platform-style data validation and reconciliation checks would execute against the simulated datasets.

**Data Quality Checks**
Example validations include:

Primary key uniqueness
Referential integrity (orphan detection)
Structural consistency

**Reconciliation Checks**
Example validations include:

Aggregate financial tie-outs
Cashflow total verification

**Note**
Screenshots will reflect execution of Python validation scripts (dq_checks.py, reconcile.py) against the repository’s simulated input datasets.



