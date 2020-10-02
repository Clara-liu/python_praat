

def get_duration_df(path, category_list):
    import textgrid
    import pandas as pd
    # read the textgrid object
    grid = textgrid.TextGrid.fromFile(path)
    # go through all the intervals
    int_num = grid[0].__len__()
    # initialise duration df
    category_list.append('Duration')
    data = {c:[] for c in category_list}
    for i in range(int_num):
        label = grid[0][i].mark
        if len(label) > 0:
            label = label.split()
            dur = grid[0][i].duration()
            data['Duration'].append(dur)
            for l in range(len(label)):
                data[category_list[l]].append(label[l])
    df = pd.DataFrame.from_dict(data)
    return df