

def get_duration_df(path, category_list):
    import textgrid
    import pandas as pd
    # read the textgrid object
    grid = textgrid.TextGrid.fromFile(path)
    # initialise duration df
    category_list.append('Duration')
    data = {c:[] for c in category_list}
    # go through all the intervals
    int_num = grid[0].__len__()
    for i in range(int_num):
        label = grid[0][i].mark
        # get data from intervals that contain label
        if len(label) > 0:
            # create list that contains the categorical values
            label = label.split()
            # get duration
            dur = grid[0][i].duration()
            data['Duration'].append(dur)
            # append categorical data value to df dict
            for l in range(len(label)):
                data[category_list[l]].append(label[l])
    # transform to pd df
    df = pd.DataFrame.from_dict(data)
    return df