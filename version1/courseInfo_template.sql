use ut_timetable;
CREATE TABLE `course_info` (
  `full_course_code` varchar(20) NOT NULL,
  `courseId` int(11) DEFAULT NULL,
  `code` text,
  `org` text,
  `orgName` text,
  `courseTitle` text,
  `courseDescription` text,
  `prerequisite` text,
  `corequisite` text,
  `exclusion` text,
  `recommendedPreparation` text,
  `section` text,
  `session` text,
  `breadthCategories` text,
  PRIMARY KEY (`full_course_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
