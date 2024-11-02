motd = """
  ______     ______   ____ _           _     ____
 |  _ \ \   / /  _ \ / ___| |__   __ _| |_  / ___|  ___ _ ____   _____ _ __
 | |_) \ \ / /| |_) | |   | '_ \ / _` | __| \___ \ / _ \ '__\ \ / / _ \ '__|
 |  __/ \ V / |  _ <| |___| | | | (_| | |_   ___) |  __/ |   \ V /  __/ |
 |_|     \_/  |_| \_\\\\____|_| |_|\__,_|\__| |____/ \___|_|    \_/ \___|_|
"""

databaseFile = "data/database.db"

dbInit = """
CREATE TABLE IF NOT EXISTS config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    port TEXT
);
"""