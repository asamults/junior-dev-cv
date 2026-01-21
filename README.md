# Python Data Processing

## Purpose
Small Python projects for processing structured data and generating insights.

## Features
- Parsing CSV files
- Filtering and summarizing data
- Simple automation scripts

## Technologies
- Python
- Pandas, CSV
- Linux

## Status
Junior-level project


# Job Application Bot (Python + Telegram)

A Telegram bot that helps junior developers find relevant job openings
and generate tailored cover letters using an LLM.

Designed as a **portfolio project** for Junior Python / Junior Data Engineer roles (UK market).

---

## 🚀 Features

- Searches for **Junior Python Developer / Junior Data Engineer** roles
- Sources jobs from RemoteOK (UK / remote-friendly)
- Generates UK-style cover letters (100–120 words)
- Telegram interface with commands
- Tracks applied jobs (SQLite)

---

## 🧰 Tech Stack

- Python 3.10
- aiogram (Telegram Bot API)
- OpenAI API (ChatCompletion)
- requests
- SQLite

---

## 📁 Project Structure

```text
job_bot/
├── bot/        # Telegram bot logic
├── jobs/       # Job search providers
├── llm/        # Cover letter generation
├── data/       # Resume storage
