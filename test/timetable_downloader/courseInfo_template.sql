use public;
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
  `session` int(11) DEFAULT NULL,
  `breadthCategories` text,
  PRIMARY KEY (`full_course_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `instructors` (
  `instructorId` varchar(40) NOT NULL,
  `firstName` text,
  `lastName` text,
  PRIMARY KEY (`instructorId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `meetings` (
  `meetingId` int(11) NOT NULL,
  `teachingMethod` varchar(45) DEFAULT NULL,
  `sectionNumber` varchar(45) DEFAULT NULL,
  `subtitle` varchar(45) DEFAULT NULL,
  `cancel` varchar(45) DEFAULT NULL,
  `waitlist` varchar(45) DEFAULT NULL,
  `online` varchar(45) DEFAULT NULL,
  `enrollmentCapacity` varchar(45) DEFAULT NULL,
  `actualEnrolment` varchar(45) DEFAULT NULL,
  `actualWaitlist` varchar(45) DEFAULT NULL,
  `enrollmentIndicator` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`meetingId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `schedules` (
  `meetingScheduleId` varchar(45) NOT NULL,
  `meetingId` varchar(45) DEFAULT NULL,
  `meetingDay` varchar(45) DEFAULT NULL,
  `meetingStartTime` varchar(45) DEFAULT NULL,
  `meetingEndTime` varchar(45) DEFAULT NULL,
  `assignedRoom1` varchar(45) DEFAULT NULL,
  `assignedRoom2` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`meetingScheduleId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
