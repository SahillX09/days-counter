from datetime import datetime

def main():
    
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    
    include_end = input("Should the end date be included? (yes/no): ").strip().lower()
    
    
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    
    delta = (end - start).days
    
   
    if include_end == "yes":
        delta += 1
    
    if delta < 0:
        print("The end date must be after the start date.")
    else:
        print(f"The total number of days is: {delta}")

if __name__ == "__main__":
    main()
