import matplotlib.pyplot as pyplot
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


def compare_performance(data1, data2):
    n_rows = len(data1.index)
    X = list(range(1, n_rows + 1, 1))
    non_busy_means = data1['mean'].tolist()
    busy_means = data2['mean'].tolist()
    # non_busy_stdev = data1['std'].tolist()
    # busy_stdev = data2['std'].tolist()

    # # figure1
    figure1 = pyplot.figure(1)
    pyplot.plot(X, non_busy_means, label="non-busy-waiting", marker='.', linestyle='--', linewidth='1')
    # pyplot.errorbar(X, non_busy_means, non_busy_stdev, fmt='none')
    pyplot.plot(X, busy_means, label="busy-waiting", marker='.', linestyle='--', linewidth='1')
    # pyplot.errorbar(X, busy_means, busy_stdev, fmt='none')

    # plot decoration
    pyplot.title("Performance Analysis")
    pyplot.xlabel("How many times the process C has consumed")
    pyplot.ylabel("The accumulative elapsed time (in nanosecond)")
    pyplot.legend(loc="upper left")
    pyplot.grid()
    pyplot.xlim(0, 11)

    # show the plot
    pyplot.show()

    # export the figure
    figure1.savefig("Performance_of_two_kinds_of_implementation.png")


if __name__ == '__main__':
    N_TIMES = 10
    N_LOOP = 50
    csv_file_suffix = ".csv"
    non_busy_waiting_file_prefix = "statistics_non-busy-waiting_"
    busy_waiting_file_prefix = "statistics_busy-waiting_"

    b_file = busy_waiting_file_prefix + str(N_LOOP) + csv_file_suffix
    n_b_file = non_busy_waiting_file_prefix + str(N_LOOP) + csv_file_suffix
    s1 = data_clean(n_times=N_TIMES, csv_file=n_b_file)
    s2 = data_clean(n_times=N_TIMES, csv_file=b_file)
    compare_performance(data1=s1, data2=s2)
