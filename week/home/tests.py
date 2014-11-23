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

class DateTest(TestCase):
	def setUp(self):
		self.response = self.client.get('/')
		self.context = self.response.context

	def test_length(self):
		'Context must have one item per day of the week + 1'
		self.assertEqual(len(self.context['week_rates'].items()), 8)