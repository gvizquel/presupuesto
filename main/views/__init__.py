""" Farm Views __init__.py
"""

# Local Folders Libraries
from .main import (
    MainCreateView, MainDeleteView, MainDetailView,
    MainListView, MainUpdateView)
from .dpt import (
    EstadoAutoComplete, MunicipioAutoComplete, ParroquiaAutoComplete)
