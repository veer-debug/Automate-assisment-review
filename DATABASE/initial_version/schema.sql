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
    "date_of_birth" NUMERIC NOT NULL,
    "gender" TEXT CHECK("gender" IN ('Male', 'Female', 'Other')),
    "batch_number" INTEGER NOT NULL,
    FOREIGN KEY ("batch_number") REFERENCES "batches" ("batch_number")
);

CREATE TABLE "instructors" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "phone" TEXT NOT NULL UNIQUE
);

CREATE TABLE "subjects" (
    "id" INTEGER PRIMARY KEY,
    "subject_name" TEXT NOT NULL,
    "instructor_id" INTEGER NOT NULL,
    FOREIGN KEY ("instructor_id") REFERENCES "instructors" ("id")
);

CREATE TABLE "passion_project" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "type" TEXT,
    "head_instructor" INTEGER,
    "guide_instructor1" INTEGER,
    "guide_instructor2" INTEGER,
    FOREIGN KEY ("head_instructor") REFERENCES "instructors" ("id"),
    FOREIGN KEY ("guide_instructor1") REFERENCES "instructors" ("id"),
    FOREIGN KEY ("guide_instructor2") REFERENCES "instructors" ("id")
);

CREATE TABLE "assignments" (
    "id" INTEGER PRIMARY KEY,
    "subject_id" INTEGER NOT NULL,
    "assignment_topic" TEXT NOT NULL,
    "total_score" INTEGER,
    "instructor_id" INTEGER NOT NULL,
    FOREIGN KEY ("subject_id") REFERENCES "subjects" ("id"),
    FOREIGN KEY ("instructor_id") REFERENCES "instructors" ("id")
);

CREATE TABLE "grades" (
    "intern_id" INTEGER NOT NULL,
    "assignment_id" INTEGER NOT NULL,
    "teacher_id" INTEGER,
    "score" INTEGER NOT NULL,
    "date" NUMERIC,
    PRIMARY KEY ("intern_id", "assignment_id"),
    FOREIGN KEY ("intern_id") REFERENCES "interns" ("id"),
    FOREIGN KEY ("assignment_id") REFERENCES "assignments" ("id"),
    FOREIGN KEY ("teacher_id") REFERENCES "instructors" ("id")
);

CREATE TABLE "batch_subject" (
    "batch_id" INTEGER,
    "subject_id" INTEGER,
    PRIMARY KEY ("batch_id", "subject_id"),
    FOREIGN KEY ("batch_id") REFERENCES "batches" ("batch_number"),
    FOREIGN KEY ("subject_id") REFERENCES "subjects" ("id")
);

CREATE TABLE "batch_instructor" (
    "batch_id" INTEGER,
    "instructor_id" INTEGER,
    PRIMARY KEY ("batch_id", "instructor_id"),
    FOREIGN KEY ("batch_id") REFERENCES "batches" ("batch_number"),
    FOREIGN KEY ("instructor_id") REFERENCES "instructors" ("id")
);