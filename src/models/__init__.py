from .agency import Agency
from .client import Client
from .vehicle import Vehicle
from .campaign import Campaign

__all__ = ["Agency", "Client", "Vehicle", "Campaign"]

mapped_classes = {
    "Agency": Agency,
    "Client": Client,
    "Vehicle": Vehicle,
    "Campaign": Campaign
}