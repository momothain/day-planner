from config import Config
from models import Plan, Task

import pandas as pd

"""12/2- Plan->df.columns: ['name', 'time', 'tags', 'freq', 'subtasks', 'details']"""
def plan_to_df(plan: Plan):
    task_dicts = [task.model_dump() for task in plan.tasks]
    df = pd.DataFrame(task_dicts)

    ### CONVERT TIME TO DURATION
    df["time"] = df["time"].apply(lambda dc: dc["duration"])
    df = df.rename(columns={"time":"duration"})

    return df

def agg_duration_by_task(plan_df: pd.DataFrame):
    task_groups = plan_df.groupby("name")
    task_sums = task_groups["duration"].sum()
    task_sums = task_sums.sort_values(ascending=False)
    print(task_sums)

def agg_duration_by_tags(plan_df: pd.DataFrame):
    dupe_df = plan_df.explode("tags")
    print(dupe_df.groupby("tags")["duration"].sum().sort_values(ascending=False))
    
if __name__ == "__main__":
    # p = Plan(tasks=[], start_time=1)
    p = Plan.read_csv(Config.plan_example)
    df = plan_to_df(p)
    agg_duration_by_task(df)
    # agg_duration_by_tags(df)
    # print(df.head())
    print("done agg")