# model_fmt.py
from util import prepend_log
from config import Config

import json
import re
from typing import List, Literal, Annotated, Optional, Self, Union
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator
from pathlib import Path
import csv

"""Time is minutes-since-midnight. Date, timezone in Plan."""


MinSinceMidnight = Annotated[
    int, Field(ge=0, le=1439)
]  # 24hr * 60min/hr = 1440. 23:59=1439min

class Time(BaseModel):
    model_config = dict(populate_by_name=True)
    kind: Literal["block", "duration"] = Field(alias="type", repr=False)
    
class TimeBlock(Time):
    kind: Literal["block"] = "block"
    start: MinSinceMidnight
    end: MinSinceMidnight  # val > start below
    
    @computed_field
    @property
    def duration(self) -> MinSinceMidnight:
        return self.end - self.start
    # duration: MinSinceMidnight = Field(
    #     default_factory=lambda data: data["end"] - data["start"]
    # )

    #
    @model_validator(mode="after")
    def _end_over_start(self) -> Self:
        if not (self.end > self.start):
            raise ValueError(
                f"End ({self.end}) must be greater than start ({self.start})."
            )
        return self


class TimeDuration(Time):
    kind: Literal["duration"] = "duration"
    duration: MinSinceMidnight
TimeUnion = Annotated[Union[TimeBlock | TimeDuration], Field(alias="Time", discriminator="kind")]

###
""""""
class Task(BaseModel):
    # Settings
    model_config = dict(populate_by_name=True)
    # Core
    name: str = Field(
        min_length=1, max_length=64, alias="Task"
    )  # DB #store as lower, rep as Pascal?
    time: TimeUnion # Have to use union can't use parent class :(
    #
    tags: List[str] = Field(default=[], alias="Tags"
                            )  # DB
    freq: str = None  # num / period # used for checking once time spent statistics are aggregated
    subtasks: Optional[List[str]] = None  # in a DB
    details: Optional[dict] = None

    ###

    ## Preprocess, Read Validate
    @field_validator("name", mode="after")
    @classmethod
    def preprocess_name(cls, name: str) -> str:
        s = name.strip().lower()
        return " ".join((word.capitalize()) for word in s.split(" "))

    @field_validator("tags", "subtasks", mode="before")
    def preprocess_list(cls, ls: str | list) -> list:
        if isinstance(ls, list):
            return [cls.preprocess_name(s) for s in ls]
        elif isinstance(ls, str):
            out = ls.split(";")
            out = [cls.preprocess_name(s) for s in out]
            return out
        else:
            raise TypeError(f"require str or list, got {ls}")

    @field_validator("time", mode="before")
    # read_time
    def preprocess_time(cls, t) -> Time:
        if isinstance(t, Time):
            return t
        elif isinstance(t, str):
            t = t.strip()
            if re.match(r"\d\d:\d\d[-,]\d\d:\d\d", t):
                return TimeBlock(
                    kind="block",
                    start=int(t[0:2]) * 60 + int(t[3:5]),
                    end=int(t[0 + 6 : 2 + 6]) * 60 + int(t[3 + 6 : 5 + 6]),
                )
            elif re.match(r"\d+", t):
                return TimeDuration(kind="duration", duration=int(t))
            # elif re.match(r"\d+[-,]\d+", t):
            #     ... #return TimeDurationRange()
            
        raise ValueError(
            f"Couldn't read {t}. Please use 'xx:xx-xx:xx', duration, 'xx-xx' duration range"
        )
        
    ## Overrides
    def __str__(self):
        str = self.model_dump_json(indent=2, exclude_none=True)
        prepend_log(Config.test_output / "task.log", str)
        return str


def test_task():
    print("START test_task(): ===============")
    p1 = Task(
        name="task1",
        time=TimeDuration(kind="duration", duration=60),
        tags=["tg1", "tg2"],
        freq="5/wk",
    )
    print(p1)
    
    p2 = Task(
        name=" task2   ",
        time=TimeDuration(kind="duration", duration=60),
        tags=" tg1 ;tg2",
        freq="2/day",
    )
    print(p2)
    
    p3 = Task(
        name="sleep",
        time=TimeBlock(kind="block", start=0, end=480),
        tags="core",
        freq="1/day",
    )
    print(p3)
    print("END test_task(): ===============")
    print()
    
    return


###
""""""
class Plan(BaseModel):
    tasks: List[Task]
    timezone: str = None  # type/val?
    date: str = None  # type # means its instantiated
    start_time: MinSinceMidnight = (
        0  # aka "midnight" for our minutes-since-midnight time representation
    )

    ## time invariants
    # [x] 24hours in a day max (handled by MinSinceMidnight maxval = 1439)
    # [] non-overlap time
    # [] order tasks by time
    
    ## QoL
    # - visualize tasks by time spatially

    @classmethod
    def read_csv(cls, fp: Path) -> Self:
        print(f"reading Plan from {fp}")
        with fp.open(mode="r") as f:
            reader = csv.DictReader(f)
            tasks = [Task.model_validate(row) for row in reader]
            # tasks = []
            # for row in reader:
            #     print(row)
            #     Task.model_validate(row)
            return Plan(tasks=tasks)
        
    
    ## Overrides
    def __str__(self):
        str = self.model_dump_json(indent=2, exclude_none=True)
        prepend_log(Config.test_output / "plan.log", str)
        return str


def test_plan():
    print("START test_plan(): ===============")
    
    p1 = Plan.read_csv(Config.plan_example)
    print(p1.__str__())
    
    print("END test_plan(): ===============")
    print()
    return

### Features

### Run Test
if __name__ == "__main__":
    # t: Time = 
    test_task()
    test_plan()
