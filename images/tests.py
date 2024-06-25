from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Image
import os

class ImageApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_image_path = os.path.join(os.path.dirname(__file__), 'test_files', 'test.jpg')

    def test_upload_image(self):
        with open(self.test_image_path, 'rb') as img:
            data = {
                'file': img,
                'filename': 'test.jpg',
                'metadata': 'Test metadata',
            }
            response = self.client.post(reverse('image-list'), data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_images(self):
        response = self.client.get(reverse('image-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_image(self):
        with open(self.test_image_path, 'rb') as img:
            data = {
                'file': img,
                'filename': 'test.jpg',
                'metadata': 'Test metadata',
            }
            response = self.client.post(reverse('image-list'), data, format='multipart')
            image_id = response.data['id']

        response = self.client.get(reverse('image-detail', args=[image_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_image(self):
        with open(self.test_image_path, 'rb') as img:
            data = {
                'file': img,
                'filename': 'test.jpg',
                'metadata': 'Test metadata',
            }
            response = self.client.post(reverse('image-list'), data, format='multipart')
            image_id = response.data['id']

        response = self.client.delete(reverse('image-detail', args=[image_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        image_exists = Image.objects.filter(id=image_id).exists()
        self.assertFalse(image_exists)
    
