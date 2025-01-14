import random
import pandas as pd

# Generate 100 data points
data = []
for _ in range(100):
    percentage_all = random.uniform(50, 100)  # Random percentage between 50% and 100%
    # percentage_school within ±10% of percentage_all
    percentage_school = percentage_all + random.uniform(-10, 10)
    # Calculate performance as the difference
    performance = percentage_school - percentage_all
    # Append to dataset
    data.append({
        "percentage_all": round(percentage_all, 2),
        "percentage_school": round(percentage_school, 2),
        "performance": round(performance, 2),
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("school_performance_data.csv", index=False)

print("Generated dataset saved as 'school_performance_data.csv'")
