const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const courseSchema = new Schema({
    fullCourseCode: {
        type: String,
        required: true,
        trim: true,
        unique: true,
        minlength: 6
    },
    courseId: {
        type: Number,
        required: false,
    },
    code: {
        type: String,
        required: true,
    },
    org: {
        type: String,
        required: false,
    },
    orgName: {
        type: String,
        required: false,
    },
    courseTitle: {
        type: String,
        required: true,
    },
    section: {
        type: String,
        required: false,
    },
    session: {
        type: Number,
        required: false,
    },
    breadth: {
        type: String,
        required: false,
    },
    courseDescription: {
        type: String,
        required: false,
    },
    prerequisite: {
        type: String,
        required: false,
    },
    corequisite: {
        type: String,
        required: false,
    },
    exclusion: {
        type: String,
        required: false,
    },
    recommendedPreparation: {
        type: String,
        required: false,
    },
});

const Course = mongoose.model('Course', courseSchema);

module.exports = Course;
