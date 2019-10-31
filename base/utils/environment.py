# -*- coding: utf-8 -*-
"""Code related to environment management"""
import os


__all__ = ['converter']


def convert_into_list(string, separator=";", to_strip=False):
    """Convert a string into a list."""
    result = string.split(separator)
    if to_strip:
        result = [ s.strip() for s in result ]
    result = [ s for s in result if s ]
    return result

def convert_into_number(string):
    """Convert a string into a number."""
    has_comma = [s in string for s in (',', ';')]
    comma_ambiguity, has_comma = all(has_comma), any(has_comma)
    potential_number = "".join(s for s in string if s not in ("+", "-", ".", ",")).isdigit()
    if potential_number:
        if comma_ambiguity:
            raise ValueError('decimal should be casted with only one symbol')
        elif has_comma:
            return float(string)
        else:
            return int(string)
    else:
        raise TypeError(f'string type should be <str>. Instead it is {type(string)}.')

def convert_into_boolean(string):
    """Convert a string into a boolean."""
    if string.strip().lower() in ['1', 'true', 't', 'y']:
        return True
    if string.strip().lower() in ['0', 'false', 'f', 'n'] or not string:
        return False
    else:
        raise TypeError(f'string {string} is not an identified boolean.')

def converter(key, output_type='str', coerce_key_error=False, list_separator=";", enable_os=True):
    """Convert an environment variable into a Python type.

        output_type: if None, the type is string
        key_error equals: if True, no raise is used when the key does not exist
            and the value is None
    """
    variable = os.getenv(key, "") if enable_os else key
    result = None
    if not variable and enable_os:
        msg = f"{key} is not enregistered as a environment variable."
        if coerce_key_error:
            print(msg, " It has been changed as the default value.")
            result = variable
        else:
            raise KeyError(msg)
    else:
        if output_type == 'str':
            result = variable
        elif output_type == 'list':
            result = convert_into_list(variable, list_separator) if variable else []
        elif output_type == 'number':
            result = convert_into_number(variable) if variable else 0
        elif output_type == 'bool':
            result = convert_into_boolean(variable) if variable else False
        else:
            print("Incorrect output_type")
    return result
