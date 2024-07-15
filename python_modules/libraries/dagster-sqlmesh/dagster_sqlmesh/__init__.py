from .version import __version__ as __version__

# isort: split

# ########################
# ##### DYNAMIC IMPORTS
# ########################
from dagster._core.libraries import DagsterLibraryRegistry

DagsterLibraryRegistry.register("dagster-sqlmesh", __version__)
