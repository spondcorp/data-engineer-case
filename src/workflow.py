from src.tasks.rsvp_summary import rsvp_summary
from src.tasks.daily_active_teams import daily_active_teams
from flytekit import workflow, FlyteDirectory
import os


@workflow
def daily_workflow(
    data_dir_path: FlyteDirectory, output_dir_path: str
) -> tuple[str, str]:
    daily_active_teams_data_path = daily_active_teams(
        data_dir_path=data_dir_path, output_dir_path=output_dir_path
    )
    rsvp_summary_data_path = rsvp_summary(
        data_dir_path=data_dir_path, output_dir_path=output_dir_path
    )
    return (daily_active_teams_data_path, rsvp_summary_data_path)


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir_path = os.path.join(root_dir, "data")
    output_dir_path = os.path.join(root_dir, "output")
    daily_active_teams_data_path = daily_workflow(data_dir_path, output_dir_path)
    print(f"Daily active teams data path: {daily_active_teams_data_path}")
