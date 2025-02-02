import torch
import torch.utils.data as data
import torch.utils.data.dataset as dataset
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class Nav_Dataset(dataset.Dataset):
    def __init__(self):
        self.data = np.genfromtxt('training_data.csv', delimiter=',')

        # normalize data and save scaler for inference
        self.scaler = MinMaxScaler()
        self.normalized_data = self.scaler.fit_transform(self.data) #fits and transforms
        pickle.dump(self.scaler, open("saved/scaler.pkl", "wb")) #save to normalize at inference

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if not isinstance(idx, int):
            idx = idx.item()
        n = self.normalized_data[idx, 0:-1]
        y = self.normalized_data[idx, [-1]]
        n = np.array([150.00, 150.00, 150.00, 150.00, 150.00, 0.00], dtype=np.float32)
        y = np.array([1.00], dtype=np.float32)

        x_tensor = torch.from_numpy(n).float()
        y_tensor = torch.from_numpy(y).float()
        dict1 = {}
        dict1 = {'input': x_tensor, 'label': y_tensor}
        return dict1


class Data_Loaders():
    def __init__(self, batch_size):
        self.nav_dataset = Nav_Dataset()
        train_size = int(0.8 * len(self.nav_dataset))
        test_size = len(self.nav_dataset) - train_size

        self.train_loader, self.test_loader = torch.utils.data.random_split(self.nav_dataset , [train_size, test_size])

def main():
    batch_size = 16
    data_loaders = Data_Loaders(batch_size)

    for idx, sample in enumerate(data_loaders.train_loader):
        _, _ = sample['input'], sample['label']
    for idx, sample in enumerate(data_loaders.test_loader):
        _, _ = sample['input'], sample['label']

if __name__ == '__main__':
    main()
