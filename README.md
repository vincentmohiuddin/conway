# Conway's Game of Life

Conway's Game of Life running in a Streamlit app.

<video src="assets/demo.mov" controls></video>

## How it works

The simulation runs step by step. Each step, only cells that are alive or next to an alive cell are checked. The result is a 2D matrix that gets rendered as an image and streamed to the browser.

Cells that move outside the grid are removed.

## Architecture

```
backend/
  cell.py       -- Cell dataclass
  automaton.py  -- simulation logic

frontend/
  config.py     -- Pydantic models for config.toml
  plot.py       -- helper for plotting backend cell matrix
  app.py        -- Streamlit UI
```

## Run

```bash
docker compose up --build
```

Open [http://localhost:8501](http://localhost:8501), set the grid size and starting cells, then click **Run**.

## Configuration

Default grid size and starting cells are set in `config.toml`. Both can also be changed in the sidebar.

## Ideas

- **Toroidal grid** -- instead of removing cells that go out of bounds, wrap them to the other side.
- **Step history** -- store all frames so the user can scrub back and forth through the simulation.
