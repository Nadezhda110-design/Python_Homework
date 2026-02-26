from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = "postgresql://postgres:5224@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_update_subject():

    sql = text("INSERT INTO subject(\"subject_id\", \"subject_title\") "
               "VALUES (:new_id,:new_title)")
    db.execute(sql, new_id=17, new_title='Handicraft')

    sql = text("UPDATE subject SET subject_title = :updated_title WHERE "
               "subject_id = :new_id")
    db.execute(sql, updated_title='Handicraft1', new_id=17)

    sql = text("SELECT subject_title FROM subject WHERE subject_id = :new_id")
    result = db.execute(sql, new_id=17)
    updated_title = result.fetchone()[0]

    assert updated_title == 'Handicraft1', (f"Expected 'Handicraft1', "
                                            f"but got '{updated_title}'")

    db.execute(text("DELETE FROM subject WHERE subject_id = :new_id"),
               {"new_id": 17})
