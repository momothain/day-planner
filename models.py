from typing import List
from pydantic import BaseModel, Field

"""Time is minutes-since-midnight"""
class Plan(BaseModel):
    # Core
    task: str = Field(...)
    time_start: int = Field(..., ) # duration or timestamp,timestamp (w/ timezone)
    #
    # tags: List[str]
    # freq: num / period 
    # subtaskss: List[str]
    # # 
    # timezone: ...
    # date: ... # means its instantiated
    # start_time # aka "midnight" for our minutes-since-midnight time representation

    ## time invar
    # invariant -- 24hours in a day max
    # inv - non-overlap time


### Features