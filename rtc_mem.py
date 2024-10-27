from machine import RTC
import json


def store(d: dict) -> None:
    rtc = RTC()
    rtc.memory(json.dumps(d))


def recall() -> dict:
    rtc = RTC()
    raw_data = rtc.memory()

    try:
        result = json.loads(raw_data)
    except:
        result = {}

    return result
