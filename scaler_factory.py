from sklearn.preprocessing import MinMaxScaler


def min_max_scaler(possible_min, possible_max, feature_range):
    scaler = MinMaxScaler(feature_range)
    scaler.fit([[possible_min], [possible_max]])
    return scaler