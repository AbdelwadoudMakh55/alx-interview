#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const charList = JSON.parse(body).characters;
  const promises = [];
  let i = 0;
  while (i < charList.length) {
    const p = new Promise((resolve, reject) => {
      request(charList[i], function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    promises.push(p);
    i++;
  }
  Promise.all(promises)
    .then((results) => {
      results.forEach(result => {
        console.log(result);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});
