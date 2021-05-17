"""
Very hacky way to write out the schema (for demo purposes only)
"""
import sys
import os

sys.path.insert(1, os.path.dirname(__file__))
import schema_doc_helpers as sh
import mmschema.dev

def gen_rst(model_name, mode="w", filename=None):

    model = getattr(mmschema.dev, model_name)

    mfile = [f"{model_name} Schema"]

    if mode == "w":
        mfile.append("=" * len(mfile[-1]))
    else:
        mfile.append("^" * len(mfile[-1]))

    mfile.extend(
        f"""A full description of the overall {model_name} model.""".splitlines()
    )


    props = model["properties"]
    req = model["required"]

    sh.write_subsubsection(mfile, "Required Keys")

    mfile.extend(
        f"""The following properties are required for the {model_name} specification.""".splitlines()
    )

    sh.write_key_table(mfile, props, req)

    ### Optional properties
    sh.write_subsubsection(mfile, "Optional Keys")

    mfile.extend(
        f"""The following keys are optional for the {model_name} specification.""".splitlines()
    )

    sh.write_key_table(mfile, props, set(props.keys()) - set(req))

    mfile.extend("\n\n")

    # Write out the file
    filename = filename or f"auto_{model_name.lower()}.rst"
    with open(filename, mode) as outfile:
        outfile.write("\n".join(mfile))
