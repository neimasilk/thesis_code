# # testing  fungsi generate dataset
#
# import numpy as np
# train = 80.5
# valid = 14.5
# test = 5
# from thesis.ekstrak_csv import Ekstraktor
# ekstraktor = Ekstraktor()
# dataset = ekstraktor.generate_dataset("./thesis_test/dataset_test/iris_dataset_test_norm", "./thesis_test/dataset_test/iris_target_test", train, valid, test)
#
#
# #testing dalam generate
# import numpy as np
# from thesis.ekstrak_csv import Ekstraktor
# ekstraktor = Ekstraktor()
# data = np.genfromtxt("./thesis_test/dataset_test/iris_dataset_test_norm.csv", dtype=float, delimiter=',')
# y = np.genfromtxt("./thesis_test/dataset_test/iris_target_test.csv", dtype=float, delimiter=',')
# data = data.transpose()
# jumlah_data = ekstraktor.ambil_jumlah_dataset(data)
#
#
# # untuk loadang mnist.pkl.gz
# import theano.tensor as T
# import numpy
# from thesis.logistic_sgd import LogisticRegression, load_data
# dataset = load_data("./mnist.pkl.gz")
#
# dataset = load_data("./thesis/dataset/iris_dataset_norm.csv_dataset.pkl.gz")
#
# # testing ekstrak ranking
# import numpy as np
# from thesis.ekstrak_csv import Ekstraktor
# from thesis.ekstrak_csv import Generator
# array_rank = np.array([2,3])
# dataset_test = np.array([[0., 1., 2.],
#                             [3., 4., 5.],
#                             [6., 7., 8.],
#                             [9.,10.,11.]])
# data_target = np.array([0,1,2])
#
# data_hasil_rank = np.array([[6., 7., 8.],
#                                [9.,10.,11.]])
# data_hasil_rank_target = np.array([1,2])
# nama_file_target = "./thesis_test/dataset_test/index_top_n""
# generator = Generator()
# a , b = generator.top_n_dataset(array_rank, dataset_test, data_target, nama_file_target )
#
# # ekstrak file log
#
# # todo:
# # 1. ambil index top n dan generate menjadi dataset x
# #   * generate_top_n_dataset(data_rank,dataset) = return = generated data
# # 2. plot antara epoch dengan cost-nya x
# # 3. plot diagram venn top n 1 dengan top n 2 x
# # * tata file log sesuai dengan nama modelnya x
# # * buat diagram venn untuk top 50 x
# # * buat plot per layer setiap percobaan x
# # 4. ANN untuk top N
# # buat algoritma di laporan
# # pindah semua kode kedalam refactor

