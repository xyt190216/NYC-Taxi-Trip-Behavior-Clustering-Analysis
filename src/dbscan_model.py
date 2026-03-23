from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from data_preprocess import load_and_clean_data
from feature_engineering import feature_engineering

def run_dbscan():
    df = load_and_clean_data("../data_sample/taxi_sample.csv")
    df = feature_engineering(df)

    features = ["is_peak", "pu_freq", "total_amount", "extra_ratio", "fare_amount"]
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    dbscan = DBSCAN(eps=0.5, min_samples=10)
    labels = dbscan.fit_predict(X_scaled)

    df["cluster"] = labels

    print(df["cluster"].value_counts())

if __name__ == "__main__":
    run_dbscan()