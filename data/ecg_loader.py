import wfdb

def load_ecg():
    record = wfdb.rdrecord("100", pn_dir="mitdb")
    signal = record.p_signal[:, 0]
    fs = record.fs
    return signal, fs
