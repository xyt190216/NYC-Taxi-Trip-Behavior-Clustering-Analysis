from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

from data_preprocess import load_and_clean_data
from feature_engineering import feature_engineering

def run_kmeans():
    df = load_and_clean_data("../20230301_Yellow_Taxi_Trip_Data.csv")
    df = feature_engineering(df)

    features = ["is_peak", "pu_freq", "total_amount", "extra_ratio", "fare_amount"]
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=5, random_state=42)
    labels = kmeans.fit_predict(X_scaled)

    df["cluster"] = labels

    print(df["cluster"].value_counts())

if __name__ == "__main__":
    run_kmeans()