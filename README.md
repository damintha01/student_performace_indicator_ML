# Student Performance Indicator (End-to-End ML) — Flask + Docker + AWS CI/CD

An end-to-end Machine Learning project that predicts student performance from demographic and academic inputs.  
Includes a **Flask web app**, **ML prediction pipeline**, **Docker containerization**, and a **CI/CD workflow** for deployment on **AWS (ECR)**.

---

## Features
- **Web UI** to input student details and scores
- **ML inference pipeline** (`src/pipeline/predict_pipeline.py`)
- **Containerized app** with Docker for consistent runtime
- **CI/CD with GitHub Actions** to build (and optionally push) images to **AWS ECR**
- Production-friendly setup (separate runtime dependencies recommended)

---

## Tech Stack
- **Python 3.10**
- **Flask** (web server + templates)
- **Pandas / NumPy / Scikit-learn** (data + ML pipeline)
- **Docker** (build/run)
- **GitHub Actions** (CI/CD)
- **AWS ECR** (container registry)

---

## Project Structure
```text
student_performace_indicator_ML/
├─ app.py
├─ src/
│  └─ pipeline/
│     └─ predict_pipeline.py
├─ templates/
│  ├─ index.html
│  └─ home.html
├─ static/
│  └─ css/
│     └─ style.css
├─ requirements.txt
├─ requirements-prod.txt        # (recommended for Docker)
├─ Dockerfile
└─ .github/
   └─ workflows/
      └─ main.yaml
```

---

## Quickstart (Windows)

### 1) Create & activate venv
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Run the app
```powershell
python app.py
```
Open: `http://localhost:8080`

---

## Run with Docker

### Build
From the project root:
```powershell
docker build -t student-performance-ml:latest .
```

### Run
```powershell
docker run --rm -p 8080:8080 student-performance-ml:latest
```

---

## CI/CD (GitHub Actions → AWS ECR)

### What the pipeline does
- **CI**: lint/tests
- **Build**: builds Docker image
- **Push (optional/typical)**: pushes image to **Amazon ECR**
- **Deploy**: can run on a **self-hosted runner** (EC2/on-prem) to pull & run the image

### Required GitHub Secrets
Set these under **Repo → Settings → Secrets and variables → Actions**:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ACCOUNT_ID`
- `ECR_REPOSITORY_NAME`

Optional:
- `IMAGE_TAG` (if your workflow supports it; otherwise defaults to `latest`)

### Self-hosted runner note
If your workflow uses `runs-on: self-hosted`, ensure your runner is:
- Installed on the target machine
- **Online** and shows **Idle** in GitHub Runner settings

---

## Important Note (Form Mapping)
In `app.py`, the `reading_score` and `writing_score` values are currently swapped:

```py
reading_score=float(request.form.get('writing_score')),
writing_score=float(request.form.get('reading_score'))
```

If your HTML form uses the standard names (`reading_score` and `writing_score`), swap these to avoid incorrect predictions.  
If you want, I can provide the exact patch after you confirm your `home.html` form field names.

---

## Recommended Improvements
- Add real linting/tests (e.g., `ruff`, `pytest`)
- Add logging instead of `print()`
- Use `requirements-prod.txt` in Docker to reduce image size
- Add a `/health` endpoint for deployments (ALB/K8s readiness)
- Pin dependency versions for reproducible builds

---

## Screenshots / Proof (for LinkedIn / Portfolio)
Include:
- Web UI (input + result)
- GitHub Actions run (successful CI/CD)
- ECR repository image tag
- Deployed container running (EC2 / self-hosted runner)