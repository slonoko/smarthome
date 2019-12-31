'use strict';

const _ = require('lodash');
const { Pool, Client } = require('pg');

module.exports = {
  dust(event, context) {
    const pool = new Pool();
    var _time;
    pool.query('SELECT NOW()', (err, res) => {
      console.log(err, res);
      _time = res;
      pool.end();
    });
    return {'now': 'test2'};
  },
};
