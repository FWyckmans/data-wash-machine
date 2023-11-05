from src._init._init import *


class cleaning_machine:
    def __init__(self) -> None:
        self.with_df = False
        self.df = None
        self.diagnosis = (
            "No diagnostic has been run yet. Please use .run_diagnosis() method first"
        )

        self.options = {}

        for i in self.options.keys():
            if locals()[i] != None:
                self.options[i] = locals()[i]

    def __str__(self) -> pl.DataFrame:
        return self.options

    def __repr__(self) -> pl.DataFrame:
        return repr(self.options)

    def add_df(self, df) -> None:
        """Add dataframe to the washing machine.

        Args:
            df (pl.DataFrame|pd.DataFrame): The dataframe, either polars or pandas.

        """
        if type(df) == pd.DataFrame:
            df = pl.DataFrame(df)
            self.type = "pandas"
        elif type(df) == pl.DataFrame:
            self.type = "polars"
        assert (
            type(df) == pl.DataFrame
        ), "Only polars or pandas df are supported at the moment."
        self.df = df
        self.with_df = True
        return self

    def update_options(self, heat=None):
        for i in self.options.keys():
            if locals()[i] != None:
                self.options[i] = locals()[i]

        return self
