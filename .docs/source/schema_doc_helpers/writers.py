"""
A small module to assist in the writing of RST
"""
import textwrap


def write_subsection(data, header):
    data.append("")
    data.append(header)
    data.append("-" * len(header))
    data.append("")


def write_subsubsection(data, header):
    data.append("")
    data.append(header)
    data.append("~" * len(header))
    data.append("")


def write_line_items(data, key, item):
    data.append("")
    data.append(key)
    data.append("~" * len(key))
    data.append("")
    if "description" in item:
        data.append(item["description"])
    else:
        data.append("No description available")
    data.append("")


def write_key_table(top_file, properties, keys=None):
    table_widths = [95, 120, 80]  # [45, 120, 27]
    fmt_string = "   | {:%s} | {:%s} | {:%s} |" % tuple(table_widths)
    dash_inds = tuple("-" * w for w in table_widths)
    equals_inds = tuple("=" * w for w in table_widths)

    top_file.append("   +-{}-+-{}-+-{}-+".format(*dash_inds))
    top_file.append(fmt_string.format("Key Name", "Description", "Field Type"))
    top_file.append("   +={}=+={}=+={}=+".format(*equals_inds))

    if keys is None:
        keys = properties.keys()
    keys = sorted(keys)  # Alphabetical sorting looks better IMO

    for key in keys:
        value = properties[key]

        if "anyOf" in value:
            value = value["anyOf"][1]

        if "type" in value:
            dtype = value["type"]
        elif "$ref" in value:
            dtype = value["$ref"]
        else:
            dtype = "object" # wild guess?
            #raise ValueError(f"type not found in {key}")

        if "description" in value:
            description = value["description"]
        elif value["type"] == "object":
            description = value["$ref"]
        else:
            description = "No description provided."

        if dtype == "array":
            if "type" in value["items"]:
                arr_type = value["items"]["type"]
            elif "$ref" in value["items"]:
                arr_type = value["items"]["$ref"]
            else:
                raise ValueError(
                    f"No dtype for items in array {key} of value {value['items']}."
                )
            dtype = "array[" + arr_type + "]"

        # Figure out the needed slices

        desc_parts = textwrap.wrap(description, width=table_widths[1])
        top_file.append(fmt_string.format(key, desc_parts[0], dtype))

        for dp in desc_parts[1:]:
            top_file.append(fmt_string.format("", dp, ""))

        top_file.append("   +-{}-+-{}-+-{}-+".format(*dash_inds))
