fs = require('fs')
fs.readFile('data.json', 'utf8', function (err,contents) {
    if (err) {
        return console.log(err);
    }
    var data = JSON.parse(contents)
    console.log(data);
});
