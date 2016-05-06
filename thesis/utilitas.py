import numpy as np

class Kolom_Tidak_Sama(Exception):
    pass

class Baris_Tidak_Sama(Exception):
    pass

def tambah_satu_kolom(a, b):
    if a.shape[0]!=b.shape[0]:
        raise Kolom_Tidak_Sama
    return np.c_[a,b]

def tambah_satu_baris(a, b):
    if a.shape[1]!=b.shape[0]:
        raise Baris_Tidak_Sama
    return np.r_[a,[b[:]]]

def top_n_dataset(array_rank, dataset_test):
    # kembalian nilai data hasil , data targetnya
    data_hasil = np.array([dataset_test[array_rank[0]]])
    panjang_vektor = array_rank.shape[0]
    for i in range(1,panjang_vektor):
        data_hasil = tambah_satu_baris(data_hasil, dataset_test[array_rank[i]])
    return data_hasil

if __name__ == '__main__':
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([5, 6])
    a_add_b = np.array([[1, 2, 3, 5],
                        [4, 5, 6, 7]])
    c = np.array([1, 2, 3])
    d = tambah_satu_kolom(a,b)

    # test kedua
    array_rank = np.array([2, 3])
    dataset_test = np.array([[0., 1., 2.],
                             [3., 4., 5.],
                             [6., 7., 8.],
                             [9., 10., 11.]])
    dataset_target = np.array([0, 1, 2])

    data_hasil_rank = np.array([[6., 7., 8.],
                                [9., 10., 11.]])
    data_hasil_rank_target = np.array([1, 2])


