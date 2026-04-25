import pandas as pd
from datetime import datetime
import os

FILE = "data.csv"

def init_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["date", "type", "category", "amount"])
        df.to_csv(FILE, index=False)

def add_entry(entry_type, category, amount):
    df = pd.read_csv(FILE)
    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": entry_type,
        "category": category,
        "amount": float(amount)
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(FILE, index=False)
    print("✅ Entry added successfully!")

def view_summary():
    df = pd.read_csv(FILE)
    if df.empty:
        print("No data available.")
        return

    income = df[df["type"] == "income"]["amount"].sum()
    expense = df[df["type"] == "expense"]["amount"].sum()

    print("\n📊 Summary:")
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Balance: {income - expense}")

def monthly_summary():
    df = pd.read_csv(FILE)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    summary = df.groupby(["month", "type"])["amount"].sum().unstack().fillna(0)
    print("\n📅 Monthly Summary:")
    print(summary)

def export_data():
    df = pd.read_csv(FILE)
    df.to_excel("expenses.xlsx", index=False)
    print("✅ Exported to expenses.xlsx")