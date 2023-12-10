import pickle
import gzip


input_pkl_file_path = 'D:\mine\Codsoft\CODSOFT\Task_4\pickled\similarity.pkl'
output_gzip_file_path = 'D:\mine\Codsoft\CODSOFT\Task_4\pickled\similarity.pkl.gz'


with open(input_pkl_file_path, 'rb') as pkl_file:
    data = pickle.load(pkl_file)


with gzip.open(output_gzip_file_path, 'wb') as gzip_file:
    pickle.dump(data, gzip_file)
