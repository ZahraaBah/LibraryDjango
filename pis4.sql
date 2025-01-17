

DROP TABLE IF EXISTS `commune`;
CREATE TABLE IF NOT EXISTS `commune` (
  `ID_commune` int NOT NULL,
  `Nom_commune` varchar(255) DEFAULT NULL,
  `ID_maghataa` int DEFAULT NULL,
  PRIMARY KEY (`ID_commune`),
  KEY `ID_maghataa` (`ID_maghataa`)
) 

--
-- Déchargement des données de la table `commune`
--

INSERT INTO `commune` (`ID_commune`, `Nom_commune`, `ID_maghataa`) VALUES
(1, 'mal', 53),
(2, 'meghta-lehjar', 53);

--
-- Structure de la table `maghataa`
--

DROP TABLE IF EXISTS `maghataa`;
CREATE TABLE IF NOT EXISTS `maghataa` (
  `ID_maghataa` int NOT NULL,
  `Nom_maghataa` varchar(255) DEFAULT NULL,
  `ID_wilaya` int DEFAULT NULL,
  PRIMARY KEY (`ID_maghataa`),
  KEY `ID_wilaya` (`ID_wilaya`)
) 

--
-- Déchargement des données de la table `maghataa`
--

INSERT INTO `maghataa` (`ID_maghataa`, `Nom_maghataa`, `ID_wilaya`) VALUES
(1, 'Akebou', 1),
(2, 'Amourj', 1),
(3, 'Bassiknou', 1),
(4, 'Tamchekett', 1),
(5, 'Tintane', 1),
(6, 'Aoujeft', 2),
(7, 'Kobeni', 2),
(8, 'Toujeil', 2),
(9, 'Mabrouka', 3),
(10, 'Moudjéria', 3),
(11, 'Ghabou', 3),
(12, 'Ould Yengé', 3),
(13, 'Kankossa', 4),
(14, 'Kaédi', 4),
(15, 'Maghama', 4),
(16, 'Monguel', 4),
(17, 'Aleg', 5),
(18, 'Bababé', 5),
(19, 'Boghé', 5),
(20, 'Mbagne', 5),
(21, 'Boutilimit', 6),
(22, 'Keur Macène', 6),
(23, 'Méderdra', 6),
(24, 'Ould Teguedi', 6),
(25, 'RKiz', 6),
(26, 'Atar', 7),
(27, 'Chinguetti', 7),
(28, 'Ouadane', 7),
(29, 'Tidjikdja', 7),
(30, 'Dakhlet Nouadhibou', 8),
(31, 'El Mina', 8),
(32, 'Moudjeria', 9),
(33, 'Tichit', 9),
(34, 'Tidjikdja', 9),
(35, 'Ould Yengé', 10),
(36, 'Sélibaby', 10),
(37, 'Gouraye', 10),
(38, 'Ould Mbareck', 10),
(39, 'Bir Moghrein', 11),
(40, 'Fdérik', 11),
(41, 'Zouérat', 11),
(42, 'Akjoujt', 12),
(43, 'Akjoujt', 12),
(44, 'Dar-Naim', 13),
(45, 'Teyarett', 13),
(46, 'Toujounine', 13),
(47, 'Arafat', 14),
(48, 'Ksar', 14),
(49, 'Sebkha', 14),
(50, 'Tevragh-Zeina', 14),
(51, 'El Mina', 15),
(52, 'Riyadh', 15),
(53, 'Maghta-lehjar', 5);

-- --------------------------------------------------------

--
-- Structure de la table `myapp_maghataa`
--

DROP TABLE IF EXISTS `myapp_maghataa`;
CREATE TABLE IF NOT EXISTS `myapp_maghataa` (
  `ID_maghataa` int NOT NULL,
  `Nom_maghataa` varchar(100) NOT NULL,
  `ID_wilaya_id` int NOT NULL,
  PRIMARY KEY (`ID_maghataa`),
  KEY `myapp_maghataa_ID_wilaya_id_378c2293` (`ID_wilaya_id`)
) 

-- --------------------------------------------------------

--
-- Structure de la table `myapp_users`
--

--------------------------------------------------------

--

-- --------------------------------------------------------

--
-- Structure de la table `myapp_wilaya`
--
 --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tel` int NOT NULL DEFAULT '0',
  `email` varchar(100) NOT NULL,
  `password` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) 

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `tel`, `email`, `password`) VALUES
(1, 42044524, '22086@supnum.mr', '1234');

-- --------------------------------------------------------

--
-- Structure de la table `village`
--

DROP TABLE IF EXISTS `village`;
CREATE TABLE IF NOT EXISTS `village` (
  `ID_village` int NOT NULL,
  `Nom_village` varchar(255) DEFAULT NULL,
  `ID_commune` int DEFAULT NULL,
  PRIMARY KEY (`ID_village`),
  KEY `ID_commune` (`ID_commune`)
)

-- --------------------------------------------------------

--
-- Structure de la table `wilaya`
--

DROP TABLE IF EXISTS `wilaya`;
CREATE TABLE IF NOT EXISTS `wilaya` (
  `ID_wilaya` int NOT NULL,
  `Nom_wilaya` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_wilaya`)
) 

--
-- Déchargement des données de la table `wilaya`
--

INSERT INTO `wilaya` (`ID_wilaya`, `Nom_wilaya`) VALUES
(13, 'Nouakchott Nord'),
(12, 'inchiri'),
(1, 'Hodh Ech Chargui'),
(2, 'Hodh El Gharbi'),
(3, 'El essaba'),
(4, 'Gorgol'),
(5, 'Brakna'),
(6, 'Trarza'),
(7, 'Adrar'),
(8, 'Dakhlet Nouadhibou'),
(9, 'Tagant'),
(10, 'Guidimaka'),
(11, 'Tiris Zemmour'),
(14, 'Nouakchott Ouest'),
(15, 'Nouakchott Sud');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
