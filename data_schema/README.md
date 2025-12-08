# 📜 Data Schema

[![YAML](https://img.shields.io/badge/Format-YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)]()
[![Data Quality](https://img.shields.io/badge/Data-Quality-success?style=for-the-badge)]()

This directory contains the contract for our data. The `schema.yaml` file is the single source of truth for what our data should look like.

## 📋 schema.yaml

This file defines:

1. **Columns**: The list of all expected columns in the dataset.
2. **Data Types**: The expected data type (e.g., `int64`) for each column.
3. **Numerical Columns**: A subset of columns that are numerical and may require scaling.

### Why is this important?

The **Data Validation** component uses this file to strictly enforce data quality. If incoming data (for training or prediction) does not match this schema, the pipeline will raise an error, preventing garbage data from corrupting the model.

---

<p align="center">
  <a href="../README.md">⬅️ Back to Main README</a>
</p>
