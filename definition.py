import pandas as pd


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("data.csv")
        definitions = tuple(df.loc[df["word"] == self.term]["definition"].values)
        return definitions if definitions else "not in the dictionary".title()


word = "acid"
d = Definition(word)
print(d.get())
