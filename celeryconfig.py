from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERYBEAT_SCHEDULE = {
    'api-request-by-minute': {
        'task': 'tasks.run_all_api_tests',
        'schedule': crontab(minute='*/1')
    }
}
