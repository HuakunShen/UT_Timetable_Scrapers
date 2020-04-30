import React, { useEffect, useState, useRef } from 'react';
import { fade, makeStyles } from '@material-ui/core/styles';
import Collapse from '@material-ui/core/Collapse';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import '../stylesheets/searchbardropdown.scss';
import Axios from 'axios';
import $ from 'jquery';

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
  const [searchRes, setSearchRes] = useState(null);
  const [timer, setTimer] = useState(null);
  const inputRef = useRef();

  const handleClick = () => {
    setOpen(!open);
  };

  const searchCourseCode = async () => {
    // console.log(search);

    try {
      const res = await Axios.get('/api/courses', {
        params: {
          code: searchInput,
        },
      });
      setSearchRes(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  // on mount
  useEffect(() => {
    $(document).keyup(function (e) {
      console.log(e.key);
      if (e.key === 'Escape' && open) {
        setOpen(false);
      }
    });
    $(
      $(document).click(function (e) {
        console.log(e.target.id);

        if (
          !$(e.target).closest('.result-list').length &&
          e.target.id !== 'search-box'
        ) {
          setOpen(false);
        }
      })
    );
  }, []);

  // while inputing
  useEffect(() => {
    // console.log('Search Content Changing: ', searchInput);
    if (timer) clearTimeout(timer);
    setTimer(
      setTimeout(() => {
        searchCourseCode(searchInput);
      }, 700)
    );
  }, [searchInput]);

  // search results changed
  useEffect(() => {
    if (searchRes) console.log(Object.keys(searchRes));
  }, [searchRes]);

  // input on change
  const inputOnChange = (e) => {
    setSearchInput(e.target.value);
  };

  return (
    <div className="search-bar-dropdown">
      <List component="div" disablePadding>
        <div className="search-box-container">
          <input
            id="search-box"
            type="text"
            ref={inputRef}
            onSelect={(e) => {
              console.log('selected');

              setOpen(true);
            }}
            // onClick={(e) => {
            //   console.log('clicked');

            //   searchCourseCode();
            // }}
            onChange={inputOnChange}
          />
          <i className="fas fa-search" />
        </div>
        <Collapse
          in={open}
          className={classes.collapse_list}
          timeout="auto"
          unmountOnExit
        >
          <div className="result-list">
            {searchRes &&
              Object.keys(searchRes).map((item, index) => {
                return (
                  <React.Fragment key={index}>
                    <div
                      className="nested-item"
                      onClick={(e) =>
                        (inputRef.current.value = `${item}-${searchRes[item].courseTitle}`)
                      }
                    >{`${item}-${searchRes[item].courseTitle}`}</div>
                    <Divider />
                  </React.Fragment>
                );
              })}
          </div>
        </Collapse>
      </List>
    </div>
  );
};

export default SearchbarDropdown;
