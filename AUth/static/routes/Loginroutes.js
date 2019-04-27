var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'your-password',
  database : 'webpages'
});
connection.connect(function(err){
if(!err) {
    console.log("Database is connected ... nn");
} else {
    console.log("Error connecting database ... nn");
}
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "CREATE TABLE users(name VARCHAR(100) COLLATE utf8_unicode_ci NOT NULL, email VARCHAR(100) COLLATE utf8_unicode_ci NOT NULL, password VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL, mobile INTEGER(20) NOT NULL, degree VARCHAR(100) NOT NULL, regno INTEGER(20) NOT NULL, rollno INTEGER(20) NOT NULL, dept VARCHAR(20) NOT NULL, yog INTEGER(20) NOT NULL);";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
});