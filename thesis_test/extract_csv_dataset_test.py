import unittest
from thesis.ekstrak_csv import Ekstraktor
from thesis.ekstrak_csv import Salah
from thesis.ekstrak_csv import Generator
import numpy as np
import filecmp
import gzip, cPickle

class Ekstraktor_Test(unittest.TestCase):
    ekstraktor = Ekstraktor()
    generator = Generator()
    def test_ekstraks_norm(self):
        self.ekstraktor.norm_dataset("./dataset_test/iris_dataset_test")
        self.assertTrue(filecmp.cmp("./dataset_test/iris_dataset_test_norm.csv", "./dataset_test/iris_dataset_norm_buattest.csv"))

    def test_generate_dataset(self):
        train=80.5
        valid = 14.5
        test = 5
        dataset = self.ekstraktor.generate_dataset("./dataset_test/iris_dataset_test_norm", "./dataset_test/iris_target_test",train,valid,test)
        [train_set, valid_set, test_set] = dataset
        self.assertEqual(train_set[0].shape[0],121)
        self.assertEqual(valid_set[0].shape[0], 22)
        self.assertEqual(test_set[0].shape[0], 5)


    def test_ambil_jumlah_dataset(self):
        self.data = np.genfromtxt("./dataset_test/iris_dataset_test.csv", dtype=float, delimiter=',')
        self.data = self.data.transpose()
        jumlah_data = self.ekstraktor.ambil_jumlah_dataset(self.data)
        self.assertEqual(jumlah_data,150)

    def test_ambil_train_valid_test(self):
        self.assertRaises(Salah, self.ekstraktor.ambil_train_valid_test,150,1,2,3)
        train,valid,test = self.ekstraktor.ambil_train_valid_test(100,80.5,14.5,5)
        self.assertEqual(train,81)
        self.assertEqual(valid,14)
        self.assertEqual(test,5)

    array_rank = np.array([2,3])
    dataset_test = np.array([[0., 1., 2.],
                            [3., 4., 5.],
                            [6., 7., 8.],
                            [9.,10.,11.]])
    data_target = np.array([0,1,2])

    data_hasil_rank = np.array([[6., 7., 8.],
                               [9.,10.,11.]])
    nama_file_target = "./dataset_test/index_top_n"



    def test_top_n_dataset(self):
        a  = self.generator.top_n_dataset(self.array_rank, self.dataset_test, self.nama_file_target )
        self.assertEqual(a.all(),self.data_hasil_rank.all())






if __name__ == '__main__':
    unittest.main()