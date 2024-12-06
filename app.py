import dash_mantine_components as dmc
from dash import Dash, dcc, html

from callbacks.config_loader import *
from callbacks.controls_calibration import *
from callbacks.controls_reduction import *
from callbacks.progress import *
from callbacks.reduction import *
from callbacks.scan import *
from components.config_loader import layout as config_layout
from components.controls_calibration import layout as controls_calibration_layout
from components.controls_fitting import layout as controls_fitting_layout
from components.controls_reduction import layout as controls_reduction_layout
from components.fitting import layout as fitting_layout
from components.progress import layout as progress_layout
from components.reduction import layout as reduction_layout
from components.scan import layout as scan_layout

# Initialize the Dash app
app = Dash(__name__)
app.title = "Workflow Configuration"
application = app.server


app.layout = dmc.MantineProvider(
    theme={"colorScheme": "light"},
    children=[
        dmc.Center(progress_layout()),
        dcc.Store(id="prefect-flow-run", data={"id": None, "result_uri": None}),
        dcc.Interval(id="prefect-flow-check", interval=1000),
        dmc.Grid(
            # grow=True,
            children=[
                dmc.Col(
                    html.Div(
                        children=[
                            scan_layout(),
                            controls_calibration_layout(),
                            controls_reduction_layout(),
                            controls_fitting_layout(),
                            config_layout(),
                        ]
                    ),
                    span=6,
                ),
                dmc.Col(
                    html.Div(children=[reduction_layout(), fitting_layout()]), span=6
                ),
            ],
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="8095")
