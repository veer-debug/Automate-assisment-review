-- Insert into batches
INSERT INTO "batches" ("batch_number", "start_date", "end_date")
VALUES (1, '2023-01-01', '2023-06-01');

-- Insert into interns
INSERT INTO "interns" ("id", "type", "first_name", "last_name", "email", "phone", "date_of_birth", "gender", "batch_number")
VALUES (1, 'Full Time', 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '1995-05-15', 'Male', 1);

-- Insert into instructors
INSERT INTO "instructors" ("id", "first_name", "last_name", "email", "phone")
VALUES (1, 'Sumit', 'Jaidka', 'sumit.jaidka@example.com', '098-765-4321');

-- Insert into subjects
INSERT INTO "subjects" ("id", "subject_name", "instructor_id")
VALUES (1, 'Python', 1);

-- Insert into passion_project
INSERT INTO "passion_project" ("id", "name", "type", "head_instructor", "guide_instructor1", "guide_instructor2")
VALUES (1, 'AI Project', 'Research', 1, NULL, NULL);

-- Insert into assignments
INSERT INTO "assignments" ("id", "subject_id", "assignment_topic", "total_score", "instructor_id")
VALUES (1, 1, 'Python', 100, 1);

-- Insert into grades
INSERT INTO "grades" ("intern_id", "assignment_id", "teacher_id", "score", "date")
VALUES (1, 1, 1, 95, '2023-03-15');

-- Insert into batch_subject
INSERT INTO "batch_subject" ("batch_id", "subject_id")
VALUES (1, 1);

-- Insert into batch_instructor
INSERT INTO "batch_instructor" ("batch_id", "instructor_id")
VALUES (1, 1);

-- Create indexes on foreign key columns
CREATE INDEX idx_interns_batch_number ON "interns" ("batch_number");
CREATE INDEX idx_grades_intern_id ON "grades" ("intern_id");
CREATE INDEX idx_grades_assignment_id ON "grades" ("assignment_id");
CREATE INDEX idx_assignments_subject_id ON "assignments" ("subject_id");
CREATE INDEX idx_subjects_instructor_id ON "subjects" ("instructor_id");

-- Create indexes on columns used in where clauses
CREATE INDEX idx_student_performance_instructor_id ON "grades" ("teacher_id");
CREATE INDEX idx_student_performance_subject_name ON "subjects" ("subject_name");

-- Additional common lookup indexes
CREATE INDEX idx_batch_subject_batch_id ON "batch_subject" ("batch_id");
CREATE INDEX idx_batch_instructor_batch_id ON "batch_instructor" ("batch_id");

-- View for average scores per batch
CREATE VIEW "average_intern_scores" AS
SELECT 
    i."id" AS "intern_id",
    i."first_name",
    i."last_name",
    i."batch_number",
    AVG(g."score") AS "average_score"
FROM 
    "interns" i
JOIN 
    "grades" g ON i."id" = g."intern_id"
GROUP BY 
    i."id", i."first_name", i."last_name", i."batch_number";

-- query for Average Scores of students in a given Batch
SELECT 
    "intern_id", 
    "first_name", 
    "last_name", 
    "average_score"
FROM 
    "average_intern_scores"
WHERE 
    "batch_number" = 1;

-- view for student_performance
CREATE VIEW "student_performance" AS
SELECT 
    i."id" AS "student_id",
    i."first_name",
    i."last_name",
    s."subject_name",
    g."score",
    g."teacher_id",
    g."assignment_id"
FROM 
    "interns" i
JOIN 
    "grades" g ON i."id" = g."intern_id"
JOIN 
    "assignments" a ON g."assignment_id" = a."id"
JOIN 
    "subjects" s ON a."subject_id" = s."id";

-- query for finding average student_performance under a given instructor for a given subject
SELECT 
    "student_id", 
    "first_name", 
    "last_name", 
    "subject_name", 
    AVG("score") AS "average_score"
FROM 
    "student_performance"
WHERE 
    "instructor_id" = 1
    AND "subject_name" = 'Python'
GROUP BY 
    "student_id", 
    "first_name", 
    "last_name", 
    "subject_name";

