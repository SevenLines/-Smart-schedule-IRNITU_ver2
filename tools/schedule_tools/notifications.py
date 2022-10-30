from datetime import timedelta, datetime

from tools.messages import reminder_messages

DEBUG = True


def get_reminders_status(time: int) -> str:
    if not time or time == 0:
        notifications_status = reminder_messages['status_disabled']
    else:
        notifications_status = reminder_messages['status_enabled'].format(time=time)
    return notifications_status


def calculating_reminder_times(schedule: list, time: int) -> dict:
    reminders = {}

    print(schedule)
    for day in schedule:
        reminders[day['day_of_week']] = []
        for lesson in day['lessons']:
            lesson_time = lesson['lesson_start'].split(':')
            hours = int(lesson_time[0])
            minutes = int(lesson_time[-1])

            reminders[day['day_of_week']].append(
                str((timedelta(hours=hours, minutes=minutes) - timedelta(minutes=time)))[:-3]
            )

    return reminders


def check_that_the_lesson_has_the_right_time(time, lesson_time) -> bool:
    if DEBUG:
        return True
    return time in lesson_time


def check_that_user_has_reminder_enabled_for_the_current_time(time_now, user_day_reminder_time: list) -> bool:
    if DEBUG:
        return True
    hours_now = int(time_now.strftime('%H'))
    minutes_now = time_now.strftime('%M')

    return user_day_reminder_time and f'{hours_now}:{minutes_now}' in user_day_reminder_time


def forming_user_to_submit(
        chat_id: int,
        group: str,
        notifications: int,
        day_now: str,
        time_now: datetime,
        week: str
) -> dict:
    lesson_time = (time_now + timedelta(minutes=notifications)).strftime('%H:%M')

    user = {
        'chat_id': chat_id,
        'group': group,
        'week': week,
        'day': day_now,
        'notifications': notifications,
        'time': lesson_time
    }

    return user
