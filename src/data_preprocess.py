import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # 去掉异常数据（模拟你awk逻辑）
    df = df[
        (df["trip_distance"] > 0) &
        (df["fare_amount"] > 0) &
        (df["total_amount"] > 0)
    ]

    return df

if __name__ == "__main__":
    df = load_and_clean_data("../data_sample/taxi_sample.csv")
    print(df.head())