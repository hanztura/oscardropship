import json
import stringcase


class Thing:
    CONTEXT = 'https://schema.org/'

    def __init__(
            self, name='', description='', url=None, image=None, same_as=None):
        self.name = name
        self.description = description
        self.url = url
        self.image = image
        self.same_as = same_as

        self.attributes_to_get = self.get_thing_attributes_to_get()
        self.optional_attributes = self.get_thing_optional_attributes()

    def __str__(self):
        return self.as_python_dict

    @classmethod
    def get_item_type(cls):
        return '{}{}'.format(cls.CONTEXT, cls.__name__)

    @classmethod
    def get_thing_optional_attributes(cls):
        return ['url', 'image', 'same_as']

    @classmethod
    def get_thing_attributes_to_get(cls):
        return ['name', 'description']

    @property
    def header_python_dict(self):
        return {
            '@context': self.CONTEXT,
            '@type': self.__class__.__name__,
        }

    @property
    def as_thing_python_dict(self):
        value = self.header_python_dict
        value = self.compute_value(value, self.get_thing_attributes_to_get())
        value = self.compute_value(
            value, self.get_thing_optional_attributes(), True)

        return value

    @property
    def as_thing_json(self):
        return json.dumps(self.as_thing_python_dict)

    @property
    def as_python_dict(self):
        value = self.header_python_dict
        value = self.compute_value(value, self.attributes_to_get)
        value = self.compute_value(
            value, self.optional_attributes, True)

        return value

    @property
    def as_json(self):
        return json.dumps(self.as_python_dict)

    def compute_value(self, value, attributes, optionals=False):
        for attribute in attributes:
            if optionals:
                if hasattr(self, attribute) and getattr(self, attribute):
                    value[stringcase.camelcase(attribute)] = getattr(
                        self, attribute)
            else:
                value[stringcase.camelcase(attribute)] = getattr(
                    self, attribute)
        return value


class PostalAddress(Thing):

    def __init__(
            self, address_country, address_locality, address_region,
            postal_code, street_address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.address_country = address_country
        self.address_locality = address_locality
        self.address_region = address_region
        self.postal_code = postal_code
        self.street_address = street_address

        self.attributes_to_get += [
            'address_country', 'address_locality', 'address_region',
            'postal_code', 'street_address'
        ]


class Organization(Thing):

    def __init__(self, address, email, telephone, same_as, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.address = address.as_python_dict
        self.email = email
        self.telephone = telephone
        self.same_as = same_as

        self.attributes_to_get += ['email', 'telephone', 'same_as']


class Person(Thing):

    def __init__(self, email, affiliation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.affiliation = affiliation.as_python_dict
        self.email = email

        self.attributes_to_get += ['email', 'affiliation']


class WebContent(Thing):

    def __init__(
            self, about, author, date_published, date_modified,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.about = about.as_thing_python_dict
        self.author = author.as_python_dict
        self.date_published = date_published
        self.date_modified = date_modified

        self.attributes_to_get += [
            'about', 'author', 'date_published',
            'date_modified'
        ]


class Offer(Thing):

    def __init__(
            self, price, price_currency, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.price_currency = price_currency

        self.attributes_to_get += ['price', 'price_currency']


class Product(Thing):

    def __init__(
            self, audience, manufacturer, brand, sku, offer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.audience = audience.as_python_dict
        self.manufacturer = manufacturer.as_python_dict
        self.brand = brand.as_python_dict  # organization
        self.sku = sku
        self.offers = offer.as_python_dict

        self.attributes_to_get += [
            'audience', 'manufacturer', 'brand', 'sku', 'offers']


SCHEMAS = [Thing, PostalAddress, Organization, Person, WebContent]
ITEM_TYPES_AS_CHOICES = [(s.get_item_type(), s.__name__)for s in SCHEMAS]
