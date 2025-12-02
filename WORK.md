# log
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