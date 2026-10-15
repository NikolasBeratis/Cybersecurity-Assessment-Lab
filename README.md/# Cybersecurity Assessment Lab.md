# Cybersecurity Assessment Lab

## Overview

This project documents a hands-on cybersecurity assessment conducted in a controlled virtual lab environment using two Kali Linux virtual machines.

The lab focuses on network reconnaissance, network traffic analysis, SSH session inspection, Linux authentication and password security, and security hardening through SSH configuration and firewall rules.

The objective was to observe system behavior, identify exposed services, examine authentication mechanisms, and validate selected defensive security controls.

## Lab Environment

The project used two virtual machines hosted in VirtualBox.

| Component               | Details           |
| ----------------------- | ----------------- |
| Virtualization platform | Oracle VirtualBox |
| Operating system        | Kali Linux        |
| Assessment machine      | `192.168.56.101`  |
| Target machine          | `192.168.56.103`  |
| Remote access service   | OpenSSH           |
| SSH port                | TCP/22            |

All testing was conducted within the controlled lab environment.

## Project Chapters

### Chapter 1 — Network Reconnaissance

* Verified network connectivity between the virtual machines.
* Examined ICMP traffic.
* Performed an initial Nmap scan.
* Identified the SSH service after it was started on the target machine.

### Chapter 2 — Network Traffic Analysis

* Captured SSH traffic using Wireshark.
* Examined the TCP three-way handshake.
* Inspected SSH protocol banners and key-exchange metadata.
* Observed the transition to encrypted SSH traffic.

### Chapter 3 — SSH Sessions and System Inspection

* Established an SSH session from the assessment machine to the target.
* Inspected logged-in users and active network connections.
* Examined SSH service status and available system logs.

### Chapter 4 — Linux Authentication and Permissions

* Examined the structure of Linux account entries.
* Investigated the relationship between `/etc/passwd` and `/etc/shadow`.
* Reviewed file permissions and privilege boundaries.
* Examined account password-hash information.

### Chapter 5 — Password Hash Testing

* Investigated John the Ripper in a controlled lab.
* Examined password-hash compatibility.
* Performed a demonstration using a synthetic MD5 hash and a small test wordlist.
* Observed the limitations of password recovery attempts.

The MD5 demonstration used a synthetic test hash and did not represent a successful crack of the target account's yescrypt hash.

### Chapter 6 — SSH Hardening and Firewall Validation

* Configured SSH to disable password authentication.
* Validated the SSH configuration syntax.
* Confirmed that public-key authentication remained available.
* Tested password-only authentication and observed rejection.
* Enabled UFW and reviewed inbound firewall rules.
* Repeated connectivity checks and performed a final Nmap scan.

The final scan reported TCP/22 as open and 999 other scanned TCP ports as filtered or receiving no response.

## Tools Used

* Kali Linux
* Oracle VirtualBox
* Nmap
* Wireshark
* OpenSSH
* Linux command-line utilities
* John the Ripper
* UFW (Uncomplicated Firewall)

## Key Outcomes

The lab demonstrated how network discovery, packet inspection, authentication controls, file permissions, and firewall rules contribute to a basic security assessment.

The SSH hardening configuration was validated, public-key access was confirmed, and password-only SSH authentication was rejected during testing.

The final network scan showed a substantially restricted externally visible TCP service surface within the lab.

## Scope and Limitations

This was a small, controlled virtual lab. Results apply to the tested configuration and environment and should not be interpreted as a comprehensive security audit of a production system.

Password-recovery testing was limited to a synthetic MD5 demonstration and compatibility testing with the target account's yescrypt hash. No successful recovery of the target account's yescrypt password was demonstrated.

## Repository Structure

* `report/` — Formal assessment report.
* `documentation/` — Technical learning documentation.
* `evidence/` — Supporting screenshots and lab evidence, when available.
* `configs/` — Example security configuration files.
* `scripts/` — Supporting scripts, if applicable.

## Ethical Statement

All activities were performed for educational purposes within a controlled lab environment using virtual machines under the project's control.

The techniques documented here are intended to support defensive security learning, system administration, and authorized security testing.
