import pandas as pd

def analyze_employee_data(file_path):
    try:
        # 1. Load the dataset
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")

        # 2. Calculate average PaymentTier (instead of Salary)
        avg_tier = df['PaymentTier'].mean()
        print(f"Average Payment Tier: {avg_tier:.2f}")

        # 3. Department/City count (using City instead of Department)
        city_count = df['City'].value_counts()
        print("\nEmployee count per City:")
        print(city_count)

        # 4. Filter employees (PaymentTier < 3 for this example)
        # Assuming Tier 1 or 2 might be the threshold you want to analyze
        high_performers = df[df['PaymentTier'] < 3]
        
        # 5. Export results
        high_performers.to_csv('filtered_employees.csv', index=False)
        print("\nFiltered data saved to 'filtered_employees.csv'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in dataset: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure this matches your filename exactly
    analyze_employee_data('Employees.csv')