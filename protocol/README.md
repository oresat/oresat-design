# Description of protocols used on CS-0

## Over-the-air protocols
These protocols are used for communications between the spacecraft and the ground.

#### Protocols intended for the general public
These are intended to give beacon data to the general public for amateur radio outreach. It is envisioned that the amateur community would reply back to the OreSat team with notices of telemetry they recieved by means of Internet email, giving OreSat information about the satellite particulary when it is out of range of the OreSat ground stations.

* ___CW Packet Protocol___
   -- This is the Morse Code message beacon sent on the UHF-Band during 10 minute periodic telemetry times.

* ___AX.25 Packet Protocol___
   -- This is the AX.25 digital packet radio beacon sent on the UHF-Band using G3RUH modulation during 10 minute periodic telemetry times. This follows just after the CW beacon.

#### Protocols intended for OreSat only
These are intended as the engineering command, control and telemetry messages for operating the satellite. These protocols should follow _to some extent_ guidelines provided by CCSDS. https://public.ccsds.org/Publications/default.aspx


* ___Engineering Data Uplink___
   -- This is the data format of the engineering uplink sent on the L-Band for control of the satellite, or for requesting a downlink of stored data. Several components of these messages are to be encrypted. The messages are also to be authenticated.
   
* ___Engineering Data Downlink___
   -- This is the data format of the engineering downlink sent on UHF for control responses and downlinked data. The responses would include acquired data and more detailed telemetry. These messages are to be authenticated. No encryption is required.
   
* ___DxWiFi Uplink___
   -- TBD on S-Band

* ___DXWiFi Downlink___
   -- TBD on S-Band

## Onboard protocols
These messages are used between subsystems on the spacecraft. They are not ever to be sent over the radio. There is no encryption or authentication. These protocols should follow _to some extent_ guidelines provided by CCSDS. https://public.ccsds.org/Publications/default.aspx

* ___C3 to xxx over CAN___
  -- TBD

* ___Xxx to C3 over CAN___
  -- TBD

