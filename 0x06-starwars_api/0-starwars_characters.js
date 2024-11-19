#!/usr/bin/node
const assert = require('assert');
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api';
const id = process.argv[2];

assert.notStrictEqual(id, undefined);

request.get(`${baseUrl}/films/${id}/`, (error, response, body) => {
  assert.strictEqual(error, null);
  assert.notStrictEqual(response, null);
  assert.strictEqual(response.statusCode, 200);

  const characters = JSON.parse(body).characters;

  if (characters.length === 0) return;

  const printCharacter = (index) => {
    request.get(characters[index], (error, response, body) => {
      assert.strictEqual(error, null);
      assert.notStrictEqual(response, null);
      assert.strictEqual(response.statusCode, 200);

      console.log(JSON.parse(body).name);
      if (characters[index + 1] !== undefined) printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
