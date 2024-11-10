import sqlite3

class Connect_DB:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def get_assignment_id(self, assignment_topic, subject_name, batch_number):
        batch_number = str(batch_number)
        query = '''SELECT "id"
                   FROM "assignments" 
                   WHERE "subject_id" = (
                   SELECT "id"  FROM "subjects" WHERE "subject_name" = ? AND "batch_number" = ?
                   ) AND "assignment_topic" = ?'''
        self.cursor.execute(query, (subject_name, batch_number, assignment_topic))
        assignment_id = self.cursor.fetchone()
        return assignment_id[0] if assignment_id else None
    
    def get_subject_id(self, subject_name, batch_number):
        batch_number = str(batch_number)
        query = '''SELECT "id"  FROM "subjects" WHERE "subject_name" = ? AND "batch_number" = ?'''
        self.cursor.execute(query, (subject_name, batch_number))
        subject_id = self.cursor.fetchone()
        return subject_id[0] if subject_id else None
    
    def get_intern_id(self, email=None, phone=None):
        if phone:
            phone = str(phone)
            query = '''SELECT "id" FROM "interns" WHERE "phone" = ?'''
            self.cursor.execute(query, (phone,))
        elif email:
            query = '''SELECT "id" FROM "interns" WHERE "email" = ?'''
            self.cursor.execute(query, (email,))
        else:
            return None
        intern_id = self.cursor.fetchone()
        return intern_id[0] if intern_id else None
    
    def get_intern_email(self, intern_id):
        intern_id = str(intern_id)
        query = '''SELECT "email" FROM "interns" WHERE "id" = ?'''
        self.cursor.execute(query, (intern_id,))
        email = self.cursor.fetchone()
        return email[0] if email else None
        
    def insert_into_grades(self, score, intern_phone=None, intern_email=None, intern_id=None, assignment_id=None, assignment_topic=None, subject_name=None, batch_number=None):
        batch_number = str(batch_number)

        if assignment_id is None:
            if not all([assignment_topic, subject_name, batch_number]):
                return "Input an assignment_id or three identifiers: assignment_topic, subject_name, batch_number"
            assignment_id = self.get_assignment_id(assignment_topic, subject_name, batch_number)

        if intern_phone == intern_email == intern_id == None:
            return "Input Intern Identifier"
        if intern_id is None:
            intern_id = self.get_intern_id(intern_email, intern_phone)     

        query = '''INSERT INTO grades (intern_id, assignment_id, score) 
                   VALUES (?, ?, ?)'''
        self.cursor.execute(query, (str(intern_id), str(assignment_id), str(score)))
        self.connection.commit()
    
    def insert_into_assignments(self, subject_id, assignment_topic, total_score):
        query = '''INSERT INTO assignments (subject_id, assignment_topic, total_score)
                   VALUES (?, ?, ?)'''
        self.cursor.execute(query, (str(subject_id), assignment_topic, str(total_score)))
        self.connection.commit()
    
    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    db = Connect_DB('database/data.db')
    print(db.get_intern_email(1))