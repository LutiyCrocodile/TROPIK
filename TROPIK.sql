-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 10, 2025 at 05:19 AM
-- Server version: 8.0.30
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `TROPIK`
--

-- --------------------------------------------------------

--
-- Table structure for table `cabinets`
--

CREATE TABLE `cabinets` (
  `id` int NOT NULL,
  `number` int NOT NULL,
  `busy` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cabinets`
--

INSERT INTO `cabinets` (`id`, `number`, `busy`) VALUES
(1, 123, 1),
(2, 333, 0);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int NOT NULL,
  `teacher_id` int DEFAULT NULL,
  `cabinet_id` int DEFAULT NULL,
  `resourse_id` int DEFAULT NULL,
  `date_of_order` date DEFAULT NULL,
  `status` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `teacher_id`, `cabinet_id`, `resourse_id`, `date_of_order`, `status`) VALUES
(2, 1, 2, 1, '2025-06-19', 1),
(3, 1, 2, 1, '2025-06-05', 0),
(4, 1, 2, 1, '2025-06-19', 0),
(10, 68, 2, 1, '2025-06-20', 1),
(11, 68, 2, 1, '2025-06-18', 1),
(12, 68, 2, 1, '2025-06-11', 1),
(13, 68, 2, 1, '2025-06-11', 1),
(14, 68, 2, 1, '2025-06-11', 1),
(15, 68, 2, 1, '2025-06-18', 1),
(16, 68, 2, 1, '2025-06-11', 1),
(17, 70, 2, 1, '2025-06-11', 0),
(18, 70, 2, 1, '2025-06-13', 1),
(19, 71, 2, 1, '2025-06-21', 0),
(20, 71, 2, 1, '2025-06-25', 0);

-- --------------------------------------------------------

--
-- Table structure for table `resuorses`
--

CREATE TABLE `resuorses` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `busy` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resuorses`
--

INSERT INTO `resuorses` (`id`, `name`, `busy`) VALUES
(1, 'pc', 0),
(2, 'nout', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `login` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `login`, `pass`) VALUES
(1, 'admin', 'admin'),
(21, 'alex', 'pass'),
(68, 'a', 'a'),
(69, 'asdasd', 'asdasd'),
(70, 'qqq', 'qqq'),
(71, 'Maksim Troshin', 'Maksim_280806');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cabinets`
--
ALTER TABLE `cabinets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `cabinet_id` (`cabinet_id`),
  ADD KEY `resourse_id` (`resourse_id`);

--
-- Indexes for table `resuorses`
--
ALTER TABLE `resuorses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`cabinet_id`) REFERENCES `cabinets` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`resourse_id`) REFERENCES `resuorses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
