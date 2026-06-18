import math


def displacements(supports: list[tuple], elevation, factor) -> list[dict]:
    nodes = []

    for node in supports:
        if not node:
            continue
        name = node[0]
        drift = math.ceil((float(node[1]) - elevation) / factor)
        drift = max(0, drift)
        nodes.append({"node": name, "drift": drift})

    return nodes
