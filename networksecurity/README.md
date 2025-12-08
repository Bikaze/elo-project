# 📦 Network Security Package

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Package](https://img.shields.io/badge/Package-Source-blue?style=for-the-badge)]()

Welcome to the core of **PhishNet**. This directory contains the entire source code for the machine learning pipeline, exception handling, logging, and utility functions.

## 📂 Directory Structure

| Module | Description |
| :--- | :--- |
| [**🧩 components/**](components/README.md) | The heart of the ML pipeline. Contains modules for Ingestion, Validation, Transformation, and Training. |
| [**🚀 pipeline/**](pipeline/README.md) | Orchestration scripts that connect components together to form a workflow. |
| **📄 entity/** | Defines `Config` objects (inputs) and `Artifact` objects (outputs) for strict typing. |
| **🔢 constant/** | Centralized configuration for file paths, database names, and model parameters. |
| **🛠️ utils/** | Helper functions for file I/O, model saving/loading, and metric calculation. |
| **⚠️ exception/** | Custom exception handling to provide detailed error traces. |
| **📝 logging/** | Centralized logging configuration to track pipeline execution. |

---

<p align="center">
  <a href="../README.md">⬅️ Back to Main README</a>
</p>
