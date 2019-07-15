-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 15, 2019 at 08:30 PM
-- Server version: 5.7.17-log
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thanwyascrape`
--

-- --------------------------------------------------------

--
-- Table structure for table `degrees`
--

CREATE TABLE `degrees` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `rakamglos` varchar(255) NOT NULL,
  `school` varchar(255) NOT NULL,
  `edara` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `kam_mada` varchar(255) NOT NULL,
  `sho3ba` varchar(255) NOT NULL,
  `Arabic` varchar(255) NOT NULL,
  `English` varchar(255) NOT NULL,
  `SecLanguage` varchar(255) NOT NULL,
  `Math2` varchar(255) NOT NULL,
  `History` varchar(255) NOT NULL,
  `Geo` varchar(255) NOT NULL,
  `Falsfa` varchar(255) NOT NULL,
  `Nafs` varchar(255) NOT NULL,
  `Kemya` varchar(255) NOT NULL,
  `Ahyaa` varchar(255) NOT NULL,
  `Geologya` varchar(255) NOT NULL,
  `MathTabe2` varchar(255) NOT NULL,
  `Physics` varchar(255) NOT NULL,
  `Total` varchar(255) NOT NULL,
  `Nesba` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `degrees`
--
ALTER TABLE `degrees`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `rakamglos` (`rakamglos`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `degrees`
--
ALTER TABLE `degrees`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=688;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
