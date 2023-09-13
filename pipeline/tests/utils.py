"""
Utility functions and constants for openMINDS tests
"""

import random
import string
from datetime import date, datetime
from openminds.base import Node, IRI

MAX_DEPTH = 10

P_PROPERTY_PRESENT = 0.8


def property_present(p):
    # randomly leave some properties empty
    if random.random() < p:
        return True
    else:
        return False


def build_fake_node(cls, depth=0):
    data = {}
    for property in cls.properties:
        if property.types:
            if property.types == (str,):
                # todo: check for property.formatting
                value = "".join(random.choices(string.printable, k=random.randint(0, 40)))
                data[property.name] = value
            elif float in property.types:
                value = 100 * random.random()
                data[property.name] = value
            elif int in property.types:
                value = random.randint(0, 100)
                data[property.name] = value
            elif issubclass(property.types[0], Node):
                if depth < MAX_DEPTH and property_present(P_PROPERTY_PRESENT):
                    child_cls = random.choice(property.types)
                    if child_cls != cls:  # reduce risk of recursion
                        value = build_fake_node(child_cls, depth=depth + 1)
                        data[property.name] = value
            elif property.types == (IRI,):
                value = "https://example.com/" + "".join(random.choices(string.ascii_letters, k=random.randint(0, 40)))
            elif datetime in property.types:
                value = datetime.now()
            elif date in property.types:
                value = date.today()
            else:
                raise TypeError(f"unexpected type(s): {property.types}")
    return cls(**data)
