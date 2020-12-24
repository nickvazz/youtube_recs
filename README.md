# youtube_recs 

This repo will generate data to analyze how youtube's recomendations are distributed from different starting points.

## generating data
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python cli.py SEARCH_TERM COUNT STARTING_VIDEO_URL
```

`SEARCH_TERM` that is logged with data
`COUNT` will be how many recommendations deep it will aggregate data from
`STARTING_VIDEO_URL` the url to start from
