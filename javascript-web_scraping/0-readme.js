#!/usr/bin/node

const fs = require('fs');

const content = fs.readFileSync(process.argv[2], 'utf8');

console.log(content);
