import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Timetable from './Timetable';
import Paper from '@material-ui/core/Paper';
import '../stylesheets/home.scss';
// import Button from '@material-ui/core/Button';
const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.background.default,
    borderRadius: 0,
  },
}));

const Home = () => {
  const classes = useStyles();

  return (
    <Paper className={classes.root}>
      <div className="home-page">
        <div className="container-fluid">
          <div className="row">
            <div className="col-md-3 tools"></div>
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
