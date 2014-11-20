from django.test import TestCase

class HomeTest(TestCase):
	def setUp(self):
		self.response = self.client.get('/')

	def test_get(self):
		'GET must return status code 200'
		self.assertEqual(self.response.status_code, 200)

	def test_template(self):
		'Response must render template'
		self.assertTemplateUsed(self.response, 'home/index.html')

	def test_context(self):
		'Rates must be in context'
		self.assertEqual(self.response.context['2014-11-14'], 2.6059)