import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
}));

const Navbar = ({ position }) => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position={`${position ? position : 'static'}`} color="default">
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="menu"
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" color="inherit">
            Plan
          </Typography>
          <div className={classes.grow} />
          <IconButton color="inherit" size="small">
            <i className="fas fa-share-square"></i>
          </IconButton>
        </Toolbar>
      </AppBar>
    </div>
  );
};
export default Navbar;
