BEGIN;
CREATE TABLE `auth_permission` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `content_type_id` integer NOT NULL,
    `codename` varchar(100) NOT NULL,
    UNIQUE (`content_type_id`, `codename`)
)
;
ALTER TABLE `auth_permission` ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
CREATE TABLE `auth_group_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`group_id`, `permission_id`)
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_group` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(80) NOT NULL UNIQUE
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_user_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`user_id`, `permission_id`)
)
;
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_user_groups` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL,
    UNIQUE (`user_id`, `group_id`)
)
;
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `username` varchar(30) NOT NULL UNIQUE,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(30) NOT NULL,
    `email` varchar(75) NOT NULL,
    `password` varchar(128) NOT NULL,
    `is_staff` bool NOT NULL,
    `is_active` bool NOT NULL,
    `is_superuser` bool NOT NULL,
    `last_login` datetime NOT NULL,
    `date_joined` datetime NOT NULL
)
;
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `auth_permission_1bb8f392` ON `auth_permission` (`content_type_id`);



INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can add user', 3, 'add_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can change user', 3, 'change_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can delete user', 3, 'delete_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can add content type', 4, 'add_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can change content type', 4, 'change_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add session', 5, 'add_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change session', 5, 'change_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete session', 5, 'delete_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can add site', 6, 'add_site');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can change site', 6, 'change_site');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can delete site', 6, 'delete_site');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can add demon mirror', 7, 'add_demonmirror');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can change demon mirror', 7, 'change_demonmirror');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can delete demon mirror', 7, 'delete_demonmirror');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can add photo', 8, 'add_photo');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can change photo', 8, 'change_photo');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can delete photo', 8, 'delete_photo');


INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$10000$M7tdL3b5rJkF$UNc787VaHWbf47626hbyvHqrU+g3vQxgxsGl9VosAfs=', '2014-11-10 08:05:24', true, 'shawn', '', '', 'shawn@shawn.com', true, true, '2014-11-06 02:51:24');


CREATE TABLE django_content_type (
    id int NOT NULL AUTO_INCREMENT, 
    name varchar(100) NOT NULL, 
    app_label varchar(100) NOT NULL, 
    model varchar(100) NOT NULL, 
    PRIMARY KEY (id), CONSTRAINT app_label UNIQUE (app_label, model)
);

CREATE TABLE django_session (
    session_key varchar(40) NOT NULL, 
    session_data longtext NOT NULL, 
    expire_date datetime NOT NULL, 
    PRIMARY KEY (session_key), 
    INDEX django_session_b7b81f0c (expire_date)
);

CREATE TABLE django_site (
    id int NOT NULL AUTO_INCREMENT, 
    domain varchar(100) NOT NULL, 
    name varchar(50) NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO django_content_type (id, name, app_label, model) VALUES (1, 'permission', 'auth', 'permission');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (2, 'group', 'auth', 'group');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (3, 'user', 'auth', 'user');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (4, 'content type', 'contenttypes', 'contenttype');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (5, 'session', 'sessions', 'session');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (6, 'site', 'sites', 'site');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (7, 'demon mirror', 'dmWeibo', 'demonmirror');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (8, 'photo', 'dmWeibo', 'photo');
INSERT INTO django_site (id, domain, name) VALUES (1, 'example.com', 'example.com');
COMMIT;