import json

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score

from reproml.config import ml_conf as mc


def validate(**kwargs):
    model_path = mc.root_path / mc.model_artifact_path

    test_df = pd.read_parquet(mc.root_path / mc.modeling_data_path / mc.test_set.filename)
    model = joblib.load(model_path)

    predicted = model.predict(test_df["lyric"])

    mat = confusion_matrix(test_df["ranker_genre"], predicted)
    precision = precision_score(test_df.ranker_genre, predicted, average="weighted")
    recall = recall_score(test_df.ranker_genre, predicted, average="weighted")
    f1 = f1_score(test_df.ranker_genre, predicted, average="weighted")
    tps = np.trace(mat)
    fps = (np.sum(mat, axis=0) - np.diagonal(mat)).sum()
    fns = (np.sum(mat, axis=1) - np.diagonal(mat)).sum()

    metrics = {
        "precision": precision.item(),
        "recall": recall.item(),
        "f1": f1.item(),
        "tps": tps.item(),
        "fns": fns.item(),
        "fps": fps.item(),
    }

    with open(mc.metrics.path, "w") as f:
        json.dump(metrics, f)
