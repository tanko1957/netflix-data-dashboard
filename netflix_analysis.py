import pandas as pd 
from pymongo import MongoClient

# 1. Load and analyze the dataset
df = pd.read_csv('netflix_titles.csv')

summary = {
    'total_entries': len(df),
    'type_counts': df['type'].value_counts().to_dict(),
    'top_countries': df['country'].value_counts().head(5).to_dict(),
    'top_genres': df['listed_in'].value_counts().head(5).to_dict(),
    'release_year_distribution': {
        str(k): v for k, v in df['release_year'].value_counts().sort_index().items()
    }
}

# 2. Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://Adam:Canada2024@cluster0.reb1ins.mongodb.net/netflixDB?retryWrites=true&w=majority&appName=Cluster0')
db = client['netflixDB']
collection = db['stats']

# 3. Insert summary
collection.delete_many({})  # Optional: clear old data
collection.insert_one(summary)

print(" Summary data inserted into MongoDB.")
