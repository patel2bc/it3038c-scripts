const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    myTotalMem=(os.totalmem() / 1000000);
    myFreeMem=(os.freemem() / 1000000);
    myOSdays=Math.floor(os.uptime() / 86000);
    myOShrs=Math.floor(os.uptime() % (3600*24) / 3600);
    myOSmins=Math.floor(os.uptime() % 3600 / 60);
    myOSseconds=Math.floor(os.uptime() % 60);
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${myOSdays} Hours: ${myOShrs} Minutes: ${myOSmins} Seconds: ${myOSseconds}</p>
        <p>Total Memory: ${myTotalMem} MB</p>
        <p>Free Memory: ${myFreeMem}</p>
        <p>Number of CPUs: ${os.cpus().length}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");