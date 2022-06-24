CREATE DATABASE  IF NOT EXISTS `artgallery` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `artgallery`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: artgallery
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `билет`
--

DROP TABLE IF EXISTS `билет`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `билет` (
  `Код билета` bigint NOT NULL,
  `Дата посещения` date NOT NULL,
  `Код категории` int NOT NULL,
  `Код выставки` int NOT NULL,
  `Код посетителя` int NOT NULL,
  `Код сотрудника` int NOT NULL,
  `Штрих-код` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Код билета`),
  KEY `Код категории` (`Код категории`),
  KEY `Код выставки` (`Код выставки`),
  KEY `Код посетителя` (`Код посетителя`),
  KEY `Код сотрудника` (`Код сотрудника`),
  CONSTRAINT `билет_ibfk_1` FOREIGN KEY (`Код категории`) REFERENCES `категории` (`Код категории`),
  CONSTRAINT `билет_ibfk_2` FOREIGN KEY (`Код выставки`) REFERENCES `выставки` (`Код выставки`),
  CONSTRAINT `билет_ibfk_3` FOREIGN KEY (`Код посетителя`) REFERENCES `посетитель` (`Код посетителя`),
  CONSTRAINT `билет_ibfk_4` FOREIGN KEY (`Код сотрудника`) REFERENCES `сотрудник` (`Код сотрудника`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `билет`
--

LOCK TABLES `билет` WRITE;
/*!40000 ALTER TABLE `билет` DISABLE KEYS */;
INSERT INTO `билет` VALUES (20000101,'2000-01-01',1,1,45462526,102,'code020000101.png'),(57737320000101,'2000-01-01',4,1,45462526,103,'code57737320000101.png'),(57737420000101,'2000-01-01',1,1,45462526,102,'code57737420000101.png');
/*!40000 ALTER TABLE `билет` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `выставки`
--

DROP TABLE IF EXISTS `выставки`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `выставки` (
  `Код выставки` int NOT NULL AUTO_INCREMENT,
  `Тема выставки` varchar(255) NOT NULL,
  `Дата начала` date NOT NULL,
  `Дата окончания` date NOT NULL,
  PRIMARY KEY (`Код выставки`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `выставки`
--

LOCK TABLES `выставки` WRITE;
/*!40000 ALTER TABLE `выставки` DISABLE KEYS */;
INSERT INTO `выставки` VALUES (1,'Религия','2022-06-20','2022-06-27');
/*!40000 ALTER TABLE `выставки` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `выставленные картины`
--

DROP TABLE IF EXISTS `выставленные картины`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `выставленные картины` (
  `Код картины` int DEFAULT NULL,
  `Код выставки` int NOT NULL,
  `Код зала` int NOT NULL,
  KEY `Код картины` (`Код картины`),
  KEY `Код выставки` (`Код выставки`),
  KEY `Код зала` (`Код зала`),
  CONSTRAINT `выставленные картины_ibfk_1` FOREIGN KEY (`Код картины`) REFERENCES `картина` (`Код картины`),
  CONSTRAINT `выставленные картины_ibfk_2` FOREIGN KEY (`Код выставки`) REFERENCES `выставки` (`Код выставки`),
  CONSTRAINT `выставленные картины_ibfk_3` FOREIGN KEY (`Код зала`) REFERENCES `зал` (`Код зала`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `выставленные картины`
--

LOCK TABLES `выставленные картины` WRITE;
/*!40000 ALTER TABLE `выставленные картины` DISABLE KEYS */;
INSERT INTO `выставленные картины` VALUES (1006,1,2);
/*!40000 ALTER TABLE `выставленные картины` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `зал`
--

DROP TABLE IF EXISTS `зал`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `зал` (
  `Код зала` int NOT NULL,
  `Наименование зала` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Код зала`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `зал`
--

LOCK TABLES `зал` WRITE;
/*!40000 ALTER TABLE `зал` DISABLE KEYS */;
INSERT INTO `зал` VALUES (1,'A'),(2,'Б'),(3,'В'),(4,'Г'),(5,'Д');
/*!40000 ALTER TABLE `зал` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `история входа`
--

DROP TABLE IF EXISTS `история входа`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `история входа` (
  `Код авторизации` int NOT NULL AUTO_INCREMENT,
  `Время входа` datetime NOT NULL,
  `Логин` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Код авторизации`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `история входа`
--

LOCK TABLES `история входа` WRITE;
/*!40000 ALTER TABLE `история входа` DISABLE KEYS */;
INSERT INTO `история входа` VALUES (1,'2022-06-23 00:14:44','Ivanov@namecomp.ru'),(2,'2022-06-23 00:14:51','Ivanov@namecomp.ru'),(3,'2022-06-23 00:15:12','Ivanov@namecomp.ru'),(4,'2022-06-23 00:43:22','Ivanov@namecomp.ru'),(5,'2022-06-23 00:53:30','Ivanov@namecomp.ru'),(6,'2022-06-23 00:58:37','fedorov@namecomp.ru'),(7,'2022-06-23 13:55:23','Ivanov@namecomp.ru'),(8,'2022-06-23 13:58:11','Ivanov@namecomp.ru'),(9,'2022-06-23 13:59:24','Ivanov@namecomp.ru'),(10,'2022-06-23 14:10:28','Ivanov@namecomp.ru'),(11,'2022-06-23 14:13:42','Ivanov@namecomp.ru'),(12,'2022-06-23 14:20:35','Ivanov@namecomp.ru'),(13,'2022-06-23 14:21:01','Ivanov@namecomp.ru'),(14,'2022-06-23 14:21:39','Ivanov@namecomp.ru'),(15,'2022-06-23 15:51:25','Ivanov@namecomp.ru'),(16,'2022-06-23 15:53:06','Ivanov@namecomp.ru'),(17,'2022-06-23 16:03:25','Ivanov@namecomp.ru'),(18,'2022-06-23 16:21:50','Ivanov@namecomp.ru'),(19,'2022-06-23 16:22:41','Ivanov@namecomp.ru'),(20,'2022-06-23 16:23:27','Ivanov@namecomp.ru'),(21,'2022-06-23 16:59:20','Ivanov@namecomp.ru'),(22,'2022-06-23 17:20:30','Ivanov@namecomp.ru'),(23,'2022-06-23 17:22:36','Ivanov@namecomp.ru'),(24,'2022-06-23 17:23:00','Ivanov@namecomp.ru'),(25,'2022-06-23 17:23:58','Ivanov@namecomp.ru'),(26,'2022-06-23 17:24:20','Ivanov@namecomp.ru'),(27,'2022-06-23 17:26:19','Ivanov@namecomp.ru'),(28,'2022-06-23 17:26:47','Ivanov@namecomp.ru'),(29,'2022-06-23 17:27:51','Ivanov@namecomp.ru'),(30,'2022-06-23 17:36:33','Ivanov@namecomp.ru'),(31,'2022-06-23 17:37:03','Ivanov@namecomp.ru'),(32,'2022-06-23 17:41:17','Ivanov@namecomp.ru'),(33,'2022-06-23 17:42:48','Ivanov@namecomp.ru'),(34,'2022-06-23 17:44:23','Ivanov@namecomp.ru'),(35,'2022-06-23 17:44:46','Ivanov@namecomp.ru'),(36,'2022-06-23 17:49:10','Ivanov@namecomp.ru'),(37,'2022-06-23 17:49:33','Ivanov@namecomp.ru'),(38,'2022-06-23 17:59:21','Ivanov@namecomp.ru'),(39,'2022-06-23 18:07:44','Ivanov@namecomp.ru'),(40,'2022-06-23 18:08:12','Ivanov@namecomp.ru'),(41,'2022-06-23 18:15:42','Ivanov@namecomp.ru'),(42,'2022-06-23 18:16:07','Ivanov@namecomp.ru'),(43,'2022-06-23 18:16:21','Ivanov@namecomp.ru'),(44,'2022-06-23 18:16:59','Ivanov@namecomp.ru'),(45,'2022-06-23 18:18:25','Ivanov@namecomp.ru'),(46,'2022-06-23 18:18:50','Ivanov@namecomp.ru'),(47,'2022-06-23 18:20:03','Ivanov@namecomp.ru'),(48,'2022-06-23 18:20:54','Ivanov@namecomp.ru'),(49,'2022-06-23 18:21:22','Ivanov@namecomp.ru'),(50,'2022-06-23 18:22:43','Ivanov@namecomp.ru'),(51,'2022-06-23 18:23:29','Ivanov@namecomp.ru'),(52,'2022-06-23 18:24:28','Ivanov@namecomp.ru'),(53,'2022-06-23 18:25:02','Ivanov@namecomp.ru'),(54,'2022-06-23 18:26:00','Ivanov@namecomp.ru'),(55,'2022-06-23 18:26:29','Ivanov@namecomp.ru'),(56,'2022-06-23 18:27:04','Ivanov@namecomp.ru'),(57,'2022-06-23 18:28:50','Ivanov@namecomp.ru'),(58,'2022-06-23 18:31:25','Ivanov@namecomp.ru'),(59,'2022-06-23 18:35:25','Ivanov@namecomp.ru'),(60,'2022-06-23 18:37:01','Ivanov@namecomp.ru'),(61,'2022-06-23 18:37:24','Ivanov@namecomp.ru'),(62,'2022-06-23 18:38:47','Ivanov@namecomp.ru'),(63,'2022-06-23 18:39:26','Ivanov@namecomp.ru'),(64,'2022-06-23 18:40:01','Ivanov@namecomp.ru'),(65,'2022-06-23 18:40:16','Ivanov@namecomp.ru'),(66,'2022-06-23 18:40:48','Ivanov@namecomp.ru'),(67,'2022-06-23 18:41:03','Ivanov@namecomp.ru'),(68,'2022-06-23 18:41:39','Ivanov@namecomp.ru'),(69,'2022-06-23 19:37:03','Ivanov@namecomp.ru'),(70,'2022-06-23 19:38:05','Ivanov@namecomp.ru'),(71,'2022-06-23 19:38:55','Ivanov@namecomp.ru'),(72,'2022-06-23 19:39:30','Ivanov@namecomp.ru'),(73,'2022-06-23 19:52:10','Ivanov@namecomp.ru'),(74,'2022-06-23 19:57:29','Ivanov@namecomp.ru'),(75,'2022-06-23 21:23:22','Ivanov@namecomp.ru'),(76,'2022-06-23 21:23:37','petrov@namecomp.ru'),(77,'2022-06-23 21:25:43','petrov@namecomp.ru'),(78,'2022-06-23 21:31:48','petrov@namecomp.ru'),(79,'2022-06-23 21:39:30','petrov@namecomp.ru'),(80,'2022-06-23 21:44:24','petrov@namecomp.ru'),(81,'2022-06-23 21:48:05','petrov@namecomp.ru'),(82,'2022-06-23 21:51:43','petrov@namecomp.ru'),(83,'2022-06-23 21:53:24','fedorov@namecomp.ru'),(84,'2022-06-23 21:58:02','fedorov@namecomp.ru'),(85,'2022-06-23 21:59:04','fedorov@namecomp.ru'),(86,'2022-06-23 22:00:06','fedorov@namecomp.ru'),(87,'2022-06-23 22:00:37','fedorov@namecomp.ru'),(88,'2022-06-23 22:00:51','fedorov@namecomp.ru'),(89,'2022-06-23 22:03:40','fedorov@namecomp.ru'),(90,'2022-06-23 22:04:55','fedorov@namecomp.ru'),(91,'2022-06-23 22:06:07','fedorov@namecomp.ru'),(92,'2022-06-23 22:07:50','fedorov@namecomp.ru'),(93,'2022-06-23 22:08:17','fedorov@namecomp.ru'),(94,'2022-06-23 22:13:21','fedorov@namecomp.ru'),(95,'2022-06-23 22:14:01','fedorov@namecomp.ru'),(96,'2022-06-23 22:14:30','fedorov@namecomp.ru'),(97,'2022-06-23 22:15:45','fedorov@namecomp.ru'),(98,'2022-06-23 22:17:05','fedorov@namecomp.ru'),(99,'2022-06-23 22:18:59','fedorov@namecomp.ru'),(100,'2022-06-23 22:20:13','fedorov@namecomp.ru'),(101,'2022-06-23 22:21:58','fedorov@namecomp.ru'),(102,'2022-06-23 22:25:25','fedorov@namecomp.ru'),(103,'2022-06-23 22:26:54','fedorov@namecomp.ru'),(104,'2022-06-23 22:43:59','fedorov@namecomp.ru'),(105,'2022-06-23 22:44:36','fedorov@namecomp.ru'),(106,'2022-06-23 22:45:15','fedorov@namecomp.ru'),(107,'2022-06-23 23:06:12','fedorov@namecomp.ru'),(108,'2022-06-23 23:07:15','fedorov@namecomp.ru'),(109,'2022-06-23 23:07:58','fedorov@namecomp.ru'),(110,'2022-06-23 23:09:06','fedorov@namecomp.ru'),(111,'2022-06-23 23:10:21','fedorov@namecomp.ru'),(112,'2022-06-23 23:11:50','fedorov@namecomp.ru'),(113,'2022-06-23 23:20:21','fedorov@namecomp.ru'),(114,'2022-06-23 23:22:09','fedorov@namecomp.ru'),(115,'2022-06-23 23:22:37','fedorov@namecomp.ru'),(116,'2022-06-23 23:22:58','fedorov@namecomp.ru'),(117,'2022-06-23 23:25:06','fedorov@namecomp.ru'),(118,'2022-06-23 23:26:07','fedorov@namecomp.ru'),(119,'2022-06-23 23:26:24','fedorov@namecomp.ru'),(120,'2022-06-23 23:32:27','fedorov@namecomp.ru'),(121,'2022-06-23 23:32:46','fedorov@namecomp.ru'),(122,'2022-06-23 23:33:29','fedorov@namecomp.ru'),(123,'2022-06-23 23:33:47','fedorov@namecomp.ru'),(124,'2022-06-23 23:34:14','fedorov@namecomp.ru'),(125,'2022-06-23 23:55:21','fedorov@namecomp.ru'),(126,'2022-06-23 23:55:33','Ivanov@namecomp.ru'),(127,'2022-06-23 23:55:51','Ivanov@namecomp.ru'),(128,'2022-06-23 23:56:23','Ivanov@namecomp.ru'),(129,'2022-06-24 00:11:54','Ivanov@namecomp.ru'),(130,'2022-06-24 00:12:16','Ivanov@namecomp.ru'),(131,'2022-06-24 00:13:35','Ivanov@namecomp.ru'),(132,'2022-06-24 00:14:14','Ivanov@namecomp.ru'),(133,'2022-06-24 00:17:43','Ivanov@namecomp.ru'),(134,'2022-06-24 00:18:29','Ivanov@namecomp.ru'),(135,'2022-06-24 00:19:07','Ivanov@namecomp.ru'),(136,'2022-06-24 00:19:43','Ivanov@namecomp.ru'),(137,'2022-06-24 00:20:19','Ivanov@namecomp.ru'),(138,'2022-06-24 00:20:43','Ivanov@namecomp.ru'),(139,'2022-06-24 16:28:29','Ivanov@namecomp.ru'),(140,'2022-06-24 16:29:02','petrov@namecomp.ru'),(141,'2022-06-24 16:29:23','petrov@namecomp.ru'),(142,'2022-06-24 16:31:35','petrov@namecomp.ru'),(143,'2022-06-24 16:33:44','petrov@namecomp.ru'),(144,'2022-06-24 16:34:30','petrov@namecomp.ru'),(145,'2022-06-24 16:38:42','petrov@namecomp.ru'),(146,'2022-06-24 16:39:20','petrov@namecomp.ru'),(147,'2022-06-24 16:41:46','petrov@namecomp.ru'),(148,'2022-06-24 16:42:50','petrov@namecomp.ru'),(149,'2022-06-24 16:43:26','petrov@namecomp.ru'),(150,'2022-06-24 16:46:22','petrov@namecomp.ru'),(151,'2022-06-24 16:48:45','petrov@namecomp.ru'),(152,'2022-06-24 16:49:24','petrov@namecomp.ru'),(153,'2022-06-24 20:38:15','petrov@namecomp.ru'),(154,'2022-06-24 20:39:46','petrov@namecomp.ru'),(155,'2022-06-24 20:46:50','petrov@namecomp.ru'),(156,'2022-06-24 20:47:23','petrov@namecomp.ru'),(157,'2022-06-24 20:47:58','petrov@namecomp.ru'),(158,'2022-06-24 20:50:05','petrov@namecomp.ru'),(159,'2022-06-24 20:50:19','petrov@namecomp.ru'),(160,'2022-06-24 20:53:02','petrov@namecomp.ru'),(161,'2022-06-24 20:53:14','petrov@namecomp.ru'),(162,'2022-06-25 00:20:27','petrov@namecomp.ru'),(163,'2022-06-25 00:20:47','petrov@namecomp.ru'),(164,'2022-06-25 00:21:24','petrov@namecomp.ru'),(165,'2022-06-25 00:21:59','petrov@namecomp.ru'),(166,'2022-06-25 00:22:39','petrov@namecomp.ru'),(167,'2022-06-25 00:23:29','petrov@namecomp.ru'),(168,'2022-06-25 00:23:55','petrov@namecomp.ru'),(169,'2022-06-25 00:29:15','petrov@namecomp.ru'),(170,'2022-06-25 00:29:29','petrov@namecomp.ru'),(171,'2022-06-25 00:30:08','petrov@namecomp.ru'),(172,'2022-06-25 00:30:18','petrov@namecomp.ru'),(173,'2022-06-25 00:31:00','petrov@namecomp.ru'),(174,'2022-06-25 00:32:48','petrov@namecomp.ru'),(175,'2022-06-25 02:12:41','Ivanov@namecomp.ru'),(176,'2022-06-25 02:13:32','Ivanov@namecomp.ru'),(177,'2022-06-25 02:14:02','Ivanov@namecomp.ru'),(178,'2022-06-25 02:14:17','Ivanov@namecomp.ru'),(179,'2022-06-25 02:16:13','Ivanov@namecomp.ru'),(180,'2022-06-25 02:16:57','Ivanov@namecomp.ru');
/*!40000 ALTER TABLE `история входа` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `картина`
--

DROP TABLE IF EXISTS `картина`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `картина` (
  `Код картины` int NOT NULL AUTO_INCREMENT,
  `Название` varchar(255) NOT NULL,
  `Год написания` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Код художника` int NOT NULL,
  `Код техники` int NOT NULL,
  `Код типа` int NOT NULL,
  `Фото` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Код картины`),
  KEY `Код художника` (`Код художника`),
  KEY `Код техники` (`Код техники`),
  KEY `Код типа` (`Код типа`),
  CONSTRAINT `картина_ibfk_1` FOREIGN KEY (`Код художника`) REFERENCES `художник` (`Код художника`),
  CONSTRAINT `картина_ibfk_2` FOREIGN KEY (`Код техники`) REFERENCES `техника картины` (`Код техники`),
  CONSTRAINT `картина_ibfk_3` FOREIGN KEY (`Код типа`) REFERENCES `тип картины` (`Код типа`)
) ENGINE=InnoDB AUTO_INCREMENT=1014 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `картина`
--

LOCK TABLES `картина` WRITE;
/*!40000 ALTER TABLE `картина` DISABLE KEYS */;
INSERT INTO `картина` VALUES (1001,'Апофеоз войны','1871',1,32,2,'Апофеоз войны.jpg'),(1002,'Звездная ночь','1889',2,32,1,'Звездная ночь.jpg'),(1003,'Крик','1893',3,32,2,'Крик.jpg'),(1004,'Девятый вал','1850',4,32,2,'Девятый вал.jpg'),(1005,'Постоянство памяти','1931',5,32,1,'Постоянство памяти.jpg'),(1006,'Тайная вечеря','1495-1498',6,45,2,'Тайная вечеря.jpg'),(1007,'Мона Лиза','1503-1519',6,32,2,'Мона Лиза.jpg'),(1008,'Сотворение Адама','1511',7,14,2,'Сотворение Адама.jpg'),(1009,'Ноктюрн в чёрном и золотом. Падающая ракета','1875',8,32,1,'Ноктюрн в чёрном и золотом. Падающая ракета.jpg'),(1010,'test','test',3,11,1,'test');
/*!40000 ALTER TABLE `картина` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `категории`
--

DROP TABLE IF EXISTS `категории`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `категории` (
  `Код категории` int NOT NULL,
  `Скидка (%)` int NOT NULL,
  `Наименование категории` varchar(255) NOT NULL,
  PRIMARY KEY (`Код категории`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `категории`
--

LOCK TABLES `категории` WRITE;
/*!40000 ALTER TABLE `категории` DISABLE KEYS */;
INSERT INTO `категории` VALUES (1,50,'Детский'),(2,40,'Школьный'),(3,30,'Студенческий'),(4,0,'Взрослый'),(5,50,'Пенсионный');
/*!40000 ALTER TABLE `категории` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `посетитель`
--

DROP TABLE IF EXISTS `посетитель`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `посетитель` (
  `Код посетителя` int NOT NULL AUTO_INCREMENT,
  `Фамилия` varchar(255) NOT NULL,
  `Имя` varchar(255) NOT NULL,
  `Отчество` varchar(255) NOT NULL,
  `Дата рождения` date NOT NULL,
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Код посетителя`)
) ENGINE=InnoDB AUTO_INCREMENT=45462598 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `посетитель`
--

LOCK TABLES `посетитель` WRITE;
/*!40000 ALTER TABLE `посетитель` DISABLE KEYS */;
INSERT INTO `посетитель` VALUES (45462526,'Фролов','Андрей','Иванович','2001-07-13','gohufreilagrau-3818@yopmail.com'),(45462527,'Николаев','Даниил','Всеволодович','2001-02-09','xawugosune-1385@yopmail.com'),(45462528,'Снегирев','Макар','Иванович','1998-05-20','satrahuddusei-4458@yopmail.com'),(45462529,'Иванов','Иван','Ильич','1998-09-30','boippaxeufrepra-7093@yopmail.com'),(45462530,'Филиппова','Анна','Глебовна','1976-05-30','zapramaxesu-7741@yopmail.com'),(45462531,'Иванов','Михаил','Владимирович','1985-11-03','rouzecroummegre-3899@yopmail.com'),(45462532,'Власов','Дмитрий','Александрович','1998-08-16','ziyeuddocrabri-4748@yopmail.com'),(45462533,'Серова','Екатерина','Львовна','1984-10-23','ketameissoinnei-1951@yopmail.com'),(45462534,'Борисова','Ирина','Ивановна','1976-10-13','yipraubaponou-5849@yopmail.com'),(45462535,'Зайцев','Никита','Артёмович','1999-10-13','crapedocouca-3572@yopmail.com'),(45462536,'Медведев','Святослав','Евгеньевич','1985-07-12','ceigoixakaunni-9227@yopmail.com'),(45462537,'Коротков','Кирилл','Алексеевич','1976-05-25','yeimmeiwauzomo-7054@yopmail.com'),(45462538,'Калашникова','Арина','Максимовна','1999-08-12','poleifenevi-1560@yopmail.com'),(45462539,'Минина','Таисия','Кирилловна','1985-10-12','kauprezofautei-6607@yopmail.com'),(45462540,'Наумов','Серафим','Романович','1999-04-14','quaffaullelourei-1667@yopmail.com'),(45462541,'Воробьева','Василиса','Евгеньевна','1999-01-12','jsteele@rojas-robinson.net'),(45462542,'Калинин','Александр','Андреевич','1999-01-06','vhopkins@lewis-mullen.com'),(45462543,'Кузнецова','Милана','Владиславовна','1999-01-23','nlewis@yahoo.com'),(45462544,'Фирсов','Егор','Романович','1993-09-01','garciadavid@mckinney-mcbride.com'),(45462545,'Зимина','Агния','Александровна','1998-09-02','cbradley@castro.com'),(45462546,'Титов','Андрей','Глебович','1985-10-22','cuevascatherine@carlson.biz'),(45462547,'Орлов','Николай','Егорович','1985-07-26','thomasmoore@wilson-singh.net'),(45462548,'Кузнецова','Аиша','Михайловна','1998-10-03','jessica84@hotmail.com'),(45462549,'Куликов','Никита','Георгиевич','1999-04-22','jessicapark@hotmail.com'),(45462550,'Карпова','София','Егоровна','1993-09-30','ginaritter@schneider-buchanan.com'),(45462551,'Смирнова','Дарья','Макаровна','1976-03-21','stephen99@yahoo.com'),(45462552,'Абрамова','Александра','Мироновна','1999-03-25','lopezlisa@hotmail.com'),(45462553,'Наумов','Руслан','Михайлович','1999-10-10','lori17@hotmail.com'),(45462554,'Бочаров','Никита','Матвеевич','1997-06-28','campbellkevin@gardner.com'),(45462555,'Соловьев','Давид','Ильич','1984-03-05','morganhoward@clark.com'),(45462556,'Васильева','Валерия','Дмитриевна','1999-09-29','carsontamara@gmail.com'),(45462557,'Макарова','Василиса','Андреевна','1999-04-07','kevinpatel@gmail.com'),(45462558,'Алексеев','Матвей','Викторович','1998-08-01','sethbishop@yahoo.com'),(45462559,'Никитина','Полина','Александровна','1976-09-18','drollins@schultz-soto.net'),(45462560,'Окулова','Олеся','Алексеевна','1999-04-02','pblack@copeland-winters.org'),(45462561,'Захарова','Полина','Яновна','1976-04-20','johnathon.oberbrunner@yahoo.com'),(45462562,'Зайцев','Владимир','Давидович','1998-01-25','bradly29@gmail.com'),(45462563,'Иванов','Виталий','Даниилович','1976-08-10','stark.cristina@hilpert.biz'),(45462564,'Захаров','Матвей','Романович','1993-07-11','bruen.eleanore@yahoo.com'),(45462565,'Иванов','Степан','Степанович','1998-09-18','percival.halvorson@yahoo.com'),(45462566,'Ткачева','Милана','Тимуровна','1998-05-23','javonte71@kuhlman.biz'),(45462567,'Семенов','Даниил','Иванович','1976-01-03','vconnelly@kautzer.com'),(45462568,'Виноградов','Вячеслав','Дмитриевич','1976-07-11','anabelle07@schultz.info'),(45462569,'Соболева','Николь','Фёдоровна','1976-05-01','nitzsche.katlynn@yahoo.com'),(45462570,'Тихонова','Анна','Львовна','1985-03-22','corine16@von.com'),(45462571,'Кузнецова','Ульяна','Савельевна','1999-06-02','otha.wisozk@lubowitz.org'),(45462572,'Смирнова','Анна','Германовна','1997-07-17','may.kirlin@hotmail.com'),(45462573,'Черепанова','Анна','Давидовна','1985-11-05','bryana.kautzer@yahoo.com'),(45462574,'Григорьев','Максим','Кириллович','1999-05-25','deborah.christiansen@quigley.biz'),(45462575,'Голубев','Даниэль','Александрович','1999-06-13','connelly.makayla@yahoo.com'),(45462576,'Миронов','Юрий','Денисович','1985-01-25','tatum.collins@fay.org'),(45462577,'Терехов','Михаил','Андреевич','1976-07-05','itzel73@anderson.com'),(45462578,'Орлова','Алиса','Михайловна','1997-02-23','arjun39@hotmail.com'),(45462579,'Кулаков','Константин','Даниилович','1993-06-19','ohara.rebeka@yahoo.com'),(45462580,'Кудрявцев','Максим','Романович','1998-05-09','danika58@rath.com'),(45462581,'Соболева','Кира','Фёдоровна','1998-03-13','janae.bogan@gmail.com'),(45462582,'Коновалов','Арсений','Максимович','1985-02-17','vern91@yahoo.com'),(45462583,'Гусев','Михаил','Дмитриевич','1999-11-22','mariana.leannon@larkin.net'),(45462584,'Суханова','Варвара','Матвеевна','1993-09-12','vmoore@gmail.com'),(45462585,'Орлова','Ясмина','Васильевна','1984-06-23','damon.mcclure@mills.com'),(45462586,'Васильева','Ксения','Константиновна','1999-07-31','grady.reilly@block.com'),(45462587,'Борисова','Тамара','Данииловна','1993-05-28','boyd.koss@yahoo.com'),(45462588,'Дмитриев','Мирон','Ильич','1985-04-12','obartell@franecki.info'),(45462589,'Лебедева','Анна','Александровна','1985-03-29','reina75@ferry.net'),(45462590,'Пономарев','Артём','Маркович','1984-06-01','karson28@hotmail.com'),(45462591,'Борисова','Елена','Михайловна','1976-05-22','damaris61@okon.com'),(45462592,'Моисеев','Камиль','Максимович','1999-06-16','carroll.jerod@hotmail.com'),(45462593,'Герасимова','Дарья','Константиновна','1984-10-12','ron.treutel@quitzon.com'),(45462594,'Михайлова','Мария','Марковна','1976-12-01','olen79@yahoo.com'),(45462595,'Коршунов','Кирилл','Максимович','1985-05-21','pacocha.robbie@yahoo.com'),(45462596,'test','test','test','2000-01-01','test'),(45462597,'test','test','test','2000-01-01','test');
/*!40000 ALTER TABLE `посетитель` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `сотрудник`
--

DROP TABLE IF EXISTS `сотрудник`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `сотрудник` (
  `Код сотрудника` int NOT NULL,
  `Фамилия` varchar(255) NOT NULL,
  `Имя` varchar(255) NOT NULL,
  `Отчество` varchar(255) NOT NULL,
  `Должность` varchar(255) NOT NULL,
  `Дата рождения` date NOT NULL,
  `Паспортные данные` bigint NOT NULL,
  `Логин` varchar(255) NOT NULL,
  `Пароль` varchar(255) NOT NULL,
  `Фото` varchar(255) NOT NULL,
  PRIMARY KEY (`Код сотрудника`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `сотрудник`
--

LOCK TABLES `сотрудник` WRITE;
/*!40000 ALTER TABLE `сотрудник` DISABLE KEYS */;
INSERT INTO `сотрудник` VALUES (101,'Иванов','Иван','Иванович','Администратор','1999-01-23',1180176596,'Ivanov@namecomp.ru','2L6KZG','Иванов.jpeg'),(102,'Петров','Петр','Петрович','Экскурсовод','1993-09-01',2280223523,'petrov@namecomp.ru','uzWC67','Петров.jpeg'),(103,'Федоров','Федор','Федорович','Экскурсовод','1998-09-02',4560354155,'fedorov@namecomp.ru','8ntwUp','Федоров.jpeg'),(104,'Миронов','Вениамин','Куприянович','Экскурсовод','1985-10-22',9120554296,'mironov@namecomp.ru','YOyhfR','Миронов.jpeg'),(105,'Ширяев','Ермолай','Вениаминович','Страший экскурсовод','1985-07-26',2367558134,'shiryev@namecomp.ru','RSbvHv','Ширяев.jpeg');
/*!40000 ALTER TABLE `сотрудник` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `техника картины`
--

DROP TABLE IF EXISTS `техника картины`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `техника картины` (
  `Код техники` int NOT NULL,
  `Техника` varchar(255) NOT NULL,
  PRIMARY KEY (`Код техники`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `техника картины`
--

LOCK TABLES `техника картины` WRITE;
/*!40000 ALTER TABLE `техника картины` DISABLE KEYS */;
INSERT INTO `техника картины` VALUES (11,'Акварель'),(12,'Акварельная монотипия'),(13,'Алла прима'),(14,'Аффреско'),(15,'Альсекко'),(16,'Батик'),(17,'Валёр'),(18,'Гризайль'),(19,'Гуашь'),(20,'Дриппинг'),(21,'Ёга'),(22,'Живопись действия'),(23,'Изокефалия'),(24,'Иллюзионизм'),(25,'Импасто'),(26,'Имприматура'),(27,'Итальянская манера'),(28,'Карандаш Конте'),(29,'Карнация'),(30,'Клеевая живопись'),(31,'Лак'),(32,'Лессировка'),(33,'Масляная живопись'),(34,'Негативное пространство'),(35,'Ноктюрн'),(36,'Пальчиковые краски'),(37,'Пастель'),(38,'Пастозная техника живописи'),(39,'Пленэр'),(40,'Рисунок по-сырому'),(41,'Сепия'),(42,'Сухая кисть'),(43,'Сфумато'),(44,'Тарасикоми'),(45,'Телесный цвет'),(46,'Темпера'),(47,'Тренкадис'),(48,'Фламандская манера'),(49,'Фроттаж'),(50,'Энкаустика');
/*!40000 ALTER TABLE `техника картины` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `тип картины`
--

DROP TABLE IF EXISTS `тип картины`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `тип картины` (
  `Код типа` int NOT NULL,
  `Тип` varchar(255) NOT NULL,
  PRIMARY KEY (`Код типа`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `тип картины`
--

LOCK TABLES `тип картины` WRITE;
/*!40000 ALTER TABLE `тип картины` DISABLE KEYS */;
INSERT INTO `тип картины` VALUES (1,'Подленник'),(2,'Репродукция');
/*!40000 ALTER TABLE `тип картины` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `художник`
--

DROP TABLE IF EXISTS `художник`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `художник` (
  `Код художника` int NOT NULL AUTO_INCREMENT,
  `Фамилия` varchar(255) NOT NULL,
  `Имя` varchar(255) NOT NULL,
  `Отчество` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Дата рождения` date NOT NULL,
  `Место рождения` varchar(255) NOT NULL,
  `Жанр` varchar(255) NOT NULL,
  `Стиль` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Код художника`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `художник`
--

LOCK TABLES `художник` WRITE;
/*!40000 ALTER TABLE `художник` DISABLE KEYS */;
INSERT INTO `художник` VALUES (1,'Верещагин','Василий','Васильевич','1842-10-25','Российская федерация, Череповеч','Батальный','Реализм'),(2,'Ван Гог','Винсент','','1853-03-29','Нидерланды, Зюндерт','Пейзаж, натюрморт, портрет','Постимпрессионизм'),(3,'Мунк','Эдвард','','1863-12-11','Норвегия, Лётен','Живопись, графика','Модерн, Экспрессионизм'),(4,'Айвазовский','Иван','Константинович','1817-07-28','Российская федерация, Феодосия','Марина, батальный','Романтизм'),(5,'Дали','Сальвадор','','1904-05-10','Испания, Каталония, Фигерас','Натюрморт, жанровая живопись, портрет, пейзаж, аллегория и религиозное искусство','Сюрреализм, дадаизм, кубизм'),(6,'Да Винчи','Леонардо','','1452-04-14','Флорентийская республика, близ Винчи','Батальный','Сфумато'),(7,'Буонарроти','Микеланджело','','1564-03-05','Италия, Ареццо','Скульптура,живопись, архитектура, поэзия','Раннее барокко'),(8,'Уистлер','Джеймс','','1834-07-10','США, штат Массачусетс, Лоуэлл','Художник, живописец, портретист, гравёр, литограф','Тонализм, реализм');
/*!40000 ALTER TABLE `художник` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'artgallery'
--

--
-- Dumping routines for database 'artgallery'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-25  2:19:04
