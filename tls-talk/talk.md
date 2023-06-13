---
marp: true
title: Marp CLI example
description: Hosting Marp slide deck on the web
theme: uncover
class: invert
---

# TLS, Certificates, Ciphers

---


## HTTPS

- HTTPS == Hypertext Transfer Protocol Secure
- encrypted version of the HTTP protocol
- uses SSL/TLS to secure the connection between the client and server

```
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* Connection state changed (HTTP/2 confirmed)
```

---

## HTTPS Protocol Stack

| Layer        | old        | current    | soon™          |
| -----------: | :--------- | :--------- | :------------- |
| Semantics    | HTTP       | HTTP       | HTTP           |
| Application  | HTTP/1.1   | HTTP/2     | HTTP/3         |
| Presentation | SSL/TLS    | TLS 1.2+   | QUIC + TLS 1.3 |
| Transport    | TCP        | TCP        | UDP            |
| Network      | IPv4, IPv6 | IPv4, IPv6 | IPv4, IPv6     |

---

## TLS

- TLS == Transport Layer Security
- protocol for securing communication over the internet
  - happens at TCP level, i.e. one layer below  HTTP
- successor to SSL (Secure Sockets Layer) protocol
  - SSL sometimes still used as a synonym ...
  - ... but no one actually encrypts with SSL anymore

---

## How TLS Uses Encryption
- combination of symmetric and asymmetric encryption
- client & server negotiate a shared symmetric key
- this key is exchanged using asymmetric encryption
- data is encrypted with symmetric key

---

## Symmetric Encryption
- same key to encrypt and decrypt data
- both sender and recipient must have the same key
- requires a secure method of exchanging keys

---

## Asymmetric Encryption
- uses different keys to encrypt and decrypt data:
  - a public key (can be freely shared)
  - a private key (is kept secret)
- slower than symmetric encryption


--- 

## TLS handshake
During a TLS handshake client and server negotiate:

- Which version of TLS they will use
- Which cipher suites they will use
- Authenticate the identity of the server via certificates
- Optional mTLS: Authenticate the identity of the **client**
- Generate symmetric encryption session keys

---

## TLS 1.2 handshake and key exchange
<style scoped>section { font-size: 25px; }</style>

1. Client hello: the client sends a hello message to the server, specifying its supported TLS version and cipher suites
2. Server hello: the server responds with a hello message, selecting the TLS version and cipher suite that both parties support
3. Server certificate: the server sends its digital certificate to the client, which includes the server's public key and other information about the certificate
4. Client key exchange: client uses the selected cipher suite, generate a random key, encrypts it with the server's public key, send to the server
6. Change cipher spec: both parties agree to switch to the encrypted mode using the negotiated symmetric key
7. Finished: both parties confirm that the handshake is complete

---


## Certificates

The HTTPS certificates "certify" a certain domain, but the protocol and encryption happen at the TCP level, before knowing which domain is being dealt with.

