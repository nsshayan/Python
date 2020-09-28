- 
  expect: 'Name .*: '
  send: testuser
  timeout: 10
-
  expect: 'Password: '
  send: w3lc0me
- 
  expect: 'ftp> '
  send_commands:
    - cd /www/files/python
    - get may27.zip
    - quit
