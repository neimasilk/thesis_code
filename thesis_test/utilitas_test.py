import unittest
import numpy as np

import thesis.utilitas as tsk

class Tambah_Satu_Kolom_Array_Test(unittest.TestCase):
    a = np.array([[1,2],
                 [3,4]])
    b = np.array([5,6])
    hasil_a_add_b = np.array([[1, 2, 5],
                              [3,4,6]])
    hasil_test_error = np.array([1, 2, 3, 4])
    hasil_tambah_baris_a_add_b = np.array([[1,2],
                                           [3,4],
                                           [5,6]])
    def test_tambah_satu_kolom(self):
        self.assertEqual(tsk.tambah_satu_kolom(self.a,self.b).all(), self.hasil_a_add_b.all())

    def test_tambah_satu_baris(self):
        self.assertEqual(self.hasil_tambah_baris_a_add_b.all(),tsk.tambah_satu_baris(self.a,self.b).all())

    def test_baris_shape_error(self):
        self.assertRaises(tsk.Baris_Tidak_Sama, tsk.tambah_satu_baris, self.a, self.hasil_test_error)

    def test_kolom_shape_error(self):
        self.assertRaises(tsk.Kolom_Tidak_Sama, tsk.tambah_satu_kolom, self.a, self.hasil_test_error)

    array_rank = np.array([2, 3])
    dataset_test = np.array([[0., 1.,  2.],
                             [3., 4.,  5.],
                             [6., 7.,  8.],
                             [9., 10.,11.]])
    dataset_target = np.array([0, 1, 2])

    data_hasil_rank = np.array([[6., 7., 8.],
                                [9., 10., 11.]])


    def test_top_n_dataset(self):
        a = tsk.top_n_dataset(self.array_rank, self.dataset_test)
        self.assertEqual(a.all(), self.data_hasil_rank.all())


if __name__ == '__main__':
    unittest.main()