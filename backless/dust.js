"use strict";

const { Pool } = require("pg");

module.exports = {
  current: (event, context) =>
    new Promise((resolve, reject) => {
      const pool = new Pool();
      pool
        .query("select * from dust order by enddate desc limit 1")
        .then(res => {
          var data = { value: "empty" };
          if (res.rows.length > 0) data = res.rows[0];
          pool.end();
          resolve(data);
        })
        .catch(err => {
          console.error(err);
          reject({ error: err.stack });
        });
    }),
  range: (event, context) =>
    new Promise((resolve, reject) => {
      const pool = new Pool();

      const query = {
        text:
          "select * from dust where startdate between $1::timestamp and $2::timestamp order by startdate desc",
        values: [event.data.from_date, event.data.to_date]
      };
      pool
        .query(query)
        .then(res => {
          var data = { value: "empty" };
          if (res.rows.length > 0) data = res.rows;
          pool.end();
          resolve(data);
        })
        .catch(err => {
          console.error(err);
          reject({ error: err.stack });
        });
    })
};
