CREATE TABLE `courseInfo` (
  `full_course_code` varchar(1000) NOT NULL,
  `courseId` int(11) DEFAULT NULL,
  `code` varchar(1000) DEFAULT NULL,
  `org` varchar(1000) DEFAULT NULL,
  `orgName` varchar(1000) DEFAULT NULL,
  `courseTitle` varchar(1000) DEFAULT NULL,
  `courseDescription` varchar(1000) DEFAULT NULL,
  `prerequisite` varchar(1000) DEFAULT NULL,
  `corequisite` varchar(1000) DEFAULT NULL,
  `exclusion` varchar(1000) DEFAULT NULL,
  `recommendedPreparation` varchar(1000) DEFAULT NULL,
  `section` varchar(1000) DEFAULT NULL,
  `session` varchar(1000) DEFAULT NULL,
  `breadthCategories` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`full_course_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;