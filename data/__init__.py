import importlib
from data.dataset.base_dataset import BaseDataset


def find_dataset_using_name(dataset_name):
    dataset_filename = "data.dataset.aligned_dataset"
    datasetlib = importlib.import_module(dataset_filename)

    dataset = None
    target_dataset_name = dataset_name.replace('_', '') + 'dataset'
    for name, cls in datasetlib.__dict__.items():
        if name.lower() == target_dataset_name.lower():
            dataset = cls

    if dataset is None:
        print("In %s.py, there should be a subclass of BaseDataset with class name that matches %s in lowercase." % (
        dataset_filename, target_dataset_name))
        exit(0)

    return dataset
