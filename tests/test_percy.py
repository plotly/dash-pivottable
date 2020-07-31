"""
For more information, see: https://dash.plotly.com/testing
"""
from dash.testing.application_runners import import_app


def test_percy(dash_duo):
    app = import_app('usage')
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#columns')
    dash_duo.percy_snapshot("usage.py")
