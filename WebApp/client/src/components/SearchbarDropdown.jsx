import React, { useEffect, useState } from 'react';
import { fade, makeStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import InputBase from '@material-ui/core/InputBase';
import SearchIcon from '@material-ui/icons/Search';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import Collapse from '@material-ui/core/Collapse';
import Grow from '@material-ui/core/Grow';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import ListItemText from '@material-ui/core/ListItemText';
import '../stylesheets/searchbardropdown.scss';

const useStyles = makeStyles((theme) => ({
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(1),
      width: 'auto',
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      width: '12ch',
      '&:focus': {
        width: '20ch',
      },
    },
  },
  nested: {
    paddingLeft: theme.spacing(4),
    backgroundColor: theme.palette.background.paper,

    '&:hover': {
      backgroundColor: theme.palette.default,
    },
  },
  results: {
    overflow: 'auto',
    maxHeight: 300,
  },
  collapse_list: {
    position: 'absolute',
    width: '100%',
    zIndex: 10,
  },
}));

const SearchbarDropdown = () => {
  const classes = useStyles();
  const [searchInput, setSearchInput] = useState('');
  const [open, setOpen] = useState(true);

  const handleClick = () => {
    setOpen(!open);
  };
  useEffect(() => {
    console.log('Search Content Changing: ', searchInput);
  }, [searchInput]);
  return (
    <div className="search-bar-dropdown">
      <List component="div" disablePadding>
        {/* <ListItem button className={classes.searchbar} style={{ padding: 0 }}> */}
        {/* <div className={classes.search}>
          <div className={classes.searchIcon}>
            <SearchIcon />
          </div>
          <InputBase
            placeholder="Search…"
            fullWidth
            classes={{
              root: classes.inputRoot,
              input: classes.inputInput,
            }}
            onClick={handleClick}
            onChange={(e) => setSearchInput(e.target.value)}
            value={searchInput}
            inputProps={{ 'aria-label': 'search' }}
          />
        </div> */}
        {/* </ListItem> */}
        <div className="search-box-container">
          <input type="text" onClick={handleClick} />
          <i className="fas fa-search" />
        </div>
        <Collapse
          in={open}
          className={classes.collapse_list}
          timeout="auto"
          unmountOnExit
        >
          <div className="result-list">
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
            <div className="nested-item">item</div>
            <Divider />
          </div>
        </Collapse>
      </List>
    </div>
  );
};

export default SearchbarDropdown;
