BEGIN;
CREATE TABLE `dmWeibo_demonmirror` (
    `uid` varchar(140) NOT NULL PRIMARY KEY,
    `access_token` varchar(140) NOT NULL,
    `expires_in` varchar(140) NOT NULL
)
;
CREATE TABLE `dmWeibo_photo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `text` varchar(140) NOT NULL,
    `idstr` varchar(140),
    `thumbnail_pic` varchar(140) NOT NULL,
    `original_pic` varchar(140) NOT NULL,
    `post_by` varchar(140) NOT NULL,
    `post_name` varchar(140) NOT NULL,
    `retweet_by` varchar(140) NOT NULL,
    `source` varchar(140) NOT NULL,
    `is_show` smallint NOT NULL,
    `status` smallint NOT NULL,
    `post_on` datetime,
    `retweet_on` datetime,
    `pass_on` datetime,
    `mark` numeric(4, 1) NOT NULL,
    `marked_num` integer NOT NULL
)
;

COMMIT;
