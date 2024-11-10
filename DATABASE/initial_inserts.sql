-- Insert into batches
INSERT INTO "batches" ("batch_number", "start_date", "end_date") VALUES
(13, '2023-09-01', '2024-09-01'),
(14, '2024-01-01', '2024-12-31');

-- Insert into interns
INSERT INTO "interns" ("id", "type", "first_name", "last_name", "email", "phone", "date_of_birth", "gender", "batch_number") VALUES
(1, 'Full Time', 'Sumit', 'Jaidka', 'sumitjaidka786@gmail.com', '1234567890', '2000-04-15', 'Male', 13),
(2, 'Part Time', 'Sumit', 'Jaidka', 'sumitatcultivatewill@gmail.com', '0987654321', '1998-06-23', 'Male', 14);


-- Insert into mentors
INSERT INTO "mentors" ("id", "first_name", "last_name", "email", "phone") VALUES
(1, 'John', 'Smith', 'john.smith@example.com', '1231231234'),
(2, 'Alice', 'Johnson', 'alice.johnson@example.com', '3213214321');

-- Insert into subjects
INSERT INTO "subjects" ("id", "batch_number", "subject_name", "mentor_id") VALUES
(1, 13, 'Python', 1),
(2, 14, 'Data Science', 2);

-- Insert into assignments
INSERT INTO "assignments" ("id", "subject_id", "assignment_topic", "total_score") VALUES
(1, 1, 'Python Basics', 100),
(2, 2, 'Introduction to Data Science', 100);
