import React, { useState, useRef, useEffect } from 'react';
import Timetable from './Timetable';
import Paper from '@material-ui/core/Paper';
import '../stylesheets/home.scss';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import InputBase from '@material-ui/core/InputBase';
import { fade, makeStyles } from '@material-ui/core/styles';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';
import TextField from '@material-ui/core/TextField';
import Navbar from './Navbar';
import SearchbarDropdown from './SearchbarDropdown';
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

  return (
    <Paper className={classes.root}>
      <Navbar position="fixed" />
      <div className={classes.offset} />
      <div className="home-page">
        <div className="container-fluid pt-1">
          <div className="row">
            <div className="col-md-3 tools">
              <SearchbarDropdown />
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
