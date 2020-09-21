from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Staff, BodyTemp


class BodyTempTests(TestCase):

    def setUp(self):
        self.staff = Staff.objects.create(
            family_name = '試験',
            given_name = '太郎',
            family_kana = 'シケン',
            given_kana = 'タロウ',
            department= '試験部',
        )

        self.body_temp = BodyTemp.objects.create(
            name = self.staff,
            temp = 36.1,
            created_at = '2020-09-20'
        )

    def test_body_temp_content(self):
        self.assertEqual(f'{self.body_temp.name}', '試験 太郎')
        self.assertEqual(self.body_temp.temp, 36.1)
        self.assertEqual(self.body_temp.created_at, '2020-09-20')

    def test_body_today_archive_veiw(self):
        response = self.client.get(reverse('body_temp:today'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'body_temp/day.html')

    def test_body_temp_day_archive_view(self):
        response = self.client.get('/2020/9/20')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 36.1)
        self.assertTemplateUsed(response, 'body_temp/day.html')

    def test_body_temp_create_view(self):
        response = self.client.post(reverse('body_temp:new'), {
            'name': self.staff,
            'temp': 35.8,          
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 35.8)

    def test_body_temp_update_view(self):
        response = self.client.post(reverse('body_temp:edit', args='1'), {
            'temp': 37.8,          
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 37.8)

    def test_body_temp_delete_view(self):
        response = self.client.get(
            reverse('body_temp:delete', args='1'))
        self.assertEqual(response.status_code, 200)