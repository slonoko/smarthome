"use strict";

const _ = require("lodash");
const { Pool } = require("pg");

module.exports = {
  current: (event, context) =>
    new Promise((resolve, reject) => {
      const pool = new Pool();
      pool
        .query("SELECT NOW()")
        .then(res => {
          console.info(`now is ${res.rows[0].now}`);
          var cur_time = res.rows[0].now;
          pool.end();
          resolve({ now: cur_time });
        })
        .catch(err => {
          console.error(err);
          reject({ error: err.stack });
        });
    }),
  range: (event, context) => new Promise((resolve, reject) =>{
    resolve({'value':'ok'});
  })
};
