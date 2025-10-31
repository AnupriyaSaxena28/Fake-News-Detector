# AI Fake News Detector — Chatbot (Full Project)

This repository contains a web-based chatbot (React + Vite frontend) and a Flask backend that serves an AI-based fake news detector.

Contents:
- backend/: Flask API, training script, utils, model placeholders
- frontend/: React + Vite chatbot UI
- docker/: Dockerfiles and docker-compose
- deployment-guides/: step-by-step deploy guides for Render, Vercel, and Heroku

Notes:
- This "full" package includes dataset placeholders (small sample files), Docker setup, and an optional transformer setup script (no large transformer models included).
- Train the TF-IDF model with `python backend/train.py` after placing datasets in `backend/dataset/`.
