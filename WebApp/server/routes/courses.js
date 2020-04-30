const Axios = require('axios');

const express = require('express');
const router = express.Router();

const attributesToKeep = [
  'courseId',
  'courseTitle',
  'code',
  'meetings',
  'session',
  'section',
  'courseDescription',
  'breadthCategories',
];
/* GET home page. */
router.get('/', (req, res, next) => {
  Axios.get('https://timetable.iit.artsci.utoronto.ca/api/20205/courses', {
    params: req.query,
  })
    .then((data) => {
      const returnData = data.data;
      for (let [key, value] of Object.entries(returnData)) {
        for (let [meetingKey, meetingValue] of Object.entries(
          returnData[key]['meetings']
        )) {
          // delete enrollment control data which is relatively large, > 15 times of space
          delete returnData[key]['meetings'][meetingKey]['enrollmentControls'];
        }
      }
      res.send(returnData);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).send(err);
    });
});

module.exports = router;
