const Axios = require('axios');

Axios.get(
  'https://timetable.iit.artsci.utoronto.ca/api/20195/courses?org=&code=CSC&section=&studyyear=&daytime=&weekday=&prof=&breadth=&online=&waitlist=&available=&title='
)
  .then((res) => {
    console.log(res.data);
  })
  .catch((err) => {
    console.log(err);
  });
