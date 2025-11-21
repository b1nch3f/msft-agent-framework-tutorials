### Setting PYTHONPATH

```
powershell

$env:PYTHONPATH = $pwd
```

### Running the agent

`python .\core\run.py`

### Running the Server

`uvicorn api.server:app --port 8000 --reload`

### Running the UI

`streamlit run .\ui\st_main.py`
