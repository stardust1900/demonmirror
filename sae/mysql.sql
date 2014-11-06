DROP DATABASE IF EXISTS `demonmirror`;
CREATE DATABASE `demonmirror` DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
USE 'demonmirror';
GRANT ALL PRIVILEGES ON demonmirror.* TO 'demonmirror'@'localhost' IDENTIFIED BY 'demonmirror' WITH GRANT OPTION;
FLUSH PRIVILEGES;