import pandas as pd
import scipy.stats as stats
import streamlit as st
import time

# -----------------------------
# Session State Initialization
# -----------------------------
if "experiment_no" not in st.session_state:
    st.session_state["experiment_no"] = 0

if "df_experiment_results" not in st.session_state:
    st.session_state["df_experiment_results"] = pd.DataFrame(
        columns=["Experiment", "Iterations", "Mean"]
    )

# -----------------------------
# App Title
# -----------------------------
st.title("🪙 Coin Toss Experiment")
st.write(
    "Simulate coin tosses and observe how the average converges toward **0.5** over time."
)

# Initial chart baseline
chart = st.line_chart([0.5])

# -----------------------------
# Simulation Function
# -----------------------------
def toss_coin(n):
    outcomes = stats.bernoulli.rvs(p=0.5, size=n)

    running_mean = 0
    ones_count = 0

    progress_bar = st.progress(0)

    for i, result in enumerate(outcomes, start=1):
        if result == 1:
            ones_count += 1

        running_mean = ones_count / i
        chart.add_rows([running_mean])

        progress_bar.progress(i / n)

        # Slow animation only for small experiments
        if n <= 200:
            time.sleep(0.02)

    return running_mean

# -----------------------------
# User Controls
# -----------------------------
number_of_trials = st.slider("Number of tosses:", 1, 1000, 50)
start_button = st.button("Run Experiment")

# -----------------------------
# Run Experiment
# -----------------------------
if start_button:
    st.session_state["experiment_no"] += 1

    st.write(f"Running experiment with **{number_of_trials}** tosses...")

    with st.spinner("Simulating coin tosses..."):
        mean = toss_coin(number_of_trials)

    # Save results
    new_row = pd.DataFrame(
        [[st.session_state["experiment_no"], number_of_trials, mean]],
        columns=["Experiment", "Iterations", "Mean"],
    )

    st.session_state["df_experiment_results"] = pd.concat(
        [st.session_state["df_experiment_results"], new_row],
        ignore_index=True,
    )

    st.success("Experiment completed!")

# -----------------------------
# Results Table
# -----------------------------
st.subheader("Experiment Results")
st.dataframe(st.session_state["df_experiment_results"])
