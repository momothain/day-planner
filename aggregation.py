from config import Config
from models import Plan, Task

import pandas as pd

"""12/2- Plan->df cols: ['name', 'time', 'tags', 'freq', 'subtasks', 'details']"""
def plan_to_df(plan: Plan):
    task_dicts = [task.model_dump() for task in plan.tasks]
    df = pd.DataFrame(task_dicts)
    if plan.start_time != 0:
        # log.warning("plan.start_time is {plan.start_time}. handle times appropriately? no need actually that would be really weird to aggregate specific time of day but ig you could do it")
        ...
    # print(df["time"][0])
    ### CONVERT TIME TO DURATION
    df["time"] = df["time"].apply(lambda dc: dc["duration"])
    df = df.rename(columns={"time":"duration"})
    # print(df.columns) # Index(['name', 'time', 'tags', 'freq', 'subtasks', 'details'], dtype='object')
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