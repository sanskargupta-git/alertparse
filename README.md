# 🚨 AlertParse – Real-Time Log Parser & Alert System

**AlertParse** is a Python tool that monitors live log files for known threat signatures such as:
- Failed logins
- SQL injection attempts
- Privilege escalation
- Access to system files

## 🔧 Features

- Live `tail -f` style monitoring
- Regex-based alert signatures
- Console alerting + optional file logging
- Useful for SecOps, SOC, SIEM simulation

## 🛠️ Usage

```bash
python alertparse.py -f /var/log/auth.log -o alerts.log
