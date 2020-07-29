"""
For more information, see: https://dash.plotly.com/testing
"""
from dash.testing.application_runners import import_app
from selenium.common.exceptions import TimeoutException


def test_callbacks(dash_duo):
    expected = {
        'columns': "['Day of Week']",
        'rows': "['Party Size']",
        'row_order': 'key_a_to_z',
        'col_order': 'key_a_to_z',
        'aggregator': 'Average',
        'renderer': 'Grouped Column Chart',
    }

    app = import_app('usage')
    dash_duo.start_server(app)

    for prop in expected:
        try:
            dash_duo.wait_for_text_to_equal(
                f'#{prop}', expected[prop], timeout=4
            )
        except TimeoutException:
            raise Exception(f"Attribute '{prop}' failed to render correctly.")
