# 🚀 Pipelines

[![Automation](https://img.shields.io/badge/Automation-Workflow-blueviolet?style=for-the-badge)]()

This directory contains the orchestration logic that ties all the [Components](../components/README.md) together into a cohesive workflow.

## 🛠️ Training Pipeline (`training_pipeline.py`)

The `TrainingPipeline` class is the conductor of the orchestra. It is responsible for:

1. **Initialization**: Setting up the configurations.
2. **Execution Flow**: Running components in the correct order:
    * `start_data_ingestion()`
    * `start_data_validation()`
    * `start_data_transformation()`
    * `start_model_trainer()`
3. **Artifact Passing**: Ensuring the output of one step is correctly passed as input to the next.

### Usage

The pipeline is triggered via the `/train` endpoint in the FastAPI app or can be run directly via `main.py`.

```python
from networksecurity.pipeline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()
```

---

<p align="center">
  <a href="../README.md">⬅️ Back to Package README</a>
</p>
