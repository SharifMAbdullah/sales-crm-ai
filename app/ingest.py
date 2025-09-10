import pandas as pd


def load_leads(path):
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def save_leads(leads, path):
    df = pd.DataFrame(leads)
    df.to_csv(path, index=False)
