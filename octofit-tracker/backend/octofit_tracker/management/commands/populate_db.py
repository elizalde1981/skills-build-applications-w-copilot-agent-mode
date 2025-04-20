import logging
from django.core.management.base import BaseCommand
from datetime import timedelta
from bson import ObjectId
from pymongo import MongoClient

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        logger.debug('Starting database population...')
        
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        logger.debug('Dropping existing collections...')
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        logger.debug('Inserting users...')
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)
        logger.debug(f'Inserted users: {users}')

        # Insert teams
        logger.debug('Inserting teams...')
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [user["_id"] for user in users]},
        ]
        db.teams.insert_many(teams)
        logger.debug(f'Inserted teams: {teams}')

        # Insert activities
        logger.debug('Inserting activities...')
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 3600},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 7200},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 5400},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 1800},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 4500},
        ]
        db.activity.insert_many(activities)
        logger.debug(f'Inserted activities: {activities}')

        # Insert leaderboard entries
        logger.debug('Inserting leaderboard entries...')
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)
        logger.debug(f'Inserted leaderboard entries: {leaderboard}')

        # Insert workouts
        logger.debug('Inserting workouts...')
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)
        logger.debug(f'Inserted workouts: {workouts}')

        logger.debug('Database population completed successfully.')
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using pymongo.'))