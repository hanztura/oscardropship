import sys

from django.conf import settings

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest


class PayPalClient:
    def __init__(self):
        super().__init__()
        self.client_id = settings.PAYPAL_API_CLIENT_ID
        self.client_secret = settings.PAYPAL_API_SECRET

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key, value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                self.object_to_json(value) if not self.is_primittive(value) else\
                value
        return result

    def array_to_json_array(self, json_array):
        result = []
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if not self.is_primittive(item)
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)


class CreateOrder(PayPalClient):

    # 2. Set up your server to receive a call from the client
    """ This is the sample function to create an order. It uses the
      JSON body returned by buildRequestBody() to create an order."""

    def create_order(self, debug=False):
        request = OrdersCreateRequest()
        request.prefer('return=representation')
        # 3. Call PayPal to set up a transaction
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Order ID: ', response.result.id
            print 'Intent: ', response.result.intent
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))
            print 'Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                               response.result.purchase_units[0].amount.value)

        return response

        """Setting up the JSON request body for creating the order. Set the intent in the
    request body to "CAPTURE" for capture intent flow."""
    @staticmethod
    def build_request_body():
        """Method to create body with CAPTURE intent"""
        return \
            {
                "intent": "CAPTURE",
                "application_context": {
                    "brand_name": "django oscar",
                    "landing_page": "BILLING",
                    "shipping_preference": "SET_PROVIDED_ADDRESS",
                    "user_action": "CONTINUE"
                },
                "purchase_units": [
                    {
                        "reference_id": "PUHF",
                        "description": "Sporting Goods",

                        "custom_id": "CUST-HighFashions",
                        "soft_descriptor": "HighFashions",
                        "amount": {
                            "currency_code": "USD",
                            "value": "230.00",
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": "180.00"
                                },
                                "shipping": {
                                    "currency_code": "USD",
                                    "value": "30.00"
                                },
                                "handling": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "tax_total": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "shipping_discount": {
                                    "currency_code": "USD",
                                    "value": "10"
                                }
                            }
                        },
                        "items": [
                            {
                                "name": "T-Shirt",
                                "description": "Green XL",
                                "sku": "sku01",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "90.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "quantity": "1",
                                "category": "PHYSICAL_GOODS"
                            },
                            {
                                "name": "Shoes",
                                "description": "Running, Size 10.5",
                                "sku": "sku02",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "45.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "5.00"
                                },
                                "quantity": "2",
                                "category": "PHYSICAL_GOODS"
                            }
                        ],
                        "shipping": {
                            "method": "United States Postal Service",
                            "address": {
                                "name": {
                                    "full_name": "John",
                                    "surname": "Doe"
                                },
                                "address_line_1": "123 Townsend St",
                                "address_line_2": "Floor 6",
                                "admin_area_2": "San Francisco",
                                "admin_area_1": "CA",
                                "postal_code": "94107",
                                "country_code": "US"
                            }
                        }
                    }
                ]
            }


"""This is the driver function that invokes the createOrder function to create
   a sample order."""
if __name__ == "__main__":
    CreateOrder().create_order(debug=True)
