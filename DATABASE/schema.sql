CREATE TABLE "batches" (
    "batch_number" INTEGER PRIMARY KEY,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC
);

CREATE TABLE "interns" (
    "id" INTEGER PRIMARY KEY,
    "type" TEXT CHECK("type" IN ('Full Time', 'Part Time')),
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "phone" TEXT NOT NULL UNIQUE,
    "date_of_birth" NUMERIC,
    "gender" TEXT CHECK("gender" IN ('Male', 'Female', 'Other', NULL)),
    "batch_number" INTEGER NOT NULL,
    FOREIGN KEY ("batch_number") REFERENCES "batches" ("batch_number")
);

CREATE TABLE "mentors" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "phone" TEXT NOT NULL UNIQUE
);
 
CREATE TABLE "subjects" (
    "id" INTEGER PRIMARY KEY,
    "batch_number" INTEGER NOT NULL,
    "subject_name" TEXT NOT NULL,
    "mentor_id" INTEGER NOT NULL,
    FOREIGN KEY ("batch_number") REFERENCES "batches"("batch_number"),
    FOREIGN KEY ("mentor_id") REFERENCES "mentors"("id")
);

CREATE TABLE "assignments" (
    "id" INTEGER PRIMARY KEY,
    "subject_id" INTEGER NOT NULL,
    "assignment_topic" TEXT NOT NULL,
    "total_score" INTEGER,
    FOREIGN KEY ("subject_id") REFERENCES "subjects"("id")
);

CREATE TABLE "grades" (
    "intern_id" INTEGER NOT NULL,
    "assignment_id" INTEGER NOT NULL,
    "score" INTEGER NOT NULL,
    PRIMARY KEY ("intern_id", "assignment_id"),
    FOREIGN KEY ("intern_id") REFERENCES "interns"("id"),
    FOREIGN KEY ("assignment_id") REFERENCES "assignments"("id")
);