from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        with transaction.atomic():
            # Clear existing data
            Leaderboard.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            Team.objects.all().delete()
            User.objects.all().delete()

            # Teams
            marvel = Team.objects.create(name='Team Marvel')
            dc = Team.objects.create(name='Team DC')

            # Users
            ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
            captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel)
            batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
            superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

            # Workouts
            w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
            w2 = Workout.objects.create(name='Running', description='Cardio endurance')

            # Activities
            Activity.objects.create(user=ironman, workout=w1, duration=30, calories=200)
            Activity.objects.create(user=batman, workout=w2, duration=45, calories=400)
            Activity.objects.create(user=superman, workout=w1, duration=60, calories=500)
            Activity.objects.create(user=captain, workout=w2, duration=20, calories=150)

            # Leaderboard
            Leaderboard.objects.create(user=ironman, points=200)
            Leaderboard.objects.create(user=batman, points=400)
            Leaderboard.objects.create(user=superman, points=500)
            Leaderboard.objects.create(user=captain, points=150)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
