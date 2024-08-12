from typing import *
import pandas as pd
from dataframe_short.utils_ds import *
def return_display_html(df:Union[pd.DataFrame], display_height=300):
    """
    this is needed as simply use display_nice_df does not work in jupyter notebook
    display_nice_df(value_counts) doesn't seem to work
    """

    from IPython.display import display, HTML
    if isinstance(df, pd.Series):
        df_in = df.to_frame()
        html = f"""
        <div style="max-height: {display_height}px; overflow-y: scroll;">
            {df_in.to_html()}
        </div>
        """
        # display(HTML(html))
    else:
        html = f"""
        <div style="max-height: {display_height}px; overflow-y: scroll;">
            {df.to_html()}
        </div>
        """
        # display(HTML(html))
    return html
def display_nice_df(df:Union[pd.DataFrame], display_height=300):

    """
    main reason I create this is to display the row with the scrolling
    display_height: is the height of diplayed cells
    """
    from IPython.display import display, HTML
    if isinstance(df, pd.Series):
        df_in = df.to_frame()
        html = f"""
        <div style="max-height: {display_height}px; overflow-y: scroll;">
            {df_in.to_html()}
        </div>
        """
        display(HTML(html))
    else:
        html = f"""
        <div style="max-height: {display_height}px; overflow-y: scroll;">
            {df.to_html()}
        </div>
        """
        display(HTML(html))

def display_value_counts(df:pd.DataFrame,dropna:bool = False, display_height=300):
    count_of_values = value_counts(df,dropna)

    # display_nice_df(count_of_values,display_height)

    from IPython.display import display, HTML
    html = return_display_html(count_of_values,display_height)
    display(HTML(html))

def display_dtype(df:pd.DataFrame, display_height=300):
    dtype_df = dtypes(df,return_as_dict=False)

    # display_nice_df(count_of_values,display_height)

    from IPython.display import display, HTML
    html = return_display_html(dtype_df,display_height)
    display(HTML(html))

def display_null(df:pd.DataFrame, display_height=300):
    null_df = count_null(df,return_as_dict=False)

    # display_nice_df(count_of_values,display_height)

    from IPython.display import display, HTML
    html = return_display_html(null_df,display_height)
    display(HTML(html))