
import numpy as np
import pandas as pd
import datetime
import random


def random_date(n_days=100):
    return datetime.date(2020, 2, 6) + datetime.timedelta(random.randint(0, n_days))

def create_binomial_data(rows, label, probability):
    data = pd.DataFrame(np.random.binomial(1, probability, size=rows).round(0), columns=["converted"])
    data["label"] = label
    data.index = pd.DatetimeIndex([random_date() for _ in range(rows)])
    return data
    
def create_exponential_data(rows, label, scale):
    s = (pd.Series(np.random.exponential(scale, size=rows))
            .apply(lambda x: max(x-(3), 0))
            .round(2)
    )
    data = pd.DataFrame(s, columns=["dollars"])
    data["label"] = label
    data.index = pd.DatetimeIndex([random_date() for _ in range(rows)])
    return data

def create_normal_data(rows, label, center):
    data = pd.DataFrame(np.random.normal(loc=center, scale=5, size=rows).round(2), columns=["time_to_complete"])
    data["label"] = label
    data.index = pd.DatetimeIndex([random_date() for _ in range(rows)])
    return data

def create_dataframe(groups, generation_method, n_rows=5000, seed=None):
    np.random.seed(seed)
    random.seed(seed)
    df = []
    for group in groups:
        rows = int(n_rows*group["percent_of_pop"])
        underlying_value = group["underlying_value"]
        label = group["label"]
        df.append(generation_method(rows, label, underlying_value))
    return pd.concat(df).sort_index()

binomial_groups1 = [
    {"label": "test",
    "underlying_value": 0.6,
    "percent_of_pop": 0.2},
    {"label": "control",
    "underlying_value": 0.5,
    "percent_of_pop": 0.8},
]

binomial_groups2 = [
    {"label": "control",
    "underlying_value": 0.08,
    "percent_of_pop": 0.8},
    {"label": "test",
    "underlying_value": 0.09,
    "percent_of_pop": 0.2},
]

exponential_groups = [
    {"label": "test",
    "underlying_value": 10,
    "percent_of_pop": 0.1},
    {"label": "control",
    "underlying_value": 12,
    "percent_of_pop": 0.9}
]

normal_groups = [
      {"label": "test",
    "underlying_value": 50,
    "percent_of_pop": 0.5},
    {"label": "control",
    "underlying_value": 50,
    "percent_of_pop": 0.5}  
]

SEED = 0

binomial_df1 = create_dataframe(binomial_groups1, create_binomial_data, seed=SEED)
binomial_df2 = create_dataframe(binomial_groups2, create_binomial_data, n_rows=6000, seed=SEED)
exponential_df = create_dataframe(exponential_groups, create_exponential_data, seed=SEED)
normal_df = create_dataframe(normal_groups, create_normal_data, seed=SEED)