# 🧠 **CM TruckEst Backend System Outline**

This is a RESTful + AI + Image-based processing system.  
It’s powered by a **Tower API Server**, **Raspberry Pi model server**, and optional **Cloud Training Pipeline**.

---

## 🔧 **PHASE 1: LOCAL API MACHINE SETUP (THE TOWER)**

### ✅ GOAL: FastAPI-based REST API that manages:
- Uploads
- Communication with Pi
- Local database
- Prepares data for retraining

### ✅ TO-DO:
#### 1. Set Up FastAPI Project (Already in Progress ✅)
- [ ] `start.sh` script (✅)
- [ ] `requirements.txt` (✅)
- [ ] `main.py`, `routes/`, `models.py`, `schemas.py`

#### 2. Build Database & Config
- [ ] `.env` file
- [ ] `config.py` to load from `.env`
- [ ] `database.py` for PostgreSQL connection
- [ ] Define tables:
  - `Estimate`
  - `Feedback`
  - (Optional) `Client`, `ImageMeta`, `ModelVersions`

#### 3. Create RESTful Endpoints
- [ ] `POST /estimate/` → Upload image + form
- [ ] `GET /estimate/{id}` → Fetch single estimate
- [ ] `POST /feedback/` → Save client/shop feedback
- [ ] `GET /estimates/` → Admin-only endpoint
- [ ] `GET /ping` → Healthcheck

#### 4. Services
- [ ] `services/yolo_client.py` → Send image to Pi
- [ ] `services/llm_client.py` → Send form + yolo result to LLM
- [ ] Save output JSON + Summary in DB

#### 5. Storage & Backups
- [ ] Mount external HDD at `/mnt/cmtruckest-data/`
- [ ] Store:
  - `/images/`
  - `/yolo_outputs/`
  - `/llm_outputs/`
  - `/weekly_training_dumps/`
- [ ] Schedule cron job to:
  - Export DB backup nightly
  - Archive files weekly

---

## 🧠 **PHASE 2: RASPBERRY PI MODEL SERVER**

### ✅ GOAL: Handle model inference locally for:
- YOLOv8 for image detection
- LLM for summary generation

### ✅ TO-DO:
#### 1. YOLOv8 Setup
- [ ] Install Python, torch, ultralytics
- [ ] Run YOLOv8n model via `infer.py`
- [ ] Expose API endpoint (`POST /yolo/`)

#### 2. LLM Setup (via Ollama or GPT4All)
- [ ] Install Ollama
- [ ] Pull small model (Phi3, TinyLlama)
- [ ] Setup endpoint (`POST /llm/`)
- [ ] Return human-readable summary

#### 3. Pi FastAPI App
- [ ] lightweight `main.py`
- [ ] `POST /yolo/` for images
- [ ] `POST /llm/` for summary requests

#### 4. Model Boot Scripts
- [ ] Autoload model on Pi boot
- [ ] Cron job to pull updated models from API server

---

## ☁️ **PHASE 3: CLOUD TRAINING PIPELINE**

### ✅ GOAL: Periodic retraining of YOLO and/or LLM using collected data

### ✅ TO-DO:
#### 1. Choose Cloud Provider
- [ ] RunPod.io, Colab Pro, Vast.ai, etc.

#### 2. Export Training Data
- [ ] Weekly `.zip` dump of:
  - Images
  - YOLO labels
  - LLM prompts/responses

#### 3. YOLOv8 Training
- [ ] Format dataset
- [ ] Train & download new `.pt` model

#### 4. LLM Fine-Tuning
- [ ] Convert feedback + estimate data to prompt/response pairs
- [ ] Use `ollama tune` or `ggml fine-tune`

#### 5. Deployment
- [ ] Upload to Pi `/models/yolo/vX.pt`, `/models/llm/vX.gguf`
- [ ] Auto-reload models on boot or via admin endpoint

---

## 💾 **PHASE 4: VECTOR DATABASE (OPTIONAL)**

### ✅ GOAL: Store past jobs in a way that’s searchable by similarity for future recall

- [ ] Use `ChromaDB`, `Weaviate`, or `FAISS` on the Tower
- [ ] Embed YOLO + LLM results (convert to vectors)
- [ ] Store to search for:
  - Similar jobs
  - Cross-shop analytics

---

## 🔐 **PHASE 5: ADMIN DASHBOARD / AUTH (LATER)**

- [ ] Admin login
- [ ] View all estimates, feedback, files
- [ ] Trigger retraining manually
- [ ] Upload new models

---

## 📝 **Final Dev Notes**

| Piece | Lives On | Notes |
|-------|----------|-------|
| FastAPI REST API | Tower | Handles client interaction & database |
| YOLOv8 | Pi | Inference-only |
| LLM | Pi | Summarization |
| Database | Tower (Postgres) | All image + feedback data |
| Model Training | Cloud | Only used weekly, manual/auto |
| External Storage | Tower | Mounted HDD, holds all file dumps |

---

## ✅ Next Steps Right Now:
1. Create `.env` file  
2. Build `config.py`  
3. Build `database.py`  
4. Create `models.py` (Estimate, Feedback)  
5. Finish `/estimate/` route to actually work end-to-end
