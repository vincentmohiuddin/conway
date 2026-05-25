import json
import logging
import tomllib

import streamlit as st

from pydantic import ValidationError

from backend.automaton import Automaton
from backend.cell import Cell
from frontend.config import AppConfig, InitialCellsConfig
from frontend.plot import plot_step

with open("config.toml", "rb") as f:
    config = AppConfig.model_validate(tomllib.load(f))

logging.basicConfig(level=config.log_level)


st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Conway's Game of Life")
    with st.form("config"):
        rows = st.number_input("Rows", value=config.grid.rows, min_value=1)
        cols = st.number_input("Columns", value=config.grid.cols, min_value=1)
        coord_input = st.text_area(
            "Initial cells — JSON array of [x, y] pairs",
            value=json.dumps(config.initial_cells.alive_cells),
            height=500,
        )
        submitted = st.form_submit_button("Run")

step_label = st.empty()
placeholder = st.empty()

if submitted:
    try:
        cells = InitialCellsConfig.model_validate(
            {"alive_cells": json.loads(coord_input)}
        )
        initial_alive_cells = {Cell(x, y) for x, y in cells.alive_cells}
    except (json.JSONDecodeError, ValidationError) as e:
        st.error(f"Invalid input: {e}")
        st.stop()

    automaton = Automaton(rows=int(rows), cols=int(cols))
    for step, matrix in enumerate(automaton.run(initial_alive_cells)):
        step_label.text(f"Step {step}")
        placeholder.image(plot_step(matrix), width="stretch")
