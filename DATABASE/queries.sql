-- Insert into batches
INSERT INTO "batches" ("batch_number", "start_date", "end_date")
VALUES (1, '2023-01-01', '2023-06-01');

-- Insert into interns
INSERT INTO "interns" ("id", "type", "first_name", "last_name", "email", "phone", "date_of_birth", "gender", "batch_number")
VALUES (1, 'Full Time', 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '1995-05-15', 'Male', 1);

-- Insert into mentors
INSERT INTO "mentors" ("id", "first_name", "last_name", "email", "phone")
VALUES (1, 'Mr.Sarbjot', 'Anand', 'example@example.com', '098-765-4321');

-- Insert into subjects
INSERT INTO "subjects" ("subject_name", "mentor_id", "batch_number")
VALUES ('Python', 1, 13);

-- Insert into assignments
INSERT INTO "assignments" ("subject_id", "assignment_topic", "total_score")
VALUES (1, 'Python', 100, 1);

-- Insert into grades
INSERT INTO "grades" ("intern_id", "assignment_id","score")
VALUES (1, 1, 100);

-- Create indexes on foreign key columns
CREATE INDEX idx_interns_batch_number ON "interns" ("batch_number");
CREATE INDEX idx_grades_intern_id ON "grades" ("intern_id");
CREATE INDEX idx_grades_assignment_id ON "grades" ("assignment_id");
CREATE INDEX idx_assignments_subject_id ON "assignments" ("subject_id");
CREATE INDEX idx_subjects_instructor_id ON "subjects" ("mentor_id");

-- Create indexes on columns used in where clauses
CREATE INDEX idx_student_performance_subject_name ON "subjects" ("subject_name");


-- Find students of a given batch
SELECT "id", "first_name", "last_name", "email" FROM "interns" WHERE "batch_number" = ? ORDER BY "first_name", "last_name";

-- Find Assignment_id
SELECT "assignment_id" 
FROM "assignments" 
WHERE "subject_id" = (
    SELECT "id"  FROM "subjects" WHERE "subject_name" = ? AND "batch_number" = ?
) AND "assignment_topic" = ?;