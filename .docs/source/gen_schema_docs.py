"""
Very hacky way to write out the schema (for demo purposes only)
"""
import sys
import os

sys.path.insert(1, os.path.dirname(__file__))
import schema_doc_helpers as sh
import mmschema


def gen_rst(model_name, mode="w", filename=None, version=1, alias=None, hyperlinks={}):

    model = mmschema.get_schema(model_name, version)
    alias = alias or model_name.title()

    mfile = [f"{alias} schema"]
    mfile.append("=" * len(mfile[-1]))

    mfile.extend(f"""A full description of the overall {alias} model.""".splitlines())

    props = model.get("properties")
    req = model.get("required")

    sh.write_subsection(mfile, "Required Keys")

    if req is not None:
        mfile.extend(
            f"""The following properties are required for the {alias} specification.""".splitlines()
        )
        sh.write_key_table(mfile, props, req)
    else:
        mfile.extend(
            f"""There are no required fields for the {alias} specification.""".splitlines()
        )

    ### Optional properties
    sh.write_subsection(mfile, "Optional Keys")

    if req is not None:
        opt = set(props.keys()) - set(req)
    else:
        opt = set(props.keys())

    if len(opt):
        mfile.extend(
            f"""The following keys are optional for the {alias} specification.""".splitlines()
        )
        sh.write_key_table(mfile, props, opt)
    else:
        mfile.extend(
            f"""There are no optional fields for the {alias} specification.""".splitlines()
        )

    mfile.extend("\n\n")

    if hyperlinks:
        sh.write_subsection(mfile, "Potential Schemas")

    for key, link in hyperlinks.items():
        #mfile.extend(f"- :doc:`{key} <{link}>` \n".splitlines())
        mfile.extend([".. toctree::", f"   :caption: {key}", "   :maxdepth: 1\n", f"   {link}\n"])

    mfile.extend("\n")

    #for link in hyperlinks.values():


    # Write out the file
    filename = filename or f"auto_{model_name.lower()}.rst"
    with open(filename, mode) as outfile:
        outfile.write("\n".join(mfile))
