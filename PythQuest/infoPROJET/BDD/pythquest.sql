-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 24 mars 2025 à 09:35
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pythquest`
--

-- --------------------------------------------------------

--
-- Structure de la table `arme`
--

CREATE TABLE `arme` (
  `id` int(11) NOT NULL,
  `combattant_id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `valeurOr` int(11) DEFAULT NULL,
  `degat` int(11) DEFAULT NULL,
  `image` blob NOT NULL COMMENT 'Image PIL en Binaire',
  `inventaire_combattant_id` int(11) DEFAULT NULL,
  `inventaire_forgeron_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `combattant`
--

CREATE TABLE `combattant` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `motDePasse` varchar(255) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `piece` int(11) DEFAULT NULL,
  `vie` int(11) DEFAULT NULL,
  `maxVie` int(11) DEFAULT NULL,
  `niveau` int(11) DEFAULT NULL,
  `experience` int(11) DEFAULT NULL,
  `inventairePotions` int(11) DEFAULT NULL,
  `armeEquipee_id` int(11) DEFAULT NULL,
  `queteActuelle_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `donjon`
--

CREATE TABLE `donjon` (
  `id` int(11) NOT NULL,
  `combattant_id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `difficulte` int(11) DEFAULT NULL,
  `statut` varchar(255) DEFAULT NULL,
  `niveau` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `forgeron`
--

CREATE TABLE `forgeron` (
  `id` int(11) NOT NULL,
  `combattant_id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `medecin`
--

CREATE TABLE `medecin` (
  `id` int(11) NOT NULL,
  `combattant_id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prixPotion` int(11) DEFAULT NULL,
  `stockPotions` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `monstre`
--

CREATE TABLE `monstre` (
  `id` int(11) NOT NULL,
  `combattant_id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `piece` int(11) DEFAULT NULL,
  `vie` int(11) DEFAULT NULL,
  `niveau` int(11) DEFAULT NULL,
  `armePossedee_id` int(11) DEFAULT NULL,
  `donjon_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `quete`
--

CREATE TABLE `quete` (
  `id` int(11) NOT NULL,
  `combattant_id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `recompenseOr` int(11) DEFAULT NULL,
  `difficulte` int(11) DEFAULT NULL,
  `statut` varchar(255) DEFAULT NULL,
  `niveau` int(11) DEFAULT NULL,
  `monstreCible_id` int(11) DEFAULT NULL,
  `donjonAssocie_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `arme`
--
ALTER TABLE `arme`
  ADD PRIMARY KEY (`id`,`combattant_id`),
  ADD KEY `combattant_id` (`combattant_id`),
  ADD KEY `inventaire_combattant_id` (`inventaire_combattant_id`),
  ADD KEY `inventaire_forgeron_id` (`inventaire_forgeron_id`);

--
-- Index pour la table `combattant`
--
ALTER TABLE `combattant`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `email` (`email`);

--
-- Index pour la table `donjon`
--
ALTER TABLE `donjon`
  ADD PRIMARY KEY (`id`,`combattant_id`),
  ADD KEY `combattant_id` (`combattant_id`);

--
-- Index pour la table `forgeron`
--
ALTER TABLE `forgeron`
  ADD PRIMARY KEY (`id`,`combattant_id`),
  ADD KEY `combattant_id` (`combattant_id`);

--
-- Index pour la table `medecin`
--
ALTER TABLE `medecin`
  ADD PRIMARY KEY (`id`,`combattant_id`),
  ADD KEY `combattant_id` (`combattant_id`);

--
-- Index pour la table `monstre`
--
ALTER TABLE `monstre`
  ADD PRIMARY KEY (`id`,`combattant_id`),
  ADD KEY `combattant_id` (`combattant_id`),
  ADD KEY `armePossedee_id` (`armePossedee_id`),
  ADD KEY `donjon_id` (`donjon_id`);

--
-- Index pour la table `quete`
--
ALTER TABLE `quete`
  ADD PRIMARY KEY (`id`,`combattant_id`),
  ADD KEY `combattant_id` (`combattant_id`),
  ADD KEY `monstreCible_id` (`monstreCible_id`),
  ADD KEY `donjonAssocie_id` (`donjonAssocie_id`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `arme`
--
ALTER TABLE `arme`
  ADD CONSTRAINT `arme_ibfk_1` FOREIGN KEY (`combattant_id`) REFERENCES `combattant` (`id`),
  ADD CONSTRAINT `arme_ibfk_2` FOREIGN KEY (`inventaire_combattant_id`) REFERENCES `combattant` (`id`),
  ADD CONSTRAINT `arme_ibfk_3` FOREIGN KEY (`inventaire_forgeron_id`) REFERENCES `combattant` (`id`);

--
-- Contraintes pour la table `donjon`
--
ALTER TABLE `donjon`
  ADD CONSTRAINT `donjon_ibfk_1` FOREIGN KEY (`combattant_id`) REFERENCES `combattant` (`id`);

--
-- Contraintes pour la table `forgeron`
--
ALTER TABLE `forgeron`
  ADD CONSTRAINT `forgeron_ibfk_1` FOREIGN KEY (`combattant_id`) REFERENCES `combattant` (`id`);

--
-- Contraintes pour la table `medecin`
--
ALTER TABLE `medecin`
  ADD CONSTRAINT `medecin_ibfk_1` FOREIGN KEY (`combattant_id`) REFERENCES `combattant` (`id`);

--
-- Contraintes pour la table `monstre`
--
ALTER TABLE `monstre`
  ADD CONSTRAINT `monstre_ibfk_1` FOREIGN KEY (`combattant_id`) REFERENCES `combattant` (`id`),
  ADD CONSTRAINT `monstre_ibfk_2` FOREIGN KEY (`armePossedee_id`) REFERENCES `arme` (`id`),
  ADD CONSTRAINT `monstre_ibfk_3` FOREIGN KEY (`donjon_id`) REFERENCES `donjon` (`id`);

--
-- Contraintes pour la table `quete`
--
ALTER TABLE `quete`
  ADD CONSTRAINT `quete_ibfk_1` FOREIGN KEY (`combattant_id`) REFERENCES `combattant` (`id`),
  ADD CONSTRAINT `quete_ibfk_2` FOREIGN KEY (`monstreCible_id`) REFERENCES `monstre` (`id`),
  ADD CONSTRAINT `quete_ibfk_3` FOREIGN KEY (`donjonAssocie_id`) REFERENCES `donjon` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
