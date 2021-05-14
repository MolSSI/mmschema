"""
Very hacky way to write out the schema (for demo purposes only)
"""
# Import headers from this
import sys
import os

sys.path.insert(1, os.path.dirname(__file__))
import schema_doc_helpers as sh
import mmschema.dev

def gen_rst(model_name):

    model = getattr(mmschema.dev, model_name)

    mfile = [f"{model_name} Schema"]
    mfile.append("=" * len(mfile[-1]))

    mfile.extend(
        f"""A full description of the overall {model_name} model.""".splitlines()
    )

    props = model["properties"]
    req = model["required"]

    sh.write_header(mfile, "Required Keys")

    mfile.extend(
        f"""The following properties are required for the {model_name} specification.""".splitlines()
    )

    sh.write_key_table(mfile, props, req)

    ### Optional properties
    sh.write_header(mfile, "Optional Keys")

    mfile.extend(
        f"""The following keys are optional for the {model_name} specification.""".splitlines()
    )

    sh.write_key_table(mfile, props, set(props.keys()) - set(req))

    # Write out the file
    with open(f"auto_{model_name.lower()}.rst", "w") as outfile:
        outfile.write("\n".join(mfile))
