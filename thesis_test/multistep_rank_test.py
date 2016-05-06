import unittest

import thesis.multistep_rank as mlt

class Multistep_Rank_Test(unittest.TestCase):
    # w1 adalah bobot untuk testing
    w1 = np.array([[0, 1, 2, 3, 4],
                   [5, 6, 7, 8, 9],
                   [10, 11, 12, 13, 14]])
    a = np.array([1., 1., 1., 1., 1.])
    x = np.array([10., 35., 60.])
    y = np.array([[  2.,  60.],
                  [  1.,  35.],
                  [  0.,  10.]])
    z = np.array([[ 0.,  0.],
                  [ 1.,  1.],
                  [ 2.,  1.]])

    def test_awal(self):
        self.assertEqual(self.a.all(),mlt.awal(self.w1).all())

    def test_jumlah_bobot(self):
        self.assertEqual(self.x.all(),mlt.jumlah_bobot(self.w1, self.a).all())

    def test_rank_hasil_jumlah(self):
        self.assertEqual(self.y.all(),mlt.rank_hasil_jumlah(self.x).all())

    def test_set_top_n(self):
        self.assertEqual(self.z.all(),mlt.set_top_n(self.z,2).all())




if __name__ == '__main__':
    unittest.main()