import pandas as pd


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("data.csv")
        definitions = df.loc[df["word"] == self.term]["definition"]
        return definitions


df = pd.read_csv("data.csv")
print(df.head())
word = "acid"
print(df.loc[df["word"] == word]["definition"])