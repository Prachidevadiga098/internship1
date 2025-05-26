
import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Step 1: Handle missing values
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Not Specified')
df['cast'] = df['cast'].fillna('Not Specified')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Standardize text fields
df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.lower().str.strip()
df['rating'] = df['rating'].str.upper().str.strip()

# Step 4: Convert date format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

# Step 5: Rename columns
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# Step 6: Fix data types
df['release_year'] = df['release_year'].astype(int)

# Step 7: Save cleaned dataset
df.to_csv('netflix_titles_cleaned.csv', index=False)

print("Cleaning complete. File saved as 'netflix_titles_cleaned.csv'")
