# A collection of python functions for praat object manipulation and processing 

## Table of contents
[Get duration data from textGrid file](https://github.com/Clara-liu/python_praat#get-duration-data-from-textGrid-file)


## Get duration data from textGrid file

The get_duration file contains a python function using the library textgrid and pandas. The textGrid file should contained intervals labelled with categorical values seperated by space. For example, if two categorical variables are needed: vowel (a ae e i o u) and length (L S), one of your label could be "ae L".  
Example:  

```Python
# The order of the variable needs to be the same as your label
category_list = ['Vowel', 'Length']

df = get_duration_df('filePath', category_list)
```