from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser, Team, Activity, Workout, Leaderboard

class APITests(APITestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', team=marvel)
        Activity.objects.create(user=user, type='run', duration=30)
        Workout.objects.create(name='Morning Cardio', description='Cardio for superheroes')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_list(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_list(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workout_list(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
