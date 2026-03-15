import sqlite3
import datetime
import os
import uuid

DB_PATH = "visits.db"
BASE_VISITS = 30212
BACKUP_DIR = "backups"

def init_db():
    """Initializes the SQLite database with the required schema."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS visits
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      visitor_id TEXT UNIQUE,
                      ip_address TEXT,
                      timestamp DATETIME)''')
        conn.commit()

def register_visit(visitor_id, ip_address='Anónima'):
    """Registers a new visit. Ignores if visitor_id already exists (handled by UNIQUE constraint)."""
    init_db()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            # Insert or ignore means if the visitor_id already exists in the table, it won't add a duplicate
            c.execute('INSERT OR IGNORE INTO visits (visitor_id, ip_address, timestamp) VALUES (?, ?, ?)',
                      (visitor_id, ip_address, datetime.datetime.now()))
            conn.commit()
    except Exception as e:
        print(f"Error registering visit: {e}")

def get_statistics():
    """Returns a dictionary containing visit statistics."""
    init_db()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            
            # Total unique visits from DB (plus base visits)
            c.execute("SELECT COUNT(*) FROM visits")
            total_db_visits = c.fetchone()[0]
            
            now = datetime.datetime.now()
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            week_start = today_start - datetime.timedelta(days=now.weekday())
            month_start = today_start.replace(day=1)
            
            # Visits today
            c.execute("SELECT COUNT(*) FROM visits WHERE timestamp >= ?", (today_start,))
            today_visits = c.fetchone()[0]
            
            # Visits this week
            c.execute("SELECT COUNT(*) FROM visits WHERE timestamp >= ?", (week_start,))
            week_visits = c.fetchone()[0]
            
            # Visits this month
            c.execute("SELECT COUNT(*) FROM visits WHERE timestamp >= ?", (month_start,))
            month_visits = c.fetchone()[0]
            
            # Daily average calculation
            c.execute("SELECT MIN(timestamp) FROM visits")
            first_visit = c.fetchone()[0]
            avg_daily = today_visits # default safely if no prior records
            
            if first_visit:
                # Handle possible fractional seconds in datetime
                dt_str = first_visit.split('.')[0] 
                first_date = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                days_diff = (now - first_date).days
                days = max(1, days_diff)
                avg_daily = total_db_visits / days
                
            return {
                "total": BASE_VISITS + total_db_visits,
                "today": today_visits,
                "week": week_visits,
                "month": month_visits,
                "average": round(avg_daily, 2)
            }
    except Exception as e:
         print(f"Error checking stats: {e}")
         return {
                "total": BASE_VISITS,
                "today": 0,
                "week": 0,
                "month": 0,
                "average": 0
            }

def backup_database():
    """Creates a local backup of the database to prevent data loss."""
    import shutil
    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
            
        backup_file = os.path.join(BACKUP_DIR, f"visits_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
        if os.path.exists(DB_PATH):
            shutil.copy2(DB_PATH, backup_file)
            return backup_file
    except Exception as e:
        print(f"Error backing up DB: {e}")
    return None
