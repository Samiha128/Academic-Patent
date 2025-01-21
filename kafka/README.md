 
## Kafka

This project sets up a local Kafka environment using Docker Compose with two main services: Zookeeper and Kafka. Zookeeper is used for managing Kafka's metadata, while Kafka handles real-time data streaming. The configuration in the docker-compose.yml file defines the listening ports, service connections, and settings required to run a Kafka cluster. This setup is used to extract data from Scopus via a Kafka cluster running in a Docker container.

## 

- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licences](#licences)

## Introduction

**Apache Kafka** est un système de messagerie distribué à haut débit. Il permet de transmettre des données en temps réel entre des producteurs et des consommateurs. Kafka est largement utilisé pour des cas d'usage tels que la gestion de logs, l'analyse en temps réel des données, et la gestion des événements dans des architectures microservices.

Dans ce projet, vous apprendrez à configurer un cluster Kafka, à produire et consommer des messages avec des producteurs et consommateurs Kafka.

## Prérequis

Avant de commencer, vous devez disposer des éléments suivants :

- **Java 8 ou supérieur** : Kafka est écrit en Java et nécessite Java pour fonctionner.
- **Zookeeper** : Kafka utilise Zookeeper pour coordonner le fonctionnement du cluster. Il doit être installé et configuré.
- **Kafka** : Téléchargez et installez Kafka depuis le site officiel.
- Un gestionnaire de paquets comme `Maven` ou `Gradle` si vous souhaitez l'intégrer dans un projet Java.

## Installation

### 1. Cloner ce dépôt

Clonez ce dépôt sur votre machine locale pour commencer à l'utiliser.

```bash
git clone https://github.com/votre-utilisateur/votre-repository.git
cd votre-repository
