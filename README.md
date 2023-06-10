# SmartSense
## Introduction
The purpose of this project is to track the readings of the sensors in the room, which are sent from the station built on the basis of the ESP8266. The project consists of three main parts - this is a website for direct viewing of readings, a sectch with which the ESP8266 microcontroller is flashed and a server that receives data from the station and writes them to the database.

The development of all parts of the application was carried out in separate repositories
-   Sketch for ESP8266 firmware with a description of the settings https://github.com/stemirkhan/SmartSenseSketch/tree/main
- A server that receives data from the ESP8266 and writes it to the database https://github.com/stemirkhan/SmartSenseServer
- A site with a unified server for receiving data from the station, and docker files for quick deployment of all services https://github.com/stemirkhan/SmartSense

![General scheme](readme-assets/general-scheme.png)


## Showcase

![Responsiveness of the site](readme-assets/responsiveness.gif)

 ## Table of Contents


  - [Deployment](#deployment)
    - [Prodactions](#prodactions)


## Deployment