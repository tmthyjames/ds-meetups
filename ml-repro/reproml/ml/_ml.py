import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from reproml.config import ml_conf as mc


def train(
    srcpath: str = (mc.root_path / mc.modeling_data_path / mc.train_set.filename),
    dstpath: str = mc.root_path / mc.model_artifact_path,
    **kwargs
):

    train_df = pd.read_parquet(srcpath)

    # define our model
    text_clf = Pipeline([("vect", TfidfVectorizer()), ("clf", MultinomialNB(alpha=0.1))])

    # train our model on training data
    text_clf.fit(train_df["lyric"], train_df["ranker_genre"])

    joblib.dump(text_clf, dstpath)

    return text_clf
