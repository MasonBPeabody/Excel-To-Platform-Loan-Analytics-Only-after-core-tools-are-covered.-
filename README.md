# Excel-To-Platform-Loan-Analytics

Excel-based private credit loan model translated into platform-ready data architecture, transformations, and validation framework.
Overview

This repository simulates a simplified analytics platform designed to model how spreadsheet-driven financial workflows can be translated into deterministic, platform-oriented data validation and reconciliation logic. The project uses normalized private credit datasets representing borrowers, facilities, loans, rates, and cashflows to demonstrate structured data ingestion, relational integrity enforcement, and financial control checks.

Rather than relying on implicit Excel formulas or manual aggregation, all validation routines are implemented using reproducible programmatic logic. The objective is to illustrate how analytical structures commonly embedded in Excel models can be formalized into platform-ready validation and monitoring controls.

**Project Objectives**

Demonstrate deterministic data ingestion from a structured raw data layer
Enforce entity identity integrity through primary key validation
Validate referential consistency across hierarchical datasets
Detect structural exceptions and orphaned records
Perform reconciliation-style financial control checks
Model platform-oriented thinking independent of spreadsheet logic

**Repository Structure**

data/raw
Contains simulated source datasets representing normalized platform inputs.

borrowers.csv – Borrower master data
facilities.csv – Facility-level attributes and commitments
loans.csv – Loan and tranche metadata
rates.csv – Reference rate inputs
cashflows.csv – Transactional cash activity

**data/processed**
Represents the logical destination for transformed or validated datasets.

docs
Contains metadata definitions and platform design artifacts.
sql
Includes schema definitions modeling relational platform structures.
python
Contains validation and reconciliation scripts simulating platform integrity controls.
powerquery
Contains Power Query logic illustrating ingestion and exception detection workflows.

**Validation Framework**

**The validation logic implemented within this project mirrors common production data platform controls:**
**Entity Integrity Validation**
Ensures uniqueness and structural correctness of entity identifiers to prevent duplication and aggregation distortion.
**Referential Integrity Checks**
Verifies relational dependencies between borrowers, facilities, loans, and cashflows to detect orphaned or inconsistent records.
**Exception Detection Logic**
Isolates structural violations rather than assuming clean data conditions.
**Financial Reconciliation Controls**
Computes deterministic aggregates across transactional measures to validate numerical consistency.
**Deterministic Processing Principle**
All validation outputs are reproducible and independent of manual spreadsheet operations.

**Notebook Demonstration**
The validation workflow models a platform-style process:
Explicit ingestion of normalized datasets
Verification of entity identity integrity
Referential integrity enforcement across entities
Detection of structural exceptions
Deterministic reconciliation of financial measures
This sequence reflects how Excel-based analytical logic can be translated into scalable validation routines within a controlled data platform environment.

**Validation Demonstration Artifact**
A static PDF export of the notebook output is included to provide environment-independent verification of the validation workflow. The artifact illustrates:
Successful deterministic data ingestion
Referential integrity validation results
Structural exception detection logic
Reconciliation control totals

The document is intended to allow reviewers to evaluate validation behavior and outputs without requiring execution of a local Python environment.

All validation checks resolved without structural exceptions, indicating relational integrity across normalized entities.

**Why This Matters**

Financial analytics platforms depend on strict data integrity, relational consistency, and reproducibility. Spreadsheet-based processes often conceal dependencies and introduce silent errors. This project demonstrates how those risks can be mitigated through deterministic validation logic and platform-oriented control structures.

Key themes demonstrated:

Deterministic ingestion patterns
Structured validation logic
Referential integrity enforcement
Exception-driven quality controls
Reconciliation discipline
