from BIyond.utils_functions import send_heartbeat, monitor_timout_events
from BIyond import app, routes
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(func=send_heartbeat, trigger="interval", seconds=3)
scheduler.add_job(func=monitor_timout_events, trigger="interval", seconds=5)
scheduler.start()

if __name__ == '__main__':
    app.run(use_reloader=False)










