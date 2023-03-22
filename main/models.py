from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from main.blocks import TextBlock

bodyContent = [
    ('text', TextBlock()),
]

class MainPage(Page):
    content = StreamField(bodyContent, use_json_field=True, default=None, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]