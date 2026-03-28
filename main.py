from utils import load_data, save_data, calculate_score
from datetime import date

def main():
    while True:
        print("\n--- Procrastination Tracker ---")
        print("1. Add today's data")
        print("2. View records")
        print("3. Show analysis")
        print("4. Clear all data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = load_data()

            planned = float(input("Enter planned study hours: "))
            studied = float(input("Enter actual study hours: "))

            wasted = max(0, planned - studied)

            if studied >= planned:
                print("🎉 You completed your goal!")
            else:
                print("📉 Goal not achieved today")

            if wasted > 3:
                print("⚠️ You wasted a lot of time today. Try to focus more!")

            entry = {
                "date": str(date.today()),
                "planned": planned,
                "studied": studied,
                "wasted": wasted
            }

            data.append(entry)
            save_data(data)

            score = calculate_score(planned, studied)
            print(f"\nScore: {score}%")

            if score > 80:
                print("😎 Excellent! You were very productive today!")
            elif score > 50:
                print("🙂 Not bad, try to reduce distractions.")
            else:
                print("⚠️ Low productivity today. Focus more tomorrow!")

        elif choice == "2":
            data = load_data()
            if len(data) == 0:
                print("No records found")
            else:
                for e in data:
                    print(f"\nDate: {e['date']}")
                    print(f"Planned: {e['planned']} hrs")
                    print(f"Studied: {e['studied']} hrs")
                    print(f"Wasted: {e['wasted']} hrs")

        elif choice == "3":
            data = load_data()
            if len(data) == 0:
                print("No data available")
            else:
                total_score = 0
                best = -1
                best_day = ""
                worst = 101
                worst_day = ""

                for e in data:
                    score = calculate_score(e['planned'], e['studied'])
                    total_score += score
                    if score > best:
                        best = score
                        best_day = e['date']
                    if score < worst:
                        worst = score
                        worst_day = e['date']

                avg = total_score / len(data)
                print(f"Days tracked: {len(data)}")
                print(f"Average productivity: {round(avg,2)}%")
                print(f"🔥 Best day: {best}% on {best_day}")
                print(f"⚠️ Worst day: {worst}% on {worst_day}")

        elif choice == "4":
            save_data([])
            print("All data cleared!")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()