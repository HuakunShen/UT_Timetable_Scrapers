import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Chip from '@material-ui/core/Chip';
import Paper from '@material-ui/core/Paper';
import TagFacesIcon from '@material-ui/icons/TagFaces';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    justifyContent: 'center',
    flexWrap: 'wrap',
    listStyle: 'none',
    padding: theme.spacing(0.5),
    margin: 0,
  },
  chip: {
    margin: theme.spacing(0.5),
  },
}));

const SelectedCourses = (props) => {
  const classes = useStyles();
  const { courses } = props;
  // const courses = [{ code: 'CSC301' }];

  React.useEffect(() => {
    console.log(courses);
  }, [courses]);

  return (
    <Paper component="ul" className={classes.root}>
      {courses &&
        courses.map((course, index) => {
          return (
            <li key={index}>
              <Chip
                label={course.code}
                onDelete={(e) => props.removeSelectedCourse(course.courseId)}
                className={classes.chip}
              />
            </li>
          );
        })}
    </Paper>
  );
};
export default SelectedCourses;
