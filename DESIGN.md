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