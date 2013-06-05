fs   = require 'fs'
toMd = require('to-markdown').toMarkdown

filename = process.argv[process.argv.length - 1]

fs.writeFileSync filename, toMd fs.readFileSync filename, 'utf-8'
