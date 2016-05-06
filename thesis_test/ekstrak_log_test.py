import unittest
import thesis.ekstrak_log_dan_plot as el
import numpy as np

class Ekstrak_Log_Test(unittest.TestCase):
    # test ekstraks log file
    layer_epoch_cost_hasil = np.array([[1., 1., -3.],
                                       [1., 2., -2.5],
                                       [2., 3., -1.2],
                                       [2., 4., -1.0]])
    nama_file_log_test = "./dataset_test/log_test.log"


    def test_load_file_ekstrak_layer_epoch_cost(self):
        self.assertTrue(self.layer_epoch_cost_hasil.all(), el.load_file_ekstrak_layer_epoch_cost(self.nama_file_log_test).all())



if __name__ == '__main__':
    unittest.main()
