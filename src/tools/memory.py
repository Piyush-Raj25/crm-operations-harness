import sqlite3
from pathlib import Path


class MemoryTool:
    """
    Stores processed CRM leads in SQLite.
    """

    DB_PATH = Path("database/crm.db")

    @classmethod
    def initialize_database(cls):
        connection = sqlite3.connect(cls.DB_PATH)
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            priority TEXT,
            approved INTEGER,
            review_notes TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        connection.commit()
        connection.close()

    @classmethod
    def save_lead(cls, lead, workflow):
        connection = sqlite3.connect(cls.DB_PATH)
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO processed_leads
            (
                name,
                phone,
                priority,
                approved,
                review_notes
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                lead.name,
                lead.phone,
                workflow.priority,
                int(workflow.approved),
                workflow.review_notes,
            ),
        )

        connection.commit()
        connection.close()