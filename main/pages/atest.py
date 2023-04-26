from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin

from .base import BasePage


class AtestPage(HeadlessPreviewMixin, BasePage):
    test_text = RichTextField(blank=True, null=True, verbose_name=_("Rich text"))

    content_panels = BasePage.content_panels + [FieldPanel("test_text")]

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.AtestPageSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("Atest")
