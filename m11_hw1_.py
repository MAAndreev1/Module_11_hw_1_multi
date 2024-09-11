import multiprocessing
import datetime


file_names = [f'./file/file {i}.txt' for i in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = 'start'
        while line:
            line = file.readline()
            all_data.append(line)


# start_only = datetime.datetime.now()
#
# for i in file_names:
#     read_info(i)
#
# end_only = datetime.datetime.now()
# print(f'{end_only - start_only} - Однопроцессорный режим') #  0:00:03.022685 - Однопоточный режим

if __name__ == '__main__':

    start_only = datetime.datetime.now()

    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, file_names)

    end_only = datetime.datetime.now()
    print(f'{end_only - start_only} - Многопроцессорный режим')  # 0:00:01.177999 - Многопроцессорный режим
