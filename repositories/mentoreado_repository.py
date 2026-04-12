import sqlite3

from configs.database import get_db_connection


class MentoreadoRepository:
    def __init__(self):
        self._conn = get_db_connection()
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

    def get_mentoreado_by_email(self, email):
        self._cursor.execute("""
            SELECT id, nome, email
            FROM mentoreados
            WHERE email = ?
        """, (email,))

        result = self._cursor.fetchone()
        return dict(result) if result else None

    def get_meetings_by_mentee_name(self, name):
        self._cursor.execute("""
            SELECT
                m.id,
                m.nome,
                m.email,
                e.data,
                e.confirmou_presenca
            FROM encontros e
            JOIN mentoreados m
                ON e.mentoreado_id = m.id
            WHERE m.nome LIKE ?
            ORDER BY m.nome, e.data
        """, (f"%{name}%",))

        results = self._cursor.fetchall()
        return [dict(row) for row in results]

    def count_enrollments_by_date(self, date):
        self._cursor.execute("""
            SELECT COUNT(*)
            FROM encontros
            WHERE data = ?
        """, (date,))

        return self._cursor.fetchone()["COUNT(*)"]

    def create_enrollment(self, mentoreado_id, date, confirmou_presenca=0):
        self._cursor.execute("""
            INSERT INTO encontros (mentoreado_id, data, confirmou_presenca)
            VALUES (?, ?, ?)
        """, (mentoreado_id, date, confirmou_presenca))

        self._conn.commit()

    def update_confirmation(self, mentoreado_id, date, confirmou_presenca):
        self._cursor.execute("""
            UPDATE encontros
            SET confirmou_presenca = ?
            WHERE mentoreado_id = ? AND data = ?
        """, (confirmou_presenca, mentoreado_id, date))

        self._conn.commit()

    def new_mentoreado(self, name, email):
        self._cursor.execute("""
            INSERT INTO mentoreados (nome, email)
            VALUES (?, ?)
        """, (name, email))

        self._conn.commit()
        return self._cursor.lastrowid

    def close(self):
        self._conn.close()
