"""Test app core view."""
from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    """This is a test case for view home."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use home.html."""
        self.assertTemplateUsed(self.resp, 'core/home.html')
