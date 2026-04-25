import pandas as pd
import matplotlib.pyplot as plt

def generate_chart():
    df = pd.read_csv("data.csv")

    if df.empty:
        print("No data to plot.")
        return

    summary = df.groupby("category")["amount"].sum()

    plt.figure()
    summary.plot(kind="bar")
    plt.title("Expenses by Category")
    plt.savefig("chart.png")

    print("📊 Chart saved as chart.png")