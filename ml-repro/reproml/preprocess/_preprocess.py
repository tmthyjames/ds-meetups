from pathlib import Path

import numpy as np
import pandas as pd

from reproml.config import etl_conf as ec


def process_lyrics(
    srcpath: str = ec.root_path / ec.raw_data_path / ec.lyrics.path,
    dstpath: str = ec.root_path / ec.processed_data_path / ec.lyrics.path,
) -> Path:

    srcpath = Path(srcpath)
    dstpath = Path(dstpath)

    lyrics_filec = [i for i in srcpath.glob("lyrics*.zip")]
    lyrics_df = pd.concat((pd.read_csv(f) for f in lyrics_filec), ignore_index=True)
    lyrics_df["ranker_genre"] = np.where(
        (lyrics_df["ranker_genre"] == "screamo")
        | (lyrics_df["ranker_genre"] == "punk rock")
        | (lyrics_df["ranker_genre"] == "heavy metal"),
        "alt rock",
        lyrics_df["ranker_genre"],
    )

    group = ["song", "year", "album", "genre", "artist", "ranker_genre"]
    lyrics_by_song = (
        lyrics_df.sort_values(group)
        .groupby(group)
        .lyric.apply(" ".join)
        .apply(lambda x: x.lower())
        .reset_index(name="lyric")
    )

    lyrics_by_song["lyric"] = lyrics_by_song["lyric"].str.replace(r"[^\w\s]", "")

    lyrics_by_song.to_parquet(dstpath, partition_cols=ec.lyrics.partition_cols)

    return dstpath


def split_lyrics(
    srcpath: str = ec.root_path / ec.processed_data_path / ec.lyrics.path,
    dstpath: str = ec.root_path / ec.modeling_data_path,
):
    pp = ec.root_path / ec.processed_data_path / ec.lyrics.path
    lyrics_files = [i for i in pp.glob("*/*")]
    lyrics_by_song = pd.concat((pd.read_parquet(f) for f in lyrics_files), ignore_index=True)

    msk = np.random.rand(len(lyrics_by_song)) < 0.8
    train = lyrics_by_song[msk]
    test = lyrics_by_song[~msk]

    train.to_parquet(dstpath / "train_set.parquet")
    test.to_parquet(dstpath / "test_set.parquet")

    return dstpath
