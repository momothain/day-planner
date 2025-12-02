from pathlib import Path


class Config:
    ### FILEPATHS
    test_output = Path("./test_output")
    test_output.mkdir(exist_ok=True)
    
    plan_example = Path("./data/schedule-example.csv")
    
    
    ### CONSTANTS
    LOG_DELIM = "\n\n======\n\n"
    