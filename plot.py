import pandas


def data_clean(n_times=10, csv_file=None):
    if csv_file is None:
        return

    # read from the csv files
    df_origin = pandas.read_csv(csv_file, names=list(range(1, n_times + 1, 1)))

    # data filtering
    df = df_origin[(df_origin > 0).all(1)]

    # generate mean values and standard derivation
    data = df.agg(['mean', 'std'])

    return data.T


if __name__ == '__main__':
    N_TIMES = 10
    N_LOOP = 50
    csv_file_suffix = ".csv"
    non_busy_waiting_file_prefix = "statistics_non-busy-waiting_"
    busy_waiting_file_prefix = "statistics_busy-waiting_"

    b_file = busy_waiting_file_prefix + str(N_LOOP) + csv_file_suffix
    n_b_file = non_busy_waiting_file_prefix + str(N_LOOP) + csv_file_suffix
    s1 = data_clean(n_times=N_TIMES, csv_file=n_b_file)
    s2 = data_clean(n_times=N_TIMES, csv_file=n_b_file)
