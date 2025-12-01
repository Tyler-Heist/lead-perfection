from importlib.metadata import version

from .canvass import Canvass
from .client import Client
from .custom import Custom
from .customers import Customers
from .downloads import Downloads
from .file import File
from .installer import Installer
from .leads import Leads
from .menu import Menu
from .sales import Sales

__all__ = [
    'Canvass',
    'Client',
    'Custom',
    'Customers',
    'Downloads',
    'File',
    'Installer',
    'Leads',
    'Menu',
    'Sales',
]

__version__ = version('lead_perfection')