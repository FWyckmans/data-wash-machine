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

    def update_options(self, heat=None):
        for i in self.options.keys():
            if locals()[i] != None:
                self.options[i] = locals()[i]

        return self
