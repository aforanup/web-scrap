from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse


class BlogAPITest(APITestCase):
    def test_success(self):
        blog_data = {
            "title": "some_data",
            "description": "some_data",
            "image_url": "some_data",
            "author": "some_data",
            "designation": "some_data",
            "read_time": "some_data",
        }
        response_post = self.client.post(reverse("blog"), blog_data, format="json")
        self.assertEqual(response_post.status_code, 201)

        response = self.client.get(reverse("blog"), blog_data, format="json")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("blog_detail", args=["1"]), format="json")
        self.assertEqual(response.status_code, 200)

        update_data = response.data["data"]
        update_data["author"] = "some_other_data"
        response = self.client.put(
            reverse("blog_detail", args=["1"]), update_data, format="json"
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(reverse("blog_detail", args=["1"]), format="json")
        self.assertEqual(response.status_code, 200)
