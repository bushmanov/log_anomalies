import pandas as pd
import matplotlib.pyplot as plt

def plot_logs(df, *, start=None, end=None, log_count=False, overlay="dot_shadow", dupe=True):
    """
    Params:
        overlay: string - one in ["shadow", "dot", "dot_shadow"]
    """
    if not (
            isinstance(df, pd.DataFrame)
            and ("sum_count" in df.columns)
            and ("anomaly" in df.columns)
            and ("dupe" in df.columns)
            and (df.index.name == 'timestamp_minutes5')
        ):
        raise ValueError(
            'Check if supplied dataframe contains "sum_count","anomaly", and "dupe" columns and index named "timestamp_minutes5'
        )
    if start is not None and end is not None:
        if not end > start:
            raise ValueError('"end" param must be greater than "start"')
        df = df[start:end]
    if start is not None and end is None:
        df = df[start:]
    if start is None and end is not None:
        df = df[:end]
    _, ax = plt.subplots(2, 1, figsize=(15, 5), gridspec_kw={"height_ratios": [3, 1]})
    if len(df) > 100:
        st = None
    else:
        st = "o-"
    df["sum_count"].plot(label="sum_count", ax=ax[0], style=st, logy=log_count)
    ax[0].set_ylabel("sum_count")
    ax[1].set_ylabel("anomaly")
    ax[1].set_yticks([0, 1])
    df["anomaly"].plot(drawstyle="steps-post", ax=ax[1], style="r--", alpha=0.5)
    if dupe:   
        dupes = df[df['dupe']==True].reset_index().copy()
        dupes.plot(
            x="timestamp_minutes5",
            y="sum_count",
            kind="scatter",
            s=250,
            marker=u"$\u25EF$",
            edgecolors='y',
            ax=ax[0],
            label="dupe"
        )
        
    if overlay == "shadow":
        ax[0].fill_between(
            df.index,
            df["sum_count"],
            where=df["anomaly"].astype(bool)
            | df["anomaly"].shift().fillna(0).astype(bool),
            color="red",
            interpolate=False,
            alpha=0.3,
            label="anomaly timespan"
        )
        ax[0].set_xlabel(None)
        ax[0].legend()
        ax[1].legend()
        plt.tight_layout()
        return ax
    
    dots = df[df["anomaly"] == 1]["sum_count"].reset_index().copy()
    if overlay == "dot":
        dots.plot(
            x="timestamp_minutes5",
            y="sum_count",
            kind="scatter",
            color="red",
            s=100,
            ax=ax[0],
            label="anomaly timestamp"
        )
        ax[0].set_xlabel(None)
        ax[0].legend()
        ax[1].legend()
        plt.tight_layout()
        return ax
        
    if overlay == "dot_shadow":
        ax[0].fill_between(
            df.index,
            df["sum_count"],
            where=df["anomaly"].astype(bool)
            | df["anomaly"].shift().fillna(0).astype(bool),
            color="red",
            interpolate=False,
            alpha=0.3,
            label="anomaly timespan"
        )
        dots.plot(
            x="timestamp_minutes5",
            y="sum_count",
            kind="scatter",
            color="red",
            s=100,
            ax=ax[0],
            label="anomaly timestamp"
        ) 
        ax[0].set_xlabel(None)
        ax[0].legend()
        ax[1].legend()
        plt.tight_layout()
        return ax  
