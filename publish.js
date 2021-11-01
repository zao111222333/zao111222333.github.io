const express = require('express');
const path = require('path');
const app = express();
// 在 app 文件夹开启静态服务
app.use('/', express.static('public'));
app.get('/', function (req, res) {
  res.send('Only for SUSTech Network Accessing');
})
app.listen(50000, () => {
  console.log('Demo server listening on port http://localhost:50000');
});