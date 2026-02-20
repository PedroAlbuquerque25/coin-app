# 🪙 Coin Toss Experiment: Law of Large Numbers Visualizer

### Interactive Statistical Simulation built with Python & Streamlit

This project is an interactive dashboard that simulates coin tosses and visualizes 
how the running average converges toward **0.5** as the number of trials increases — 
demonstrating the **Law of Large Numbers** in real time.

🔗 **Live Demo:** https://coin-app-yhlyxki9slxqvz8tyeofwl.streamlit.app

---

### 🛠️ Tech Stack:

- **Python** — Core simulation logic using `SciPy` (Bernoulli distribution) and `Pandas`
- **Streamlit** — Interactive UI with real-time chart updates and session management
- **Streamlit Cloud** — Live deployment and hosting

---

### 📊 What it does:

1. **Simulates** coin tosses using a Bernoulli distribution (`p=0.5`)
2. **Tracks** the running mean across all tosses in real time
3. **Persists** experiment history across multiple runs using Streamlit Session State
4. **Visualizes** convergence behavior through a live-updating line chart

---

### 📁 Repository Structure:

├── .streamlit/        # Custom theme and platform settings
├── .devcontainer/     # Standardized dev environment for Codespaces
├── app.py             # Core application logic and Streamlit UI
├── requirements.txt   # Dependencies (Pandas, SciPy, Streamlit)
└── README.md          # Project documentation

---

### 🚀 How to Run Locally:
```bash
git clone https://github.com/PedroAlbuquerque25/coin-app.git
cd coin-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🤝 Contact
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/phaa/)