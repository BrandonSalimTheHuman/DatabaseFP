-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:4306
-- Generation Time: Jan 15, 2024 at 04:09 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_fp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `admin_id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `salt` binary(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`admin_id`, `username`, `password`, `email`, `salt`) VALUES
(1, 'sumaya_buckley', '12fe33a4dc66c13f471198f3578ca864cd84d5c3f11f36b8f72aa14ecabe50d9', 'sumayabuckley@gmail.com', 0x6fc647d6c2e5a0cabdc96053021d46fc4e07572fe2decd7de0a5bd949f29),
(2, 'mya_mcneil', '164694826247bf0b967ea2841e0c0ae87c42a16a0baad9f4ab888d5d2d726b8f', 'myamcneil@gmail.com', 0x02d6156fb14669bd3041ee4ef87b8893cc8063a14be3a79c5ef61f8f5d05),
(3, 'sylvie_clements', '22aed6071cd26bbc7bcbbf57fa25eb974c9155296a44220b851bda71ecf75779', 'sylvieclements@gmail.com', 0x251e2494f54af680d4e6877997e95cc06ee85b26b722fcd2bc566968e310),
(4, 'gladys_simmons', '191e12ca03986103e548b3f2b6861d26cb7df36bf9956e955b6e02541e531654', 'gladyssimmons@gmail.com', 0x4157260f8c2ce4e1f2d2abde43f3b079f4a29d051f66186aad0aa108d65c),
(5, 'kamran_knowles', '313286d1a3fa11810d987c5f00413e0d943f2896e5474f4afc3d630a0bd1d74b', 'kamranknowles@gmail.com', 0xf52401151ac0e43b58ba67f1384714fa6440306a9744a4a170edc2ebc3e2),
(6, 'carrie_foster', '75177d2285ce8e32e23e4888b0f73c1f7107b0a84268ef134054fe97947cca2b', 'carriefoster@gmail.com', 0xa6b62ec65d1d5694ff84df770cf2a80e0a399f227e13a303191f9215af5b),
(7, 'tegan_ray', 'd75f6a9cda3ebde23bf67ae91df5a22808ccbfdb511da3830328cdd4890c9f64', 'teganray@gmail.com', 0x81dc0821b73eec9f1c232dd3eecd5030c9ed21b6e2d4a2463c116a09a99a),
(8, 'carys_hoover', '640b21e15d892451c148230de72db9d83ff14ec7192ed405918f9e53e469748a', 'caryshoover@gmail.com', 0x86b54de90214636ad270a2e48b1f4cfdeb09ce89161667b921b7b846cc29),
(9, 'tara_diaz', '1fe7d31302982a34a5d5bc8d5e23bddc9907204c6c01473b99e9d67924d92518', 'taradiaz@gmail.com', 0xa54e76f42cf3305b87aabd681cad5a06cd6a0e9589e47ee52f41b407d3c8),
(10, 'maja_odling', 'b2c3ff5699f434d120930452fbbd7b742df0ba34177612e9c8a574f6a8d95ecd', 'majaodling@gmail.com', 0x8660d6dcd6054ec5d8c55a27c50b0951d3f4806b5aa75fd3277f713240bf);

-- --------------------------------------------------------

--
-- Table structure for table `data_readings`
--

CREATE TABLE `data_readings` (
  `reading_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `parameter_id` int(11) NOT NULL,
  `value` float NOT NULL,
  `status` varchar(10) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_readings`
--

INSERT INTO `data_readings` (`reading_id`, `location_id`, `parameter_id`, `value`, `status`, `timestamp`) VALUES
(1, 1, 1, 21, 'safe', '2023-12-22 10:31:40'),
(2, 2, 1, 28, 'moderate', '2023-12-22 10:33:35'),
(3, 3, 1, 29, 'moderate', '2023-12-22 10:33:54'),
(4, 4, 1, 21, 'safe', '2023-12-22 10:34:19'),
(5, 5, 1, 24, 'safe', '2023-12-22 10:34:38'),
(6, 6, 1, 30, 'moderate', '2023-12-22 10:34:57'),
(7, 7, 1, 29, 'moderate', '2023-12-22 10:36:25'),
(8, 8, 1, 31, 'moderate', '2023-12-22 10:36:43'),
(9, 9, 1, 33, 'dangerous', '2024-01-13 19:35:10'),
(10, 10, 1, 27, 'moderate', '2023-12-22 10:37:22'),
(11, 11, 1, 27, 'moderate', '2023-12-22 10:42:18'),
(12, 12, 1, 31, 'moderate', '2023-12-22 10:42:39'),
(13, 13, 1, 34, 'dangerous', '2023-12-22 10:43:31'),
(14, 14, 1, 33, 'dangerous', '2023-12-22 10:43:47'),
(15, 15, 1, 25, 'safe', '2023-12-22 10:44:30'),
(16, 16, 1, 32, 'moderate', '2023-12-22 10:44:46'),
(17, 17, 1, 34, 'dangerous', '2023-12-22 10:45:06'),
(18, 18, 1, 27, 'moderate', '2023-12-22 10:45:22'),
(19, 19, 1, 36, 'dangerous', '2023-12-22 10:45:43'),
(20, 20, 1, 34, 'dangerous', '2023-12-22 10:46:09'),
(21, 21, 1, 37, 'dangerous', '2023-12-22 10:46:27'),
(22, 22, 1, 26, 'safe', '2023-12-22 10:46:46'),
(23, 23, 1, 26, 'safe', '2023-12-22 10:47:13'),
(24, 24, 1, 29, 'moderate', '2023-12-22 10:47:43'),
(25, 25, 1, 29, 'moderate', '2023-12-22 10:47:56'),
(26, 26, 1, 22, 'safe', '2023-12-22 10:48:17'),
(27, 27, 1, 28, 'moderate', '2023-12-22 10:48:41'),
(28, 28, 1, 30, 'moderate', '2023-12-22 10:48:57'),
(29, 29, 1, 28, 'moderate', '2023-12-22 10:49:13'),
(30, 30, 1, 32, 'moderate', '2023-12-22 10:49:29'),
(31, 31, 1, 30, 'moderate', '2023-12-22 10:49:46'),
(32, 32, 1, 29, 'moderate', '2023-12-22 10:50:02'),
(33, 33, 1, 29, 'moderate', '2023-12-22 10:50:19'),
(34, 34, 1, 33, 'dangerous', '2023-12-22 10:50:34'),
(35, 35, 1, 31, 'moderate', '2023-12-22 10:50:49'),
(36, 36, 1, 26, 'safe', '2023-12-22 10:51:32'),
(37, 37, 1, 24, 'safe', '2023-12-22 10:52:00'),
(38, 38, 1, 28, 'moderate', '2023-12-22 10:52:21'),
(39, 1, 2, 94, 'dangerous', '2023-12-22 17:36:27'),
(40, 1, 3, 1.67, 'safe', '2023-12-22 17:37:12'),
(41, 2, 2, 95, 'dangerous', '2023-12-22 17:37:48'),
(42, 2, 3, 2.78, 'safe', '2023-12-22 17:38:03'),
(43, 3, 2, 94, 'dangerous', '2023-12-22 17:39:36'),
(44, 3, 3, 1.11, 'safe', '2023-12-22 17:39:49'),
(46, 4, 3, 1.11, 'safe', '2023-12-22 17:43:44'),
(47, 5, 2, 99, 'dangerous', '2023-12-22 17:44:33'),
(48, 5, 3, 1.11, 'safe', '2023-12-22 17:44:43'),
(49, 6, 2, 90, 'dangerous', '2023-12-22 17:46:08'),
(50, 6, 3, 0.83, 'safe', '2023-12-22 17:46:26'),
(51, 7, 2, 88, 'dangerous', '2023-12-22 17:47:33'),
(52, 7, 3, 5.11, 'moderate', '2023-12-22 17:47:41'),
(53, 8, 2, 73, 'dangerous', '2023-12-22 17:49:34'),
(54, 8, 3, 3.05, 'safe', '2023-12-22 17:50:09'),
(55, 9, 2, 57, 'safe', '2023-12-22 17:51:44'),
(56, 9, 3, 1.11, 'safe', '2023-12-22 17:52:07'),
(57, 10, 2, 95, 'dangerous', '2023-12-22 17:52:58'),
(58, 10, 3, 1.11, 'safe', '2023-12-22 17:53:08'),
(59, 11, 2, 75, 'dangerous', '2023-12-22 17:53:51'),
(60, 11, 3, 5.56, 'moderate', '2023-12-22 17:54:18'),
(61, 12, 2, 58, 'safe', '2023-12-22 17:57:08'),
(62, 12, 3, 1.94, 'safe', '2023-12-22 17:57:27'),
(63, 13, 2, 77, 'dangerous', '2023-12-22 17:58:25'),
(64, 13, 3, 3.11, 'safe', '2023-12-22 17:58:42'),
(65, 14, 2, 63, 'moderate', '2023-12-22 17:59:44'),
(66, 14, 3, 2.22, 'safe', '2023-12-22 18:00:01'),
(67, 15, 2, 80, 'dangerous', '2023-12-22 18:00:52'),
(68, 15, 3, 5.56, 'moderate', '2023-12-22 18:01:08'),
(69, 16, 2, 71, 'dangerous', '2023-12-22 18:01:56'),
(70, 16, 3, 1.39, 'safe', '2023-12-22 18:02:16'),
(71, 17, 2, 44, 'safe', '2023-12-22 18:03:25'),
(72, 17, 3, 4.44, 'safe', '2023-12-22 18:03:57'),
(73, 18, 3, 2.22, 'safe', '2023-12-22 18:05:40'),
(74, 18, 2, 64, 'moderate', '2023-12-22 18:06:24'),
(75, 19, 2, 80, 'dangerous', '2023-12-22 18:07:13'),
(76, 19, 3, 5.83, 'moderate', '2023-12-22 18:07:28'),
(77, 20, 2, 67, 'moderate', '2023-12-22 18:08:53'),
(78, 20, 3, 5.56, 'moderate', '2023-12-22 18:09:00'),
(79, 21, 2, 60, 'safe', '2023-12-22 18:09:38'),
(80, 21, 3, 5.56, 'moderate', '2023-12-22 18:09:53'),
(81, 22, 2, 82, 'dangerous', '2023-12-22 18:10:36'),
(82, 22, 3, 5, 'moderate', '2023-12-22 18:10:55'),
(83, 23, 2, 95, 'dangerous', '2023-12-22 18:11:36'),
(84, 23, 3, 0.83, 'safe', '2023-12-22 18:11:54'),
(85, 24, 2, 67, 'moderate', '2023-12-22 18:12:22'),
(86, 24, 3, 5, 'moderate', '2023-12-22 18:12:42'),
(87, 25, 2, 75, 'dangerous', '2023-12-22 18:13:30'),
(88, 25, 3, 0.28, 'safe', '2023-12-22 18:13:36'),
(89, 26, 2, 82, 'dangerous', '2023-12-22 18:14:22'),
(90, 26, 3, 2.78, 'safe', '2023-12-22 18:14:29'),
(91, 27, 2, 94, 'dangerous', '2023-12-22 18:15:04'),
(92, 27, 3, 0.83, 'safe', '2023-12-22 18:15:11'),
(93, 28, 2, 100, 'dangerous', '2023-12-22 18:21:16'),
(94, 28, 3, 2.78, 'safe', '2023-12-22 18:21:22'),
(95, 29, 2, 69, 'moderate', '2023-12-22 18:22:13'),
(96, 29, 3, 5.56, 'moderate', '2023-12-22 18:22:26'),
(97, 30, 2, 56, 'safe', '2023-12-22 18:23:01'),
(98, 30, 3, 4.17, 'safe', '2023-12-22 18:23:20'),
(99, 31, 2, 70, 'moderate', '2023-12-22 18:23:50'),
(100, 31, 3, 5.56, 'moderate', '2023-12-22 18:23:59'),
(101, 32, 2, 64, 'moderate', '2023-12-22 18:24:26'),
(102, 32, 3, 3.06, 'safe', '2023-12-22 18:24:43'),
(103, 33, 2, 65, 'moderate', '2023-12-22 18:25:34'),
(104, 33, 3, 8.33, 'moderate', '2023-12-22 18:25:48'),
(105, 34, 2, 84, 'dangerous', '2023-12-22 18:26:12'),
(106, 34, 3, 0.27, 'safe', '2023-12-22 18:26:18'),
(107, 35, 2, 91, 'dangerous', '2023-12-22 18:27:21'),
(108, 35, 3, 1.11, 'safe', '2023-12-22 18:27:32'),
(109, 36, 2, 98, 'dangerous', '2023-12-22 18:28:05'),
(110, 36, 3, 0, 'safe', '2023-12-22 18:28:17'),
(111, 37, 2, 70, 'moderate', '2023-12-22 18:28:42'),
(112, 37, 3, 5.56, 'moderate', '2023-12-22 18:28:48'),
(113, 38, 2, 55, 'safe', '2023-12-22 18:29:47'),
(114, 38, 3, 5, 'moderate', '2023-12-22 18:29:57'),
(115, 1, 4, 1012.53, 'safe', '2023-12-23 13:14:34'),
(116, 2, 4, 1015.92, 'safe', '2023-12-23 13:22:58'),
(117, 3, 4, 1015.92, 'safe', '2023-12-23 13:23:33'),
(118, 4, 4, 1009.14, 'safe', '2023-12-23 13:25:04'),
(119, 5, 4, 1009.14, 'safe', '2023-12-23 13:25:42'),
(120, 6, 4, 1012.53, 'safe', '2023-12-23 13:26:19'),
(121, 7, 4, 1012.53, 'safe', '2023-12-23 13:26:49'),
(122, 8, 4, 1009.14, 'safe', '2023-12-23 13:27:19'),
(123, 9, 4, 1009.14, 'safe', '2023-12-23 13:27:45'),
(124, 10, 4, 1009.14, 'safe', '2023-12-23 13:28:01'),
(125, 11, 4, 1012.53, 'safe', '2023-12-23 13:29:13'),
(126, 12, 4, 1012.53, 'safe', '2023-12-23 13:29:43'),
(127, 13, 4, 1012.53, 'safe', '2023-12-23 13:31:39'),
(128, 14, 4, 1012.53, 'safe', '2023-12-23 13:33:03'),
(129, 15, 4, 1015.91, 'safe', '2023-12-23 13:33:33'),
(130, 16, 4, 1015.91, 'safe', '2023-12-23 13:37:01'),
(131, 17, 4, 1015.91, 'safe', '2023-12-23 13:37:16'),
(132, 18, 4, 1015.91, 'safe', '2023-12-23 13:37:38'),
(133, 19, 4, 1015.91, 'safe', '2023-12-23 13:38:00'),
(134, 20, 4, 1009.14, 'safe', '2023-12-23 13:38:18'),
(135, 21, 4, 1009.14, 'safe', '2023-12-23 13:38:55'),
(136, 22, 4, 1015.91, 'safe', '2023-12-23 13:39:23'),
(137, 23, 4, 1015.91, 'safe', '2023-12-23 13:39:42'),
(138, 24, 4, 1009.14, 'safe', '2023-12-23 13:39:59'),
(139, 25, 4, 1009.14, 'safe', '2023-12-23 13:40:16'),
(140, 26, 4, 1015.91, 'safe', '2023-12-23 13:40:35'),
(141, 27, 4, 1015.91, 'safe', '2023-12-23 13:40:49'),
(142, 28, 4, 1009.14, 'safe', '2023-12-23 13:41:05'),
(143, 29, 4, 1009.14, 'safe', '2023-12-23 13:41:31'),
(144, 30, 4, 1009.14, 'safe', '2023-12-23 13:41:51'),
(145, 31, 4, 1009.14, 'safe', '2023-12-23 13:42:05'),
(146, 32, 4, 1009.14, 'safe', '2023-12-23 13:42:23'),
(147, 33, 4, 1012.53, 'safe', '2023-12-23 13:42:55'),
(148, 34, 4, 1012.53, 'safe', '2023-12-23 13:43:16'),
(149, 35, 4, 1015.91, 'safe', '2023-12-23 13:43:42'),
(150, 36, 4, 1019.3, 'safe', '2023-12-23 13:44:07'),
(151, 37, 4, 1009.14, 'safe', '2023-12-23 13:44:25'),
(152, 38, 4, 1012.53, 'safe', '2023-12-23 13:44:50'),
(153, 1, 5, 2.286, 'safe', '2023-12-23 13:50:40'),
(154, 2, 5, 4.06, 'safe', '2023-12-23 13:51:09'),
(155, 3, 5, 0.762, 'safe', '2023-12-23 13:51:39'),
(156, 4, 5, 27.94, 'dangerous', '2023-12-23 13:52:13'),
(157, 5, 5, 3.048, 'safe', '2023-12-23 13:52:54'),
(158, 6, 5, 6.096, 'safe', '2023-12-23 13:53:18'),
(159, 7, 5, 5, 'safe', '2024-01-11 15:05:40'),
(160, 8, 5, 0, 'safe', '2023-12-23 13:54:15'),
(161, 9, 5, 14.22, 'moderate', '2024-01-11 16:56:39'),
(162, 10, 5, 4.064, 'safe', '2023-12-23 13:55:06'),
(163, 11, 5, 1.016, 'safe', '2023-12-23 13:55:28'),
(164, 12, 5, 0, 'safe', '2023-12-23 13:55:51'),
(165, 13, 5, 12.7, 'moderate', '2023-12-23 13:56:13'),
(166, 14, 5, 0.254, 'safe', '2023-12-23 13:56:40'),
(167, 15, 5, 0.762, 'safe', '2023-12-23 13:57:04'),
(168, 16, 5, 8.636, 'safe', '2023-12-23 13:57:39'),
(169, 17, 5, 0.508, 'safe', '2023-12-23 13:58:06'),
(170, 18, 5, 0, 'safe', '2023-12-23 13:58:33'),
(171, 19, 5, 0.508, 'safe', '2023-12-23 13:58:59'),
(172, 20, 5, 0, 'safe', '2023-12-23 13:59:26'),
(173, 21, 5, 51.308, 'dangerous', '2023-12-23 13:59:55'),
(174, 22, 5, 0, 'safe', '2023-12-23 14:00:21'),
(175, 23, 5, 0, 'safe', '2023-12-23 14:00:45'),
(176, 24, 5, 0.508, 'safe', '2023-12-23 14:00:55'),
(177, 25, 5, 0, 'safe', '2023-12-23 14:01:15'),
(178, 26, 5, 2.032, 'safe', '2023-12-23 14:01:50'),
(179, 27, 5, 3.048, 'safe', '2023-12-23 14:02:16'),
(180, 28, 5, 0, 'safe', '2023-12-23 14:02:39'),
(181, 29, 5, 1.778, 'safe', '2023-12-23 14:03:03'),
(182, 30, 5, 3.048, 'safe', '2023-12-23 14:03:23'),
(183, 31, 5, 0, 'safe', '2023-12-23 14:03:39'),
(184, 32, 5, 5.842, 'safe', '2023-12-23 14:03:57'),
(185, 33, 5, 5.08, 'safe', '2023-12-23 14:04:17'),
(186, 34, 5, 3.81, 'safe', '2023-12-23 14:04:45'),
(187, 35, 5, 7.112, 'safe', '2023-12-23 14:05:14'),
(188, 36, 5, 10.16, 'moderate', '2023-12-23 14:05:40'),
(189, 37, 5, 0, 'safe', '2023-12-23 14:05:57'),
(190, 38, 5, 0, 'safe', '2023-12-23 14:06:16'),
(191, 1, 6, 10, 'dangerous', '2023-12-23 15:45:22'),
(192, 2, 6, 6, 'moderate', '2023-12-23 15:46:36'),
(193, 3, 6, 7, 'dangerous', '2023-12-23 15:46:59'),
(194, 4, 6, 12, 'dangerous', '2023-12-23 15:51:47'),
(195, 5, 6, 12, 'dangerous', '2023-12-23 15:52:30'),
(196, 6, 6, 6, 'moderate', '2023-12-23 15:53:15'),
(197, 7, 6, 4, 'moderate', '2023-12-23 15:56:12'),
(198, 8, 6, 7, 'dangerous', '2023-12-23 15:57:05'),
(199, 9, 6, 5, 'moderate', '2024-01-11 15:21:12'),
(200, 10, 6, 6, 'moderate', '2023-12-23 15:58:32'),
(201, 11, 6, 8, 'dangerous', '2023-12-23 16:00:26'),
(202, 12, 6, 9, 'dangerous', '2023-12-23 16:00:51'),
(203, 13, 6, 6, 'moderate', '2023-12-23 16:01:10'),
(204, 14, 6, 6, 'moderate', '2023-12-23 16:01:32'),
(205, 15, 6, 9, 'dangerous', '2023-12-23 16:02:03'),
(206, 16, 6, 8, 'dangerous', '2023-12-23 16:02:24'),
(207, 17, 6, 11, 'dangerous', '2023-12-23 16:02:46'),
(208, 18, 6, 5, 'moderate', '2023-12-23 16:03:18'),
(209, 19, 6, 12, 'dangerous', '2023-12-23 16:05:23'),
(210, 20, 6, 11, 'dangerous', '2023-12-23 16:07:32'),
(211, 21, 6, 6, 'moderate', '2024-01-14 15:40:33'),
(212, 22, 6, 8, 'dangerous', '2023-12-23 16:12:23'),
(213, 23, 6, 12, 'dangerous', '2023-12-23 16:13:44'),
(214, 24, 6, 6, 'moderate', '2023-12-23 16:14:12'),
(215, 25, 6, 9, 'dangerous', '2023-12-23 16:14:32'),
(216, 26, 6, 5, 'moderate', '2023-12-23 16:14:57'),
(217, 27, 6, 4, 'moderate', '2023-12-23 16:15:42'),
(218, 28, 6, 6, 'moderate', '2023-12-23 16:16:11'),
(219, 29, 6, 6, 'moderate', '2023-12-23 16:16:43'),
(220, 30, 6, 12, 'dangerous', '2023-12-23 16:17:13'),
(221, 31, 6, 7, 'dangerous', '2023-12-23 16:17:52'),
(222, 32, 6, 11, 'dangerous', '2023-12-23 16:18:07'),
(223, 33, 6, 6, 'moderate', '2023-12-23 16:18:28'),
(224, 34, 6, 9, 'dangerous', '2023-12-23 16:18:59'),
(225, 35, 6, 3, 'moderate', '2023-12-23 16:19:41'),
(226, 36, 6, 7, 'dangerous', '2023-12-23 16:21:14'),
(227, 37, 6, 5, 'moderate', '2023-12-23 16:21:39'),
(228, 38, 6, 6, 'moderate', '2023-12-23 16:22:12'),
(229, 1, 7, 47, 'safe', '2023-12-23 16:28:42'),
(230, 2, 7, 67, 'moderate', '2023-12-23 16:29:21'),
(231, 3, 7, 99, 'moderate', '2023-12-23 16:29:53'),
(232, 4, 7, 48, 'safe', '2023-12-23 16:30:17'),
(233, 5, 7, 55, 'moderate', '2023-12-23 16:30:45'),
(234, 6, 7, 70, 'moderate', '2023-12-23 16:31:10'),
(235, 7, 7, 5, 'safe', '2024-01-11 15:05:32'),
(236, 8, 7, 57, 'moderate', '2023-12-23 16:31:49'),
(237, 9, 7, 105, 'dangerous', '2024-01-14 16:11:39'),
(238, 10, 7, 62, 'moderate', '2023-12-23 16:32:34'),
(239, 11, 7, 157, 'dangerous', '2023-12-23 16:32:56'),
(240, 12, 7, 47, 'safe', '2023-12-23 16:33:14'),
(241, 13, 7, 79, 'moderate', '2023-12-23 16:33:32'),
(242, 14, 7, 72, 'moderate', '2023-12-23 16:33:50'),
(243, 15, 7, 34, 'safe', '2023-12-23 16:34:13'),
(244, 16, 7, 184, 'dangerous', '2023-12-23 16:34:40'),
(245, 17, 7, 137, 'dangerous', '2023-12-23 16:35:47'),
(246, 18, 7, 181, 'dangerous', '2023-12-23 16:36:18'),
(247, 19, 7, 110, 'dangerous', '2023-12-23 16:36:38'),
(248, 20, 7, 56, 'moderate', '2023-12-23 16:37:04'),
(249, 21, 7, 65, 'moderate', '2023-12-23 16:37:25'),
(250, 22, 7, 142, 'dangerous', '2023-12-23 16:37:46'),
(251, 23, 7, 37, 'safe', '2023-12-23 16:38:03'),
(252, 24, 7, 59, 'moderate', '2023-12-23 16:38:33'),
(253, 25, 7, 59, 'moderate', '2023-12-23 16:38:47'),
(254, 26, 7, 18, 'safe', '2023-12-23 16:39:03'),
(255, 27, 7, 21, 'safe', '2023-12-23 16:39:41'),
(256, 28, 7, 46, 'safe', '2023-12-23 16:40:04'),
(257, 29, 7, 54, 'moderate', '2023-12-23 16:40:22'),
(258, 30, 7, 71, 'moderate', '2023-12-23 16:40:46'),
(259, 31, 7, 7, 'safe', '2023-12-23 16:41:08'),
(260, 32, 7, 37, 'safe', '2023-12-23 16:41:30'),
(261, 33, 7, 8, 'safe', '2023-12-23 16:41:52'),
(262, 34, 7, 71, 'moderate', '2023-12-23 16:42:19'),
(263, 35, 7, 71, 'moderate', '2023-12-23 16:42:34'),
(264, 36, 7, 46, 'safe', '2023-12-23 16:42:54'),
(265, 37, 7, 35, 'safe', '2023-12-23 16:43:16'),
(266, 38, 7, 8, 'safe', '2023-12-23 16:43:48');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `event_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `event_type` varchar(30) NOT NULL,
  `event_status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`event_id`, `location_id`, `event_type`, `event_status`) VALUES
(3, 14, 'monke spinnnnnnn', 'dangerous'),
(4, 34, 'separatism', 'moderate'),
(10, 9, 'Canon event', 'dangerous');

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `location_id` int(11) NOT NULL,
  `location_name` varchar(50) NOT NULL,
  `overall_status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`location_id`, `location_name`, `overall_status`) VALUES
(1, 'Nanggroe Aceh Darussalam', 'moderate'),
(2, 'Sumatera Utara', 'moderate'),
(3, 'Sumatera Selatan', 'moderate'),
(4, 'Sumatera Barat', 'safe'),
(5, 'Bengkulu', 'moderate'),
(6, 'Riau', 'moderate'),
(7, 'Kepulauan Riau', 'moderate'),
(8, 'Jambi', 'moderate'),
(9, 'Lampung', 'moderate'),
(10, 'Bangka Belitung', 'moderate'),
(11, 'Kalimantan Barat', 'dangerous'),
(12, 'Kalimantan Timur', 'moderate'),
(13, 'Kalimantan Selatan', 'dangerous'),
(14, 'Kalimantan Tengah', 'moderate'),
(15, 'Kalimantan Utara', 'moderate'),
(16, 'Banten', 'dangerous'),
(17, 'DKI Jakarta', 'moderate'),
(18, 'Jawa Barat', 'moderate'),
(19, 'Jawa Tengah', 'dangerous'),
(20, 'Daerah Istimewa Yogyakarta', 'dangerous'),
(21, 'Jawa Timur', 'moderate'),
(22, 'Bali', 'moderate'),
(23, 'Nusa Tenggara Timur', 'moderate'),
(24, 'Nusa Tenggara Barat', 'moderate'),
(25, 'Gorontalo', 'moderate'),
(26, 'Sulawesi Barat', 'safe'),
(27, 'Sulawesi Tengah', 'moderate'),
(28, 'Sulawesi Utara', 'moderate'),
(29, 'Sulawesi Tenggara', 'moderate'),
(30, 'Sulawesi Selatan', 'moderate'),
(31, 'Maluku Utara', 'moderate'),
(32, 'Maluku', 'moderate'),
(33, 'Papua Barat', 'moderate'),
(34, 'Papua', 'dangerous'),
(35, 'Papua Tengah', 'moderate'),
(36, 'Papua Pegunungan', 'moderate'),
(37, 'Papua Selatan', 'safe'),
(38, 'Papua Barat Daya', 'safe');

-- --------------------------------------------------------

--
-- Table structure for table `parameters`
--

CREATE TABLE `parameters` (
  `parameter_id` int(11) NOT NULL,
  `parameter_name` varchar(30) NOT NULL,
  `unit_of_measurement` varchar(20) DEFAULT NULL,
  `description` varchar(150) NOT NULL,
  `safe_value_min` float NOT NULL,
  `safe_value_max` float NOT NULL,
  `moderate_value_min` float NOT NULL,
  `moderate_value_max` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parameters`
--

INSERT INTO `parameters` (`parameter_id`, `parameter_name`, `unit_of_measurement`, `description`, `safe_value_min`, `safe_value_max`, `moderate_value_min`, `moderate_value_max`) VALUES
(1, 'Temperature', 'C', 'Measure of the average kinetic energy of particles in a substance.', 17, 26, 9, 32),
(2, 'Humidity', '%', 'Measure of the amount of water vapor in the air.', 40, 60, 30, 70),
(3, 'Wind speed', 'm/s', 'Measure of the speed of the wind above the ground.', 0, 5, 5, 10),
(4, 'Air pressure', 'hPa', 'Measure of the force exerted by air molecules on a surface.', 980, 1020, 950, 1050),
(5, 'Precipitation', 'mm', 'Measure of the amount of water (liquid or solid) falling from the sky.', 0, 10, 10, 20),
(6, 'UV index', NULL, 'Measure of the intensity of ultraviolet (UV) radiation from the sun.', 0, 3, 3, 7),
(7, 'Air quality index', NULL, 'Measure of air quality based on various pollutants.', 0, 50, 50, 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `data_readings`
--
ALTER TABLE `data_readings`
  ADD PRIMARY KEY (`reading_id`),
  ADD KEY `location_id` (`location_id`),
  ADD KEY `parameter_id` (`parameter_id`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`event_id`),
  ADD KEY `fk_location_id` (`location_id`);

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`location_id`);

--
-- Indexes for table `parameters`
--
ALTER TABLE `parameters`
  ADD PRIMARY KEY (`parameter_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `location_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `parameters`
--
ALTER TABLE `parameters`
  MODIFY `parameter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data_readings`
--
ALTER TABLE `data_readings`
  ADD CONSTRAINT `location_id` FOREIGN KEY (`location_id`) REFERENCES `locations` (`location_id`),
  ADD CONSTRAINT `parameter_id` FOREIGN KEY (`parameter_id`) REFERENCES `parameters` (`parameter_id`);

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `fk_location_id` FOREIGN KEY (`location_id`) REFERENCES `locations` (`location_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
