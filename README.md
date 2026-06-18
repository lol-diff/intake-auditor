# Intake Auditor Service

This service automates the auditing of new legal intakes from Clio.

## Project Structure
- `src/main.py`: Webhook entry point.
- `src/auditor.py`: Logic engine for processing intakes.
- `data/criteria.json`: Rules for case eligibility.

## How to run
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the server:
   `python3 -m uvicorn src.main:app --reload`