# Workflow Setup Visualization Prototype

# Initial setup: Clone the repository, create an environment, activate the environment

```bash
python3 -m venv workflow-viz-env
source workflow-viz-env/bin/activate
pip install -r requirements.txt
```

# Start up a Tiled server

```bash
tiled/tiled_catalog_register.sh
tiled/tiled_config_serve.sh
```