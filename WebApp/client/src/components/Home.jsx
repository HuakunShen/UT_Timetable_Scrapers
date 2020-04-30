import React, { useState, useRef, useEffect } from 'react';
import Timetable from './Timetable';
import Paper from '@material-ui/core/Paper';
import '../stylesheets/home.scss';
import { makeStyles } from '@material-ui/core/styles';
import Navbar from './Navbar';
import SearchbarDropdown from './SearchbarDropdown';
import IconButton from '@material-ui/core/IconButton';
import SelectedCourses from './SelectedCourses';
// import Button from '@material-ui/core/Button';
const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.background.default,
    borderRadius: 0,
  },
  offset: theme.mixins.toolbar,
}));

const Home = () => {
  const classes = useStyles();
  const [selectedCourses, setSelectedCourses] = useState([]);
  const selectCourse = (course) => {
    setSelectedCourses(selectedCourses.concat([course]));
  };
  const removeSelectedCourse = (courseId) => {
    setSelectedCourses(
      selectedCourses.filter((course) => course.courseId !== courseId)
    );
  };
  return (
    <Paper className={classes.root}>
      <Navbar position="fixed" />
      <div className={classes.offset} />
      <div className="home-page">
        <div className="container-fluid pt-1">
          <div className="row">
            <div className="col-md-3 tools">
              <SearchbarDropdown selectCourse={selectCourse} />
              <br />
              {selectedCourses.length > 0 && (
                <React.Fragment>
                  <SelectedCourses
                    courses={selectedCourses}
                    removeSelectedCourse={removeSelectedCourse}
                  />
                  <div className="text-center mt-2">
                    <span className="generate-paln-btn">
                      <IconButton>
                        <i className="fas fa-rocket-launch"></i>
                      </IconButton>
                      Generate
                    </span>
                  </div>
                </React.Fragment>
              )}
            </div>
            <div className="col-md-9">
              <Timetable />
            </div>
          </div>
        </div>
      </div>
    </Paper>
  );
};

export default Home;
