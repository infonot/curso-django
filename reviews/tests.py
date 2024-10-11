from django.test import TestCase
from django.urls import reverse

from reviews.models import Review


class ReviewListViewTest(TestCase):
    def setUp(self):
        number_of_reviews = 5
        for review_id in range(number_of_reviews):
            Review.objects.create(
                username=f'Usuario {review_id}',
                review=f'Esta es la reseña {review_id}.',
                rating=review_id
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('reviews:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reviews:index'))
        self.assertTemplateUsed(response, 'reviews/review_list.html')

    def test_context_contains_reviews(self):
        response = self.client.get(reverse('reviews:index'))
        self.assertTrue('object_list' in response.context)
        self.assertEqual(len(response.context['object_list']), 5)


class ReviewDetailViewTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            username='Juan',
            review='Mi reseña.',
            rating=4
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/reviews/consultar/{self.review.pk}')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('reviews:consultar', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reviews:consultar', kwargs={'pk': self.review.pk}))
        self.assertTemplateUsed(response, 'reviews/review_detail.html')

    def test_context_contains_review(self):
        response = self.client.get(reverse('reviews:consultar', kwargs={'pk': self.review.pk}))
        self.assertTrue('object' in response.context)
        self.assertEqual(response.context['object'], self.review)


class ReviewCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reviews/registrar')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('reviews:registrar'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reviews:registrar'))
        self.assertTemplateUsed(response, 'reviews/review_form.html')

    def test_create_review(self):
        data = {
            'username': 'Juan',
            'review': 'Mi nueva reseña.',
            'rating': 5
        }
        response = self.client.post(reverse('reviews:registrar'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)


class ReviewUpdateViewTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            username='Juan',
            review='Reseña inicial.',
            rating=3
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/reviews/modificar/{self.review.pk}')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('reviews:modificar', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reviews:modificar', kwargs={'pk': self.review.pk}))
        self.assertTemplateUsed(response, 'reviews/review_form.html')

    def test_update_review(self):
        data = {
            'username': 'Juan',
            'review': 'Nueva reseña.',
            'rating': 4
        }
        response = self.client.post(reverse('reviews:modificar', kwargs={'pk': self.review.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.review.refresh_from_db()
        self.assertEqual(self.review.review, 'Nueva reseña.')


class ReviewSuccessViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reviews/registro_exitoso')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('reviews:registro_exitoso'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reviews:registro_exitoso'))
        self.assertTemplateUsed(response, 'reviews/review_success.html')
