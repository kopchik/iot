from ..ha import HA, HAError
import os

HA_BASE_URL = "http://ha/api/states"
OUTDOOR_SENSOR_ID = "sensor.atc_al1_1ac4_temperature"


import pytest
@pytest.fixture(autouse=True)
def ha_token():
    token = os.environ.get('HA_TOKEN')
    assert token is not None, "set HA_TOKEN environment variable"
    return token


def test_temperature(ha_token):
    ha = HA(base_url=HA_BASE_URL, ha_token=ha_token, outdoor_sensor_id=OUTDOOR_SENSOR_ID)
    temp = ha.get_outdoor_temp()
    breakpoint()
