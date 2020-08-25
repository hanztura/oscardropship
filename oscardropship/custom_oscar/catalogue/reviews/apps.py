import oscar.apps.catalogue.reviews.apps as apps

get_class = apps.get_class


class CatalogueReviewsConfig(apps.CatalogueReviewsConfig):
    name = 'oscardropship.custom_oscar.catalogue.reviews'

    def ready(self):
        self.detail_view = get_class('reviews.views', 'ProductReviewDetail')
        self.create_view = get_class('reviews.views', 'CreateProductReview')
        self.vote_view = get_class('reviews.views', 'AddVoteView')
        self.list_view = get_class('reviews.views', 'ProductReviewList')
