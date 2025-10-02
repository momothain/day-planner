from typing import List, Literal, Annotated, Self
from pydantic import BaseModel, Field, model_validator

"""Time is minutes-since-midnight. Date, timezone in Plan."""
MinSinceMidnight = Annotated[int, Field(ge=0,le=1439)] # 24hr * 60min/hr = 1440. 23:59=1439min

class Time(BaseModel):
    kind: Literal["block", "duration"] = Field(alias="type", repr="False")

class TimeBlock(Time):
    kind = "block"
    start: MinSinceMidnight
    end: MinSinceMidnight #val > start below
    duration = Field(default_factory=lambda data: data["end"] - data["start"])

    @model_validator(model='after')
    def end_over_start(self) -> Self:
        if not (self.end > self.start):
            raise ValueError(f"End ({self.end}) must be greater than start ({self.start}).")
        return Self
    

class TimeDuration(Time):
    kind = "duration"
    duration: MinSinceMidnight


class Plan(BaseModel):
    # Core
    task: str = Field(min_length=1, max_length=64) # DB
    time: Time = Field(discriminator="kind")
    #
    tags: List[str] # DB
    freq: str # num / period 
    subtasks: List[str] #in a DB
    # # 
    timezone: str # type/val?
    date: str # type # means its instantiated
    start_time: MinSinceMidnight # aka "midnight" for our minutes-since-midnight time representation

    ## time invar
    # invariant -- 24hours in a day max
    # inv - non-overlap time


### Features