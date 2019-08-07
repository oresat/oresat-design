# Description of protocols used on CS-0

## Over-the-air protocols
These protocols are used for communications between the spacecraft and the ground. By requirements of international treaty, these protocols must adhere to the requirements of described by the IARU <http://www.iaru.org/satellite.html> and are to be published with the request to coordinate frequencies. Only the encryption and message format of the uplink control is held in confidence with the IARU and ITU. All other protocol information is to be open to the amateur community.



#### Protocols intended for the general public
These are intended to give beacon data to the general public for amateur radio outreach. It is envisioned that the amateur community would reply back to the OreSat team with notices of telemetry they recieved by means of Internet email, giving OreSat information about the satellite particulary when it is out of range from any of the OreSat ground stations in the early phases of the mission. The protocol of these messages are chosen to be the most popular around the world for amateur satellite communication to enable and ease this participation.

* ___CW Packet Protocol___
   -- This is the Morse Code message beacon sent at 10 wpm from the spacecraft on the UHF downlink frequency during 10 minute periodic telemetry times.

* ___AX.25 Packet Protocol___
   -- This is the AX.25 digital packet radio beacon sent from the spacecraft on the UHF downlink frequency using 9600 bit/sec
G3RUH FSK modulation and whitening, no FEC, no encryption, during 10 minute periodic telemetry times. This emission comes just
after the periodic CW beacon.



#### Protocols intended for OreSat only
These are intended as the engineering command, control and telemetry messages for operating the satellite. These protocols should follow _to some extent_ guidelines provided by CCSDS <https://public.ccsds.org/Publications/default.aspx>, and must adhere to the requirements of international treaty as described by the IARU <http://www.iaru.org/satellite.html>. The protocols physical layer is an emission of specifically GMSK modulation with a BT of 0.3 on both up and down links.

* ___Engineering Data Uplink___
   -- This is the data format of the engineering uplink sent from the ground station on the L-Band for control of the satellite, or for requesting a downlink of stored data. Several components of these messages must be encrypted, and all of the messages are to be authenticated. There will be a mechanism of error detection and forward error correction.
   
* ___Engineering Data Downlink___
   -- This is the data format of the engineering downlink sent from the spacecraft on UHF for response to control and downlink of stored data. The stored data would include various portions of acquired data or more detailed telemetry. These messages are to be authenticated, but no encryption at all is permitted. There will be a mechanism of error detection and forward error correction.

#### Protocols deemed experimental
   -- These are intended as the bulk data links (and DxWiFi experiment) and are mostly TBD at this time.

* ___Bulk Data Uplink___
   -- TBD on S-Band; This is a BPSK uplink with a frame format that closely resembles 802.11b. This will be an alternate to the L-Band Engineering Control uplink. A second function will be the uplink portion the missions DxWiFi experiment.

* ___Bulk Data Downlink___
   -- TBD on S-Band; This is a BPSK downlink with a frame format that closely resembles 802.11b. The data frames sent will be initiated by data requests on the Engineering Control channel and contain large quantities of bulk mission data. A second function will be the downlink portion the missions DxWiFi experiment.

![OreSat Protocols](https://github.com/oresat/oresat-design/blob/gh-pages/protocol/20190715_131244.jpg)

## Onboard protocols
These messages are used between subsystems on the spacecraft. They are not ever to be sent over the radio. There is no encryption or authentication. These protocols should follow _to some extent_ guidelines provided by CCSDS. https://public.ccsds.org/Publications/default.aspx

* ___C3 to XXX (critical subsystem only)___
  -- TBD on CAN 1; There will be a mechanism of error detection and request for retransmission.

* ___XXX to C3 (critical subsystem only)___
  -- TBD on CAN 1; There will be a mechanism of error detection and request for retransmission.

* ___C3 to YYY___
  -- TBD on CAN 2; There will be a mechanism of error detection and request for retransmission.

* ___YYY to C3___
  -- TBD on CAN 2; There will be a mechanism of error detection and request for retransmission.
