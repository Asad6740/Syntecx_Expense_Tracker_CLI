import argparse
from tracker import init_file, add_entry, view_summary, monthly_summary, export_data
from utils import generate_chart

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    parser.add_argument("--add", nargs=3, metavar=("TYPE", "CATEGORY", "AMOUNT"),
                        help="Add entry: income/expense category amount")

    parser.add_argument("--summary", action="store_true", help="Show summary")
    parser.add_argument("--monthly", action="store_true", help="Monthly summary")
    parser.add_argument("--export", action="store_true", help="Export to Excel")
    parser.add_argument("--chart", action="store_true", help="Generate chart")

    args = parser.parse_args()

    init_file()

    if args.add:
        entry_type, category, amount = args.add
        add_entry(entry_type, category, amount)

    elif args.summary:
        view_summary()

    elif args.monthly:
        monthly_summary()

    elif args.export:
        export_data()

    elif args.chart:
        generate_chart()

    else:
        print("Use --help for commands")

if __name__ == "__main__":
    main()