import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import '../stylesheets/timetable.scss';

const columns = [
  { id: 'Time', label: 'Time', minWidth: 50, align: 'center' },
  { id: 'Monday', label: 'Monday', minWidth: 70, align: 'center' },
  {
    id: 'Tuesday',
    label: 'Tuesday',
    minWidth: 70,
    align: 'center',
  },
  {
    id: 'Wednesday',
    label: 'Wednesday',
    minWidth: 70,
    align: 'center',
  },
  {
    id: 'Thursday',
    label: 'Thursday',
    minWidth: 70,
    align: 'center',
  },
  {
    id: 'Friday',
    label: 'Friday',
    minWidth: 70,
    align: 'center',
  },
];

function createData(Time, Monday, Tuesday, Wednesday, Thursday, Friday) {
  return { Time, Monday, Tuesday, Wednesday, Thursday, Friday };
}

const useStyles = makeStyles({
  root: {
    width: '100%',
  },
  container: {
    maxHeight: '100vh',
  },
});

const Timetable = (props) => {
  const classes = useStyles();
  const { schedules } = props;
  const [tableRows, setTableRows] = useState([]);
  const initEmptyRows = () => {
    const rows = [];
    for (let i = 9; i < 21; i++) {
      rows.push(
        createData(`${i % 12 === 0 ? 12 : i % 12}:00`, '', '', '', '', '')
      );
    }
    setTableRows(rows);
  };

  // on mount
  useEffect(() => {
    initEmptyRows();
  }, []);

  // add schedules
  useEffect(() => {}, [schedules]);

  return (
    <div className="timetable-page">
      <Paper className={classes.root}>
        <TableContainer className={classes.container}>
          <Table stickyHeader aria-label="sticky table">
            <TableHead>
              <TableRow>
                {columns.map((column, index) => (
                  <TableCell
                    key={index}
                    align={column.align}
                    style={{ minWidth: column.minWidth }}
                  >
                    {column.label}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {tableRows.map((row, index) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={index}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      return (
                        <TableCell key={column.id} align={column.align}>
                          {column.format && typeof value === 'number'
                            ? column.format(value)
                            : value}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </div>
  );
};
export default Timetable;
