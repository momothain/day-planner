from pathlib import Path


class Config:
    ### FILEPATHS
    test_output = Path("./test_output")
    test_output.mkdir(exist_ok=True)
    output = Path("./output")
    output.mkdir(exist_ok=True)
    
    plan_example = Path("./data/schedule-example.csv")
    dayplan_example = Path("./data/example1.dayplan")
    
    ### CONSTANTS
    LOG_DELIM = "\n\n======\n\n"
    DAYPLAN_DELIM = "\n\n"
    HEADER_DELIM = ","
    