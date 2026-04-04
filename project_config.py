"""Shared configuration for the Breast Cancer Wisconsin project."""

from __future__ import annotations

import random

import numpy as np
import torch


RANDOM_SEED = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2
TARGET_COLUMN = "target"
DATASET_NAME = "Breast Cancer Wisconsin"


def set_global_seed(seed: int = RANDOM_SEED) -> int:
    """Apply a reproducible seed across Python, NumPy and PyTorch."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    if torch.backends.cudnn.is_available():
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    return seed
