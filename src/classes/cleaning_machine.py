from src._init._init import *


class cleaning_machine:
    def __init__(self, type=None) -> None:
        self.original_df = None
        self.clean_df = None
        self.diagnosis = (
            "No diagnostic has been run yet. Please use .run_diagnosis() method first"
        )

        self.options = {"type": None}
        self.state = {
            "original_df": False,
            "diagnostic_done": False,
            "cleaning_done": False,
        }

        for i in self.options.keys():
            if locals()[i] != None:
                self.options[i] = locals()[i]

    def __str__(self) -> dict:
        return self.options

    def __repr__(self) -> dict:
        return repr(self.options)

    def add_df(self, df) -> None:
        """Add dataframe to the washing machine.

        Args:
            df (pl.DataFrame|pd.DataFrame): The dataframe, either polars or pandas.

        """
        if type(df) == pd.DataFrame:
            df = pl.DataFrame(df)
            self.options["type"] = "pandas"
        elif type(df) == pl.DataFrame:
            self.options["type"] = "polars"

        assert self.options["type"] in [
            "pandas",
            "polars",
        ], "Only polars or pandas df are supported at the moment."
        self.original_df = df
        self.state["original_df"] = True

    def update_options(self, heat=None):
        for i in self.options.keys():
            if locals()[i] != None:
                self.options[i] = locals()[i]

        return self

    def run_diagnostic(self, on="original"):
        if on == "original":
            assert (
                self.state["original_df"] == True
            ), "Please first add a dataframe to the washing machine with .add_df() method."

            diagnosis = self.original_df.describe()
            self.diagnosis = diagnosis
            self.state["diagnostic_done"] = True
            return diagnosis

        elif on == "clean":
            assert (
                self.state["cleaning_done"] == True
            ), "Please clean original df first with the .clean() method."
            diagnosis_clean = self.clean_df.describe()
            self.diagnosis_clean = diagnosis
            return diagnosis_clean

    def start_program(self):
        dt = self.original_df
        dt = dt.with_columns(pl.all().forward_fill())
        self.clean_df = dt
        self.state["cleaning_done"] = True

        if self.options["type"] == "pandas":
            dt = dt.to_pandas()
        return dt


df = pl.DataFrame([[1, 2, 3], ["a", "b", None]])
df = pd.DataFrame([[1, "a"], [2, "b"], [3, None]])

cm_test = cleaning_machine()
cm_test.options
cm_test.state
cm_test.add_df(df)
cm_test.options
cm_test.state
cm_test.run_diagnostic()
cm_test.options
cm_test.state
cm_test.start_program()
