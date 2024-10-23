from machine import RTC
import json

def store(d: dict) -> None:
    rtc = RTC()
    rtc.memory(json.dumps(d))

def recall() -> dict:
    rtc = RTC()
    raw_data = rtc.memory()
    if raw_data == b'':
        return {}
    return json.loads(raw_data)