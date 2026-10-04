def drop_missing(df, cols):
    """Drop rows that have a missing value in any of the given columns."""
    return df.dropna(subset=cols).reset_index(drop=True)
