from shiny import App, render, ui
from shinywidgets import render_altair, output_widget
import altair as alt
import pandas as pd
import numpy as np


app_ui = ui.page_fluid(
    ui.panel_title("Normal Distribution of 100 Draws from Mu!"),
    ui.input_slider("mu", "N", 0, 200, 20),
    output_widget("my_hist")
)


def server(input, output, session):
    @render_altair 
    def my_hist():
        sample = np.random.normal(input.mu(), 20, 100) #generates sample with sd of 20 and size 100, mean = shiny input
        df = pd.DataFrame({'sample': sample})
        return(
            alt.Chart(df).mark_bar().encode(
                alt.X('sample:Q', bin=True), #value of 
                alt.Y('count()')
            )
        )


app = App(app_ui, server)
