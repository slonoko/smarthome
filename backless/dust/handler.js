'use strict';

const _ = require('lodash');
const { Pool, Client } = require('pg');

module.exports = {
  dust(event, context) {
    const pool = new Pool();
    pool.query('SELECT NOW()', (err, res) => {
      console.log(err, res);
      pool.end();
      return res.rows[0];
    });
  }
};
