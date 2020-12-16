-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: Library_db
-- ------------------------------------------------------
-- Server version	8.0.22-0ubuntu0.20.04.3

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
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` float DEFAULT NULL,
  `importedDate` date NOT NULL,
  `bookBorrowSlip_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bookBorrowSlip_id` (`bookBorrowSlip_id`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`bookBorrowSlip_id`) REFERENCES `bookBorrowSlip` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'How To Win Friends And Influence People','How-To-Win-Friends-And-Influence-People',1.99,'2020-12-14',NULL),(2,'How To Stop Worrying And Start Living','How-To-Stop-Worrying-And-Start-Living',1.99,'2020-12-14',NULL),(3,'The Alchemist','The-Alchemist',9.95,'2020-12-14',NULL),(4,'Harry Potter 1','Harry-Potter-1',9.99,'2020-12-14',NULL),(5,'Harry Potter 2','Harry-Potter-2',8.98,'2020-12-14',NULL),(6,'Harry Potter 3','Harry-Potter-3',7.97,'2020-12-14',NULL),(7,'Harry Potter 4','Harry-Potter-4',6.96,'2020-12-14',NULL),(8,'Harry Potter 5','Harry-Potter-5',5.95,'2020-12-14',NULL),(9,'Harry Potter 6','Harry-Potter-6',4.94,'2020-12-14',NULL),(10,'Harry Potter 7','Harry-Potter-7',3.93,'2020-12-14',NULL),(11,'Soul Seek 1','Soul-Seek-1',1.99,'2020-12-14',NULL),(12,'Soul Seek 2','Soul-Seek-2',1.99,'2020-12-14',NULL),(13,'Soul Seek 3','Soul-Seek-3',6.77,'2020-12-14',NULL),(14,'Soul Seek 4','Soul-Seek-4',3.45,'2020-12-14',NULL),(15,'Soul Seek 5','Soul-Seek-5',8.76,'2020-12-14',NULL),(16,'Soul Seek 6','Soul-Seek-6',9.01,'2020-12-14',NULL),(17,'Soul Seek 7','Soul-Seek-7',6.04,'2020-12-14',NULL),(18,'Soul Seek 8','Soul-Seek-8',5.34,'2020-12-14',NULL),(19,'Soul Seek 9','Soul-Seek-9',7.77,'2020-12-14',NULL),(20,'Soul Seek 10','Soul-Seek-10',2.99,'2020-12-14',NULL);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-16 22:29:28
