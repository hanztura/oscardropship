from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    title_tag = blocks.ChoiceBlock(
        default='h1',
        choices=(
            ('h1', 'h1'),
            ('p', 'p'),
            ('h2', 'h2'),
            ('h3', 'h3'),
            ('h4', 'h4'),
            ('h5', 'h5'),
            ('h6', 'h6'),
        )
    )
    cta_text = blocks.CharBlock(
        required=False,
        help="Call to Action - Text"
    )
    cta_href = blocks.CharBlock(
        required=False,
        default='#',
        help="Call to Action - Target Link"
    )
    background_image = ImageChooserBlock(required=False)

    class Meta:
        template = 'uikit/wagtail/blocks/banner.html'
