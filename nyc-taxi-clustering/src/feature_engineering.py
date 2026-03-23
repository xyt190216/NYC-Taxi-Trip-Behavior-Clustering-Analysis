import pandas as pd

def feature_engineering(df):
    # 时间特征
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["hour"] = df["pickup_datetime"].dt.hour
    df["is_peak"] = df["hour"].apply(lambda x: 1 if 17 <= x <= 19 else 0)

    # 空间特征（pu_freq）
    freq = df["pu_Location_id"].value_counts(normalize=True)
    df["pu_freq"] = df["pu_Location_id"].map(freq)

    # 费用结构
    df["extra_ratio"] = (df["total_amount"] - df["fare_amount"]) / df["total_amount"]

    return df

if __name__ == "__main__":
    from data_preprocess import load_and_clean_data
    df = load_and_clean_data("../data_sample/taxi_sample.csv")
    df = feature_engineering(df)
    print(df.head())