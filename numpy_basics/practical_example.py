import matplotlib.pyplot as plt
import numpy as np

# Dataset schema:
# Column 0: User_ID
# Column 1: Time-to-First-Token (TTFT) in milliseconds
# Column 2: Total_Tokens_Generated
# Column 3: Server_Load_Percentage (0-100)
# Column 4: Total_Latency in milliseconds

llm_logs = np.array(
    [
        [101, 250, 1500, 45, 1200],
        [102, 180, 250, 30, 400],
        [103, 850, 4000, 92, 5500],
        [104, 210, 800, 50, 850],
        [105, 900, 150, 95, 1100],
        [106, 195, 3000, 60, 2900],
        [107, 220, 500, 40, 600],
        [108, 950, 4500, 98, 6200],
        [109, 240, 1200, 55, 1300],
        [110, 810, 50, 88, 950],
    ]
)


def main():
    # MatPlotlib Practice
    # cumulativeSum = np.cumsum(llm_logs,axis=1)
    # plt.figure(figsize=(10,6))
    # plt.plot(np.mean(cumulativeSum,axis=0))
    # plt.title("Average of cumalative")
    # plt.xlabel("Token")
    # plt.ylabel("Cost")
    # plt.show()

    # 1. Slicing & Extraction
    # mask = [False,False, True, False, True]
    # t_l = llm_logs[:,mask]
    # print(t_l)

    # 2. Vectorized Math (Feature Engineering)

    # a.) Generation time
    generation_time = llm_logs[:, 4] - llm_logs[:, 1]
    print(generation_time)

    # b.) Tokens per second
    tokens_per_second = llm_logs[:, 2] / generation_time
    print(tokens_per_second)

    # 3. Boolean Masking (Anomaly Detection)

    filtered_server_data = llm_logs[llm_logs[:, 3] > 80]
    print(filtered_server_data)

    condition_load = (llm_logs[:, 1] > 800) & (llm_logs[:, 2] < 500)
    filtered_load_data = llm_logs[condition_load]
    print(filtered_load_data)

    # 4. Aggregations (SLA Monitoring)

    print(np.mean(llm_logs[:, 1]))

    # percentile
    threshold = np.percentile(llm_logs[:, 3], 90)
    print(threshold)

    # 5. Broadcasting (Machine Learning Preprocessing)

    mean_server_load = np.mean(llm_logs[:, 3])
    std_server_load = np.std(llm_logs[:, 3])
    normalized_op = (llm_logs[:, 3] - mean_server_load) / std_server_load
    print(normalized_op)


if __name__ == "__main__":
    main()
