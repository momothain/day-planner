# day-planner
## init venv
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

# TODO
## Models / Data Structure
- [x] .dayplan concrete instance
    - [x] read parser
        - [] review
    - [] pydantic model -> write json
- []? Tags can have relations. e.g. "Eating" Tag => "Basics". so can skip writing basics when there is eating, but could count for aggregation stats for basics..?
- []! In general, if Task (concrete) has appeared before w/ certain Tags, perchance if no Tags are assigned, all prev assoc Tags will be assigned to the new instance. if clustering and cleanup is done, that will help.....

## Aggregation / Statistics
- [x] aggregation of duration by task and tags (exploded such that a single task will "repeat" counts toward all assoc. tags)
- [x] pyd -> pandas
- [x] TimeUnion -> duration
- [] add Task.name to Task.tags before explosion so it counts as a Tag for aggregation
- [] for .dayplan inst, delete rows where Cancelled=true. ignore `done`
### secondary metrics
- \# unique tasks 
- Distribution/plot of task x total_occurences
- ! Since Tags of Tasks can intersect and be double-counted, we should measure the `quantity, %overlap` of Tasks for `pairs of Tasks` -> `cluster` Tags for fewer buckets and more meaningful stats & plots. 
    - can also be semantic a la PartPredictor.
    - motivation: the occurence and amount of Tags for a Task depends on the human's whim on the day to do more data labelling


## UI: Visualization + Interactive Elements
- makes CRUD (below) feel more motivated, as you have a tangible sense of the plans and can tweak it for the day. UI will make the testing easier as well.

## Database Management / Backend CRUD
- sort tasks by time
- insert in order
- Anchor to real calendar/dates


# DESIGN - Daily Schedule – 24 Hours

***Task,Tags,Time,Frequency,Subtask***

## App Goals

### Core

- Visualize Time-Tasks in a 24 hour calendar format.
    - Fix Time Blocked Tasks in place (edit with prompt).
    - Allow Duration Tasks to both moved around and stretched like other calendar apps
- Allow Day Templates to be instantiated into a Day Schedule.
    - Prompt non-HARD tasks to be filled in with potential Subtasks

### QoL

- Allow Schedules to be copied. Allow defaults to be set for each day of the week.

### Data – Tasks and Tags

- Allow Tasks to be pre-defined with times and details. Inserted easily. Suggested appropriately.
- Associate Tags to Tasks. Allow `view by tag`. Visualize breakdown of time by tag in a day, week, month, all time…somewhat similar to Screen Time.
- Allow a Template to list a Tag instead of a Task (see Job(tag) ex)

### Usage – ToDo list, reminders, pomodoro timer for tasks, and time tracking

- Allow users to check off tasks as they do them.
- Allow them to push back one task and thus pushback everything after it.
    - Allow overflow past 24 hours but flag it.
    - Consider Time Blocked Tasks to not be move-able.
        - Allow overlap of Tasks if a Duration Task gets pushed into a hard Time Block, but flag it.
- ¿How to handle deletion and early completion?

---

## Example Template

Pre-Sleep, Basics;Sleep, 00:20-01:20, DAILY, shower;journal;brush teeth;bathroom;read;listen dr k

Sleep, Basics;Sleep, 01:20-09:20, DAILY, HARD

Morning, Basics;Sleep, 9:20-10:00, DAILY, sit;dream journal;brush teeth;bathroom;read

Yog, Health;Spirituality, 45-75min, 5 DAY/WK, HARD

Breakfast, Basics;Eating, 30-60min, DAILY, toast;peanut butter;nutella;cereal

Job(tag), 45-120min, 2/DAY

### *Example of Job(tag) Task*

Study Leetcode, Job;Learn, 45-120min, 6 DAY/MO, link to neetcode

## Data Syntax Definition

*Interline-[**\n**]. Delimeter-[**,**]. Sub-delimeter-[**;**].*

***Task,Tags,Time,Frequency,Subtask***

***ALT: Tag,Time,Frequency***

***DETAILS:*** 

- ***Task,***
- ***Tag1;Tag2,***
- ***Time***
    - ***Hard Time Block(xx:xx-xx:xx) or***
    - ***Duration or Duration range in min or hours},***
- ***Frequency x/day, x/wk,…***
- ***Subtask1;subtask2 options* or *HARD meaning it is just one predesignated routine***