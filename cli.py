from persine import PersonaEngine
import click
import pandas as pd
import os


@click.command()
@click.argument('search-term')
@click.argument('count')
@click.argument('starting-video-url', default="https://www.youtube.com/watch?v=U5R8qWCBA2M")
@click.option('--headless', is_flag=True)
def run_search(search_term, count, starting_video_url, headless):

    engine = PersonaEngine(headless=headless)
    with engine.persona() as persona:
        # persona.run("youtube:search?{}".format(search_term))
        persona.run(starting_video_url)
        persona.run("youtube:next_up#{}".format(count))

        history = persona.history.to_df()
        recs = persona.recommendations.to_df()

        history['search_term'] = search_term
        recs['search_term'] = search_term
        
        
    if os.path.exists('hist.csv'):
        old_hist = pd.read_csv('hist.csv')
        history = pd.concat([old_hist, history])

        old_recs = pd.read_csv('recs.csv')
        recs = pd.concat([old_recs, recs])

    history.to_csv('hist.csv', index=False)
    recs.to_csv('recs.csv', index=False)


    
if __name__ == '__main__':
    run_search()
