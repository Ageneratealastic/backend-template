# Backend Template

A production-ready, 12-Factor compliant FastAPI template.

---

## Quick Start

### 1.Clone the repo
```bash
git clone https://github.com/your-org/your-backend-template.git
cd your-backend-template

### 2.Create & activate virtual environment
###macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate
###Windows:
python -m venv .venv
.venv\Scripts\activate

### 3.Install 
pip install -e .

### 4.Run the app
uvicorn src.myapp.main:app --reload
