from .base import ApiBase
import logging

logger = logging.getLogger(__name__)

class InventoryItems(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryItem')

class ServiceSaleItems(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ServiceSaleItem')

class NonInventorySaleItems(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='NonInventorySaleItem')
