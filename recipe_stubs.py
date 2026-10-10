import sys
import tomllib

with open("pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)

version = pyproject["project"]["version"]
name = pyproject["project"]["name"]
description = pyproject["project"]["description"]
license_expr = pyproject["project"]["license"]
requires_python = pyproject["project"]["requires-python"]

recipe_content = f"""context:
  version: "{version}"

package:
  name: {name}
  version: "${{{{ version }}}}"

source:
  path: .

build:
  number: 0
  noarch: python
  script: "${{{{ PYTHON }}}} -m pip install . -vv --no-deps --no-build-isolation"

requirements:
  host:
    - python {requires_python}
    - hatchling
    - pip
  run:
    - python {requires_python}

about:
  homepage: https://www.freecad.org/
  license: {license_expr}
  summary: {description}
  description: |
    Type stubs for the FreeCAD Python API, providing PEP 561 py.typed stubs 
    generated from FreeCAD's C++ Python bindings.
"""

with open("recipe.yaml", "w", encoding="utf-8") as f:
    f.write(recipe_content)

print(f"Successfully generated recipe.yaml for {name} v{version}")
