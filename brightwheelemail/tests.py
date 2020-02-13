from rest_framework import status

from rest_framework import test

# Create your tests here.


class EmailTestCase(test.APITestCase):

    def setUp(self):
        return None

    def tearDown(self):
        return None

    def to_email_is_missing(self):
        url = '/send_email/'
        data = {
            "to_name": "aabhas singhal",
            "from": "noreply@abc.com",
            "from_name": "test name",
            "subject": "this is a test case",
            "body": "this is the body"
        }
        response = self.client.post(url=url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def to_email_is_not_valid(self):
    #     pass
    #
    # def from_email_is_missing(self):
    #     pass
    #
    # def from_email_is_not_valid(self):
    #     pass
    #
    # def all_data_is_correct(self):
    #     pass
