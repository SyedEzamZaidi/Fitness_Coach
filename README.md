# Fitness_Coach

Multi-agent coaching system for diet and exercise. A central coach agent coordinates specialist agents (diet/macros, fitness data, food scanning, recommendations) and keeps short- and long-term memory of the user.

## What it does
- grounded diet and exercise guidance (defers to a professional, doesn't diagnose)
- RAG over a nutrition / exercise-science knowledge base
- short- and long-term memory (profile + logs in Postgres)
- human approval gate before it recommends any purchase

## Stack
Python, LangGraph, Groq, Chroma, sentence-transformers, PostgreSQL

## Status
In development, building it in phases.
