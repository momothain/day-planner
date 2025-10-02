# log
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