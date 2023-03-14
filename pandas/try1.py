import pandas as pd
class Learn:
    data = {
        "stundas" : ["matematika", "latv val", "anglu val", "kimjia"],
        "atzimes" : ["9", "8", "10", "8"],
        "patik" : [True, False, False, False],
    }
    index = [1,2,3]    
    
    def one():
        frame = pd.DataFrame(__class__.data)
        series = pd.Series([1,2,8,32], index=["boy1", "boy2", "boy3", "boy4"])

        print(series)
        print("-->>", series["boy3"], sep="")
    
    def two():
        calories = {"day1" : 420, "day2" : 380, "day3" : 470}
        series = pd.Series(calories, index=["day1", "day2"])
        print(series)
        print(series.shape)
        # taisot series ar dict, keys become labels

    def three():
        data = {
            "calories" : [420,380,470],
            "duration" : [50,40,45]
        }

        df = pd.DataFrame(data, index = __class__.index)
        print(df)

        # loc to locate row(s)
        print("\n", df.loc[3], sep="") # returns a series
        # vins meklee peec assignotajiem indexiem

        print("\n", df.loc[[3]], sep="") # izmantojot [] vins returno dataframe

    def four():
        df = pd.read_csv("pandas/try1.csv")
        print(df.to_string()) # to_string prints the entire frame
        print(pd.options.display.max_rows) # can check max rows after which the frame gets compressed

        pd.options.display.max_rows = 1
        print(df)

    def five():
        df = pd.read_json("pandas/try1.json")
        print(df["Maxpulse"].head(15))


Learn.five()