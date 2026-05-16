# CLIbrarian

A CLI-based AI research agent that takes a user question, searches the web, and returns a synthesized answer with sources.

## Overview

CLIbrarian is a Python-based AI agent that combines web search with large language model reasoning to answer questions from the terminal. Instead of returning a list of links, it reads and synthesizes search results into a clear, sourced response.

The idea behind CLIbrarian came from a simple frustration: searching the web gives you links, but what you actually want is an answer. A librarian does not hand you a stack of books and walk away. They listen to your question, find the right sources, and come back with what you need to know.

CLIbrarian tries to bring that experience to the terminal. You ask a question in plain English, and instead of a list of URLs, you get a synthesized answer drawn from real, current sources with citations so you can dig deeper if you want to.

## Features (In Progress)

- Natural language question input via the terminal
- Automatic web search using the Tavily API
- LLM-powered synthesis of search results using the Anthropic API
- Source citations included in every response

## Tech Stack

- Python
- Anthropic API (Claude)
- Tavily Search API
- LangChain (planned)

## Status

Currently in active development.
