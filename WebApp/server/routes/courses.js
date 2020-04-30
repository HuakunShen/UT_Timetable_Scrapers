const Axios = require('axios');

const express = require('express');
const router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  Axios.get('https://timetable.iit.artsci.utoronto.ca/api/20205/courses', {
    params: req.query,
  })
    .then((data) => {
      console.log(data.data);
      res.send(data.data);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).send(err);
    });
});

module.exports = router;
