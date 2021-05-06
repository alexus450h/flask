def ran(*fg):
    for x in fg:
        for k in x.items():
            print(type(k))
df={'f':2}
ran(df)