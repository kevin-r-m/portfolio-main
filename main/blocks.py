from wagtail import blocks

## Resusable blocks

class TextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'blocks/text_block.html'