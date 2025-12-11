# log
## 12
- logger w/ line numbers, src fp, levels
- [] writeout stats structured fmt
- claude code / ..


## 12/3/25, 1610-1850
- planning more agg, DayPlan (.dayplan) concrete Vs. Plan(Template) generic schedule w/ (gpt)[https://chatgpt.com/g/g-p-68dda8de895c8191861a958222f91b1e-interactive-day-task-planner-app/c/6930ab00-cf20-8327-b23b-78b022f2eb18]
- task, tag, 2ndary metric plan details
- impl reading dayplan
    - wrote out example1.dayplan w/ today real data -> led to Done checkbox t/f, Cancelled, 
    - date handling w/ dateutil -> datetime
    - added a stupid extra 30+30 case, impl not bad, debug took more time.
## 12/2/25, 930-1200
- pllaning in readme
- refactor paths,const to Config. util for log prepend. write logs added to __str__
    - models.31 (dur comp prop): BUG found thru trying to agg duration and printing NaN, not caught through MinSinceMidnight type ://
- core aggregation of duration by task and tags (exploded such that a single task will "repeat" counts toward all assoc. tags)


## 10/7/25
- fixed the errors. Actually, Task was erroring because of the `kind alias="type"` causing the code's sets `kind = "xxx"` not registering
    - solved with `model_config = dict(populate_by_name=True)`
- settled on `TimeUnion` as the usable type, and Time just exists for shared functionality
    - this means people that use TimeUnion have to handle each subtype's fields and functionality separately, as there is not interface defined for how to interact with all Time implementations, and the subclasses thus don't have e.g. `get_time_representation` or `set_time` or other stuff
- TODO: change prints to logs, and tests to DEBUG level
- edit, export functions. but to edit non-visually?....
- TODO:-next find a way to make Visuals then Interaction (so a UI)...MVP streamlit/dash/NiceGUI? or actual html-react

### Plan's time invariants
- [x] 24hours in a day max (handled by MinSinceMidnight maxval = 1439)
- [] non-overlap time
- [] order tasks by time


## 10/2/25
### actual 
- a lot of [field_validator](https://docs.pydantic.dev/2.11/concepts/validators/#field-validators) work to do the reading and preprocessing of all fields. "  task name " -> "Task Name", "t1;t2" -> ls
- Time regex matching and digit extracting 
    - debugging in process. erroring is weird, and parent/union type shit is not working
- basic test_task() and test_plan() w/ a schedule exmaple without TimeDurationRange and Task(tag)

### goals
- data in csv -> memory -> json
- validate, transform

## 10/1/25
- models.py, Time def via [pydantic Fields' constraints, etc](https://docs.pydantic.dev/2.11/concepts/fields/), [model_validator](https://docs.pydantic.dev/2.11/concepts/validators/#model-validators)