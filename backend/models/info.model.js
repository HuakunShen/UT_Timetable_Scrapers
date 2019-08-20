const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const instructorSchema = new Schema({
    id: {type: int, required: true, unique: true},
    firstName: {type: String, required: false},
    lastName: {type: String, required: false},
});


// TODO: meetings and schedules
// CREATE TABLE `meetings` (
//     `meetingId` int(11) NOT NULL,
//     `teachingMethod` varchar(45) DEFAULT NULL,
//     `sectionNumber` varchar(45) DEFAULT NULL,
//     `subtitle` varchar(45) DEFAULT NULL,
//     `cancel` varchar(45) DEFAULT NULL,
//     `waitlist` varchar(45) DEFAULT NULL,
//     `online` varchar(45) DEFAULT NULL,
//     `enrollmentCapacity` varchar(45) DEFAULT NULL,
//     `actualEnrolment` varchar(45) DEFAULT NULL,
//     `actualWaitlist` varchar(45) DEFAULT NULL,
//     `enrollmentIndicator` varchar(45) DEFAULT NULL,
//     PRIMARY KEY (`meetingId`)
// ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
//
//
// CREATE TABLE `schedules` (
//     `meetingScheduleId` varchar(45) NOT NULL,
//     `meetingId` varchar(45) DEFAULT NULL,
//     `meetingDay` varchar(45) DEFAULT NULL,
//     `meetingStartTime` varchar(45) DEFAULT NULL,
//     `meetingEndTime` varchar(45) DEFAULT NULL,
//     `assignedRoom1` varchar(45) DEFAULT NULL,
//     `assignedRoom2` varchar(45) DEFAULT NULL,
//     PRIMARY KEY (`meetingScheduleId`)
// ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


const Instructor = mongoose.model('Instructor', instructorSchema);

module.exports = Instructor;