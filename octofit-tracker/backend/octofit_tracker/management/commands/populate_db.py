from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, Activity, Leaderboard, Workout, CustomUser

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        CustomUser.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            CustomUser.objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel),
            CustomUser.objects.create_user(email='captain@marvel.com', username='captain', team=marvel),
            CustomUser.objects.create_user(email='batman@dc.com', username='batman', team=dc),
            CustomUser.objects.create_user(email='superman@dc.com', username='superman', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30),
            Activity.objects.create(user=users[1], type='cycle', duration=45),
            Activity.objects.create(user=users[2], type='swim', duration=60),
            Activity.objects.create(user=users[3], type='run', duration=50),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='Cardio for superheroes'),
            Workout.objects.create(name='Strength Training', description='Strength for superheroes'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
