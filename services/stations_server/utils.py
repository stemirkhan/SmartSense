import urllib.parse
import re


def parse_request_client(url: str) -> dict:
    arguments = urllib.parse.urlparse(url).fragment

    return dict(urllib.parse.parse_qsl(arguments))


def validator_url_arguments(arguments_url: dict) -> bool:
    reference_keys_url = ('access_token', 'temperature', 'pressure', 'carbonMonoxide', 'humidity')

    if not checking_names_numbers(arguments_url, reference_keys_url):
        return False
    if not checking_correctness_indications(arguments_url, reference_keys_url[1:]):
        return False

    return True


def checking_names_numbers(arguments: dict, reference_keys: tuple) -> bool:
    if len(arguments) != len(reference_keys):
        return False

    for key in reference_keys:
        if key not in arguments.keys():
            return False

    return True


def checking_correctness_indications(sensor_readings: dict, keys_sensor: tuple) -> bool:
    for key in keys_sensor:
        if not re.search(r'[+-]?\d+(\.\d+)?', sensor_readings[key]):
            return False

    return True
