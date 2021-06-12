-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2021 at 06:01 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `daycare`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_detailtransaksi`
--

CREATE TABLE `tb_detailtransaksi` (
  `idDetailTransaksi` bigint(20) NOT NULL,
  `idTransaksi` bigint(20) DEFAULT NULL,
  `idKategori` bigint(20) DEFAULT NULL,
  `namaPeliharaan` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_detailtransaksi`
--

INSERT INTO `tb_detailtransaksi` (`idDetailTransaksi`, `idTransaksi`, `idKategori`, `namaPeliharaan`) VALUES
(1, 1, 2, 'Poci'),
(2, 2, 3, 'Ciko');

-- --------------------------------------------------------

--
-- Table structure for table `tb_kategorihewan`
--

CREATE TABLE `tb_kategorihewan` (
  `idKategori` bigint(20) NOT NULL,
  `namaKategori` varchar(255) DEFAULT NULL,
  `biaya` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_kategorihewan`
--

INSERT INTO `tb_kategorihewan` (`idKategori`, `namaKategori`, `biaya`) VALUES
(1, 'Kucing', 50000),
(2, 'Anjing', 75000),
(3, 'Burung Beo', 30000),
(4, 'Musang', 40000);

-- --------------------------------------------------------

--
-- Table structure for table `tb_pelanggan`
--

CREATE TABLE `tb_pelanggan` (
  `usernamePelanggan` varchar(15) NOT NULL,
  `nama` varchar(40) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_pelanggan`
--

INSERT INTO `tb_pelanggan` (`usernamePelanggan`, `nama`, `password`) VALUES
('bila1212', 'Aura Salsabila', 'aura'),
('rarasdw', 'Raras Dwistian', 'raras');

-- --------------------------------------------------------

--
-- Table structure for table `tb_petugas`
--

CREATE TABLE `tb_petugas` (
  `usernamePetugas` varchar(15) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_petugas`
--

INSERT INTO `tb_petugas` (`usernamePetugas`, `nama`, `password`) VALUES
('jeje1702', 'Jessica Maya', '1702jeje');

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi`
--

CREATE TABLE `tb_transaksi` (
  `idTransaksi` bigint(20) NOT NULL,
  `waktuTransaksi` datetime NOT NULL,
  `waktuPengembalian` datetime DEFAULT NULL,
  `usernamePetugas` varchar(15) DEFAULT NULL,
  `usernamePelanggan` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_transaksi`
--

INSERT INTO `tb_transaksi` (`idTransaksi`, `waktuTransaksi`, `waktuPengembalian`, `usernamePetugas`, `usernamePelanggan`) VALUES
(1, '2021-06-07 11:00:47', '2021-06-07 11:01:30', 'jeje1702', 'rarasdw'),
(2, '2021-06-07 11:01:06', NULL, 'jeje1702', 'bila1212');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_detailtransaksi`
--
ALTER TABLE `tb_detailtransaksi`
  ADD PRIMARY KEY (`idDetailTransaksi`),
  ADD KEY `idTransaksi` (`idTransaksi`),
  ADD KEY `idKategori` (`idKategori`);

--
-- Indexes for table `tb_kategorihewan`
--
ALTER TABLE `tb_kategorihewan`
  ADD PRIMARY KEY (`idKategori`);

--
-- Indexes for table `tb_pelanggan`
--
ALTER TABLE `tb_pelanggan`
  ADD PRIMARY KEY (`usernamePelanggan`);

--
-- Indexes for table `tb_petugas`
--
ALTER TABLE `tb_petugas`
  ADD PRIMARY KEY (`usernamePetugas`);

--
-- Indexes for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD PRIMARY KEY (`idTransaksi`),
  ADD KEY `usernamePetugas` (`usernamePetugas`),
  ADD KEY `usernamePelanggan` (`usernamePelanggan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_detailtransaksi`
--
ALTER TABLE `tb_detailtransaksi`
  MODIFY `idDetailTransaksi` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_kategorihewan`
--
ALTER TABLE `tb_kategorihewan`
  MODIFY `idKategori` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  MODIFY `idTransaksi` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_detailtransaksi`
--
ALTER TABLE `tb_detailtransaksi`
  ADD CONSTRAINT `tb_detailtransaksi_ibfk_1` FOREIGN KEY (`idTransaksi`) REFERENCES `tb_transaksi` (`idTransaksi`),
  ADD CONSTRAINT `tb_detailtransaksi_ibfk_2` FOREIGN KEY (`idKategori`) REFERENCES `tb_kategorihewan` (`idKategori`);

--
-- Constraints for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD CONSTRAINT `tb_transaksi_ibfk_1` FOREIGN KEY (`usernamePetugas`) REFERENCES `tb_petugas` (`usernamePetugas`),
  ADD CONSTRAINT `tb_transaksi_ibfk_2` FOREIGN KEY (`usernamePelanggan`) REFERENCES `tb_pelanggan` (`usernamePelanggan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
