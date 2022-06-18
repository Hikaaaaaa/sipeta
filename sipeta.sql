-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 18 Jun 2022 pada 01.04
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sipeta`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `distances`
--

CREATE TABLE `distances` (
  `id` int(10) UNSIGNED NOT NULL,
  `petshop_id` int(11) DEFAULT NULL,
  `firebase_user_id` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `distance` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Struktur dari tabel `petshops`
--

CREATE TABLE `petshops` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  `total_employee` int(11) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `grooming_price` varchar(255) DEFAULT NULL,
  `animal_care_price` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `gmaps_link` varchar(255) DEFAULT NULL,
  `open_hours` varchar(255) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `distance` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;

--
-- Dumping data untuk tabel `petshops`
--

INSERT INTO `petshops` (`id`, `name`, `capacity`, `total_employee`, `latitude`, `longitude`, `grooming_price`, `animal_care_price`, `address`, `gmaps_link`, `open_hours`, `image_url`, `distance`) VALUES
(2, 'Lestari pet shops', 15, 12, '-8.79062617195797', '115.163885904035', '55000', '50000', NULL, NULL, NULL, NULL, NULL),
(3, 'Babi', 15, 11, '-8.79062617195797', '115.187085134834', '50000', '50000', 'tukad batanghari', 'http://aangps01.com', '123123', 'http://aangps01.com', NULL);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `distances`
--
ALTER TABLE `distances`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Indeks untuk tabel `petshops`
--
ALTER TABLE `petshops`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `distances`
--
ALTER TABLE `distances`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `petshops`
--
ALTER TABLE `petshops`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
