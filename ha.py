#!/usr/bin/env python3

import requests

ok = True
err = "err"


class HAError(Exception): ...


class HA:
    base_url: str
    outdoor_sensor_id: str | None = None
    date_time_sensor_id: str | None = None
    ha_token: str

    def __init__(self, base_url, ha_token,  outdoor_sensor_id=None, date_time_sensor_id=None):
        self.base_url = base_url
        self.outdoor_sensor_id = outdoor_sensor_id
        self.date_time_sensor_id = date_time_sensor_id
        self.ha_token = ha_token

    def _query(self, sensor_id: str):
        headers = {"Authorization": f"Bearer {self.ha_token}"}
        try:
            r = requests.get(f"{self.base_url}/{sensor_id}", headers=headers)
        except Exception as err:
            return (err, f"network: {err}")

        if r.status_code > 299:
            return (err, r.text)

        state = r.json()["state"]
        if state == "unavailable":
            return (err, "sensor not available in HA")

        return (ok, state)

    def get_date_time(self) -> tuple[str, str]:
        if self.date_time_sensor_id is None:
            raise HAError("provide sensor id")

        status, result = self._query(self.date_time_sensor_id)
        if status != ok:
            raise HAError(result)

        raw_date, raw_time = result.split(", ")
        return raw_date, raw_time

    def get_outdoor_temp(self) -> tuple[str, str]:
        if self.outdoor_sensor_id is None:
            raise HAError("provide sensor id")

        status, result = self._query(self.outdoor_sensor_id)
        if status != ok:
            raise HAError(result)

        temp = result
        return temp