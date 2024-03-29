-- MySQL Script generated by MySQL Workbench
-- Thu 01 Apr 2021 12:30:57 PM CDT
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema blackswan_event_tracker
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `blackswan_event_tracker` ;

-- -----------------------------------------------------
-- Schema blackswan_event_tracker
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `blackswan_event_tracker` ;
USE `blackswan_event_tracker` ;

-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`user` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(90) NOT NULL,
  `website` VARCHAR(90) NOT NULL,
  `displayname` VARCHAR(90) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`location` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`location` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `gps_long` DOUBLE NULL,
  `gps_lat` DOUBLE NULL,
  `name` VARCHAR(200) NULL,
  `radius` DOUBLE NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`post` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(90) NULL,
  `date` DATE NULL,
  `time` TIME NULL,
  `description` VARCHAR(500) NULL,
  `like_num` INT NULL,
  `comment_num` INT NULL,
  `dislike_num` INT NULL,
  `is_comment` TINYINT NULL,
  `parentid` INT NULL,
  `url` VARCHAR(500) NULL,
  `issensitive` TINYINT NULL,
  `language` VARCHAR(45) NULL,
  `sharecount` INT NULL,
  `idUser` INT NULL,
  `idLocation` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `idUser_idx` (`idUser` ASC) VISIBLE,
  INDEX `idLocation_idx` (`idLocation` ASC) VISIBLE,
  CONSTRAINT `fk_idUser_post`
    FOREIGN KEY (`idUser`)
    REFERENCES `blackswan_event_tracker`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idLocation_post`
    FOREIGN KEY (`idLocation`)
    REFERENCES `blackswan_event_tracker`.`location` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`event` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`event` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `date_start` DATE NULL,
  `time_start` TIME NULL,
  `date_end` DATE NULL,
  `time_end` TIME NULL,
  `idlocation` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `idlocation_idx` (`idlocation` ASC) VISIBLE,
  CONSTRAINT `fk_idlocation_event`
    FOREIGN KEY (`idlocation`)
    REFERENCES `blackswan_event_tracker`.`location` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`tag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`tag` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`tag` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`tagevent`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`tagevent` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`tagevent` (
  `idtag` INT NOT NULL,
  `idevent` INT NOT NULL,
  INDEX `idevent_idx` (`idevent` ASC) VISIBLE,
  PRIMARY KEY (`idtag`, `idevent`),
  CONSTRAINT `fk_idtag_tag`
    FOREIGN KEY (`idtag`)
    REFERENCES `blackswan_event_tracker`.`tag` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idevent_tag`
    FOREIGN KEY (`idevent`)
    REFERENCES `blackswan_event_tracker`.`event` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`url`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`url` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`url` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `url_UNIQUE` (`url` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`url_post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`url_post` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`url_post` (
  `idPost` INT NOT NULL,
  `idurl` INT NOT NULL,
  INDEX `idurl_idx` (`idurl` ASC) VISIBLE,
  PRIMARY KEY (`idPost`, `idurl`),
  CONSTRAINT `fk_idpost_url`
    FOREIGN KEY (`idPost`)
    REFERENCES `blackswan_event_tracker`.`post` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idurl_url`
    FOREIGN KEY (`idurl`)
    REFERENCES `blackswan_event_tracker`.`url` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`media`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`media` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`media` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data` LONGBLOB NOT NULL,
  `media_type` VARCHAR(45) NULL,
  `runtime` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`media_post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`media_post` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`media_post` (
  `idpost` INT NOT NULL,
  `idmedia` INT NOT NULL,
  INDEX `idPost_idx` (`idpost` ASC) VISIBLE,
  INDEX `idmedia_idx` (`idmedia` ASC) VISIBLE,
  PRIMARY KEY (`idpost`, `idmedia`),
  CONSTRAINT `fk_idpost_media`
    FOREIGN KEY (`idpost`)
    REFERENCES `blackswan_event_tracker`.`post` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idmedia_media`
    FOREIGN KEY (`idmedia`)
    REFERENCES `blackswan_event_tracker`.`media` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blackswan_event_tracker`.`postevent`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blackswan_event_tracker`.`postevent` ;

CREATE TABLE IF NOT EXISTS `blackswan_event_tracker`.`postevent` (
  `idevent` INT NOT NULL,
  `idPost` INT NOT NULL,
  INDEX `idPost_idx` (`idPost` ASC) VISIBLE,
  INDEX `idevent_idx` (`idevent` ASC) VISIBLE,
  PRIMARY KEY (`idevent`, `idPost`),
  CONSTRAINT `fk_idevent_post`
    FOREIGN KEY (`idevent`)
    REFERENCES `blackswan_event_tracker`.`event` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idpost_post`
    FOREIGN KEY (`idPost`)
    REFERENCES `blackswan_event_tracker`.`post` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;





SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
