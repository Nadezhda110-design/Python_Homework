from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = "postgresql://postgres:5224@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_update_subject():

    sql = text("INSERT INTO subject( \"subject_title\") "
               "VALUES (:new_title)")
    db.execute(sql, new_title='Handicraft')

    sql = text("UPDATE subject SET subject_title = :updated_title "
               "WHERE subject_title = :new_title")
    db.execute(sql, updated_title='Handicraft1', new_title='Handicraft')

    sql = text("SELECT subject_title FROM subject WHERE subject_title = :updated_title")
    result = db.execute(sql, {"updated_title": 'Handicraft1'})
    updated_title = result.fetchone()[0]

    assert updated_title == 'Handicraft1'
    db.execute(text("DELETE FROM subject WHERE subject_title = :updated_title"),
               {"updated_title": "Handicraft1"})
