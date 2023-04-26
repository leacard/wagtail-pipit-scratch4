from .base_page import BasePageFactory
from ..pages.atest import AtestPage


class AtestPageFactory(BasePageFactory):
    class Meta:
        model = AtestPage
