from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = "postgresql://postgres:5224@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert_new_subject():
    initial_count = db.execute(text("SELECT COUNT(*) FROM subject")).scalar()
    sql = text("INSERT INTO subject( \"subject_title\") "
               "VALUES (:new_title)")
    db.execute(sql, new_title='Handicraft')
    final_count = db.execute(text("SELECT COUNT(*) FROM subject")).scalar()
    assert final_count - initial_count == 1

    db.execute(text("DELETE FROM subject WHERE subject_title = :new_title"),
               {"new_title": "Handicraft"})
