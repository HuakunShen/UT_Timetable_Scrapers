const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const fetch = require('node-fetch');
const log = console.log;
const load = true;
const url = "https://timetable.iit.artsci.utoronto.ca/api/20199/courses";
let Course = require('./models/course.model');
const alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());
const uri = process.env.ATLAS_URI;

mongoose.connect(uri, {useNewUrlParser: true, useCreateIndex: true}
);

const connection = mongoose.connection;
connection.once('open', () => {
    log("MongoDB database connection established successfully");
    if (load) {
        loadData((res) => {
                return res;
            }
        );
    }

});


function loadData() {
    alphabet.forEach((l) => {
            fetch(url + "?code=" + l)
                .then((res) => {
                    let result = res.json();
                    return result;
                })
                .then(res => {
                    if (res instanceof Array) {
                        log("No courses fetched for letter " + l);
                        return res;
                    }
                    for (let courseCode in res) {
                        const c = res[courseCode];
                        let course = new Course({
                            fullCourseCode: courseCode,
                            courseId: c.courseId,
                            code: c.code,
                            org: c.org,
                            orgName: c.orgName,
                            courseTitle: c.courseTitle,
                            section: c.section,
                            session: c.session,
                            breadth: c.breadthCategories,
                            courseDescription: c.courseDescription,
                            prerequisite: c.prerequisite,
                            corequisite: c.corequisite,
                            exclusion: c.exclusion,
                            recommendedPreparation: c.recommendedPreparation,
                        });
                        course.save()
                            .catch(error => {
                                if (error.code === 11000) {
                                    log(`Duplicated course ${course.code}, skipped`);
                                } else {
                                    return log(error);
                                }
                            })
                            .then(log(`Course ${course.code} added!`));

                    }

                    return res;
                })
                .catch(() => {
                    console.log(
                        "Did not fetch correctly"
                    );
                });
        }
    );
}


// const exercisesRouter = require('./routes/exercises');
// const usersRouter = require('./routes/users');
//
// app.use('/exercises', exercisesRouter);
// app.use('/users', usersRouter);


app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});
