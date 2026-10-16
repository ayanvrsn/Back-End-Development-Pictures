# Back-End-Development-Pictures

IBM Back-End Development Capstone implementation based on the official IBM Skills Network starter template. Original starter instructions are preserved in `IBM_STARTER_README.md`.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --port 5000
```

Run the official starter API tests with `pytest -v`. The starter uses in-memory data, so deploy one worker; changes reset on restart.

## Evidence and deployment status

`evidence/` contains actual captured command output from local verification. Local test success does not assert IBM Cloud deployment. Docker and Kubernetes files provide a deployment configuration; cloud rollout must be executed and checked separately. No cloud endpoint or screenshot is fabricated.
