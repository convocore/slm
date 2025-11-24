import yaml
import os

def test_persona_files_exist():
    files = ["wanderer.yaml", "archivist.yaml", "anomaly.yaml"]
    for f in files:
        path = os.path.join("examples", "personas", f)
        assert os.path.exists(path)
