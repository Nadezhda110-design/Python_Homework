from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = "postgresql://postgres:5224@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_delete_subject():
    initial_count = db.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    sql = text("INSERT INTO subject(\"subject_id\", \"subject_title\") VALUES "
               "(:new_id,:new_title)")
    db.execute(sql, new_id=17, new_title='Handicraft')

    db.execute(text("DELETE FROM subject WHERE subject_title = :new_title"),
               {"new_title": 'Handicraft'})

    final_count = db.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    assert initial_count == final_count
