# tocak
A lightweight web server

![Github stars](https://img.shields.io/github/stars/chzane/tocak.svg?style=for-the-badge)
![Team](https://img.shields.io/badge/TEAM-Solariix-blue?style=for-the-badge)
![Team](https://img.shields.io/badge/License-MIT-blue?style=social)
***
**_The project continues to update, some functions may not be perfect, has a better suggestion please submit issues_**
***
Hi, thank you for using tocak as your web application server system.

Tocak is a lightweight web application server system, it can help you quickly on your web applications.
## install
This project uses python3 or python2. Go check them out if you don't have them locally installed.
```shell
git clone https://github.com/chzane/tocak.git
```
## Usage
Open the `web.config.tocak` file, this is the web application configuration file, you can change here application port, set up the index file, set the error page, etc.

It's format should be like this

```json
{
  "http_config": {
    "index": "./webapp/",
    "port": "8888"
  },
  "error_page": {
    "404": " <title>404 error</title><h1>404 error</h1><hr><p>sorry,file not found.<br>Please check the URL you entered or contact developers.</p><p>tocak</p>"
    ... ...
  }
}
```

`http_config` used to set the basic operating parameters.

`error_page` used to set the error page.

### http_config
`index` : Set the directory of web app store, the default is `webapp`, we do not recommend changes.

`port` : Set web application port.

### error_page
`ERRORCODE` : like `404`,`502`,etc.After setting error page.

## License
![Team](https://img.shields.io/badge/License-MIT-blue?style=social) @chzane
