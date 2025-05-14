# Dynamic Audience Segmentation via Online Clustering

An end-to-end prototype for real-time audience segmentation using online clustering algorithms. Ingest sessionized clickstream or transaction data, extract features on the fly, and cluster each user session incrementally with both River and scikit-learn models.

---

## 🚀 Features

* **Streaming Simulation**
  Read pre-processed session data in small batches to mimic real-time arrival.
* **Feature Engineering**
  Session-level metrics: total items, total value, unique products, session duration, hour of day.
* **Multiple Clustering Models**

  * **River KMeans** for fully online, one-observation-at-a-time learning
  * **scikit-learn MiniBatchKMeans** for batch-based incremental updates
  * *(Optional)* River DenStream for density-based clustering (commented out)
* **Visualization**
  Centroid drift plots to monitor how clusters evolve over time.
* **Modular Codebase**
  Clean separation of streaming, feature engineering, modeling, visualization, and configuration.

---

## 📁 Directory Structure

```
dynamic-audience-segmentation/
├── data/
│   ├── raw/                  # raw source files (e.g. online_retail.xlsx)
│   └── processed/            # cleaned & sessionized CSVs
│
├── notebooks/
│   └── prototyping_final.ipynb  # end-to-end prototype flow
│
├── src/
│   ├── config.py             # hyperparameters & file paths
│   ├── main.py               # orchestrates streaming → clustering → viz
│   ├── data/
│   │   └── stream.py         # batch generator for streaming sessions
│   ├── features/
│   │   └── engineer.py       # extract_features() function
│   ├── models/
│   │   └── online_cluster.py # OnlineClustering wrapper with multiple algorithms
│   └── utils/
│       ├── viz.py            # centroid drift plotting
│       └── metrics.py        # optional evaluation helpers
│
├── requirements.txt          # Python dependencies
├── README.md                 # this file
└── .gitignore
```

---

## ⚙️ Prerequisites

* Python 3.8 or later
* `virtualenv` or `venv` for environment isolation

---

## 📥 Installation

1. **Clone the repo**

   ```bash
   git clone https://your.repo.url/dynamic-audience-segmentation.git
   cd dynamic-audience-segmentation
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate.bat       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃‍♂️ Usage

### 1. Prepare your data

* Place your raw Excel file in `data/raw/online_retail.xlsx`.
* Run the notebook to clean, sessionize, and export to `data/processed/sessions.csv`:

  1. Launch Jupyter:

     ```bash
     jupyter lab
     ```
  2. Open `notebooks/prototyping_final.ipynb` and execute all cells.

### 2. Run the prototype script

```bash
python src/main.py
```

* Streams your session CSV in batches.
* Fits River KMeans and MiniBatchKMeans incrementally.
* Renders centroid drift plots at the end.

---

## 🔧 Configuration

All “knobs” live in `src/config.py`:

* `STREAM_BATCH_SIZE` & `STREAM_SLEEP_SEC`
* `N_CLUSTERS`
* `PROCESSED_DATA_PATH`

Tweak these constants to suit your data volume and experimenting pace.

---

## 📈 Next Steps & Extensions

* **Real Data Streams**: Swap `stream_batches()` to read from Kafka, Kinesis, or Pub/Sub.
* **Additional Models**: Plug in other River algorithms (e.g. DenStream, DBSTREAM) or online neural nets.
* **Dashboard**: Build a Streamlit or Dash UI to visualize clusters, segment composition, and concept drift live.
* **Evaluation & Alerts**: Integrate silhouette scoring, waterfall charts, or drift detectors with email or Slack notifications.

