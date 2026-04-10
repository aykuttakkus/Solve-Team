import torch
import numpy as np
import random

DATASET_NAME = "Breast Cancer Dataset"
RANDOM_SEED = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2

def set_global_seed(seed=RANDOM_SEED):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
