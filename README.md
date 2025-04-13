# Getting Started with Local setup

We are using below technologies for this task.

- Flyte for workflow orchastration
- uv package manager
- Docker and K8s for production deployment (Next steps)
- Github actions for CI/CD pipelines (Next steps)

We can execute unit tests for this project using below command:

```
python -m pytest tests/
```

# Aim of this coding task

The aim of this coding task is to assess the way you approach problems and design solutions, as well as providing insight into your coding style, expertise and willingness to experiment. It will also provide us with a common ground for a technical interview.

We'd love to see what kind of solution you come up with to the task below and how you approach problem solving.

There is no hard time limit set for this task, but we recommend allocating up to 3 hours to complete this task. Due to time constraints, we don't expect a perfect solution with all the edge cases covered. You’re encouraged to focus on your core strengths and things that you think are important — feel free to leave notes and TODOs if there are parts of implementation you didn’t manage to complete.

# Task Description

## Scenario

Spond provides a platform for organizing sports teams, events, and communication. In this challenge, you’ll simulate ingesting and transforming data about members, teams, and events (including RSVPs) to produce analytics. The focus is on:

1. **Data ingestion** \- reading source files or streaming data.
2. **Data modeling** \- designing efficient, scalable tables/structures.
3. **Transformations & analytics** \- consider how well your solution support queries and pipelines to answer common business questions.
4. **Performance & cost** \- consider impact and improvements to performance and cost in a production setting.
5. **Coding style & solution design** \- showcasing how you structure projects, write clean code, and handle error cases or edge conditions.

## Data Description

You are provided with three sample datasets (in CSV).

| Table       | Column                       | Description                                                              |
| :---------- | :--------------------------- | :----------------------------------------------------------------------- |
| teams       | team_id (string)             | Unique ID                                                                |
|             | group_activity (string)      | Activity type of group e.g., football, cricket, rugby, etc.              |
|             | country_code (string)        | Alpha-3 country code of group e.g., NOR=Norway; GBR=United Kingdom; etc. |
|             | created_at (UTC timestamp)   | System generated creation timestamp                                      |
| memberships | membership_id                | Unique ID                                                                |
|             | team_id                      | Foreign Key                                                              |
|             | role_title (string)          | member or admin                                                          |
|             | joined_at (UTC timestamp)    | System generated creation timestamp                                      |
| events      | event_id                     | Unique ID                                                                |
|             | team_id                      | Foreign Key                                                              |
|             | event_start (UTC timestamp)  | User-defined event start timestamp                                       |
|             | event_end (UTC timestamp)    | User-defined event end timestamp                                         |
|             | latitude (float)             | latitude of event location                                               |
|             | longitude (float)            | longitude of event location                                              |
|             | created_at (UTC timestamp)   | System generated creation timestamp                                      |
| event_rsvps | event_rsvp_id                | Unique ID                                                                |
|             | event_id                     | Foreign Key                                                              |
|             | member_id                    | Foreign Key                                                              |
|             | rsvp_status                  | Enum (0=unanswered; 1=accepted; 2=declined)                              |
|             | responded_at (UTC timestamp) | System generated creation timestamp                                      |

# Requirements

1. ## Data Ingestion

Provide a way to ingest the above data into your chosen data store (assume that the data needs to be extracted from a PostgreSQL database hosted in AWS).

- Show how you handle foreign keys, data types, timestamps, and any malformed data.
- Provide clear setup instructions or scripts so others can replicate your ingestion process and verify that the data has been successfully loaded.
- You do not need to deploy a real cloud service; a local simulation is fine. Show us your approach.

2. ## Data Modelling

Create a data model (tables, views, or equivalent) that will support common analytical patterns. Your model should easily support use-cases listed below. You are not expected to perform these queries, but rather describe how your design is enabling these analyses.

**Analytics Requirements**

- **Daily active teams:** How many distinct teams hosted or updated events each day?
- **RSVP summary:** For each event, indicate how many members responded as accepted, how many responded as declined, and how many did not respond at any given day.
- **Attendance rate:** Over the last 30 days, what’s the average percentage of “Accepted” RSVPs compared to total invites sent?
- **New vs. returning members:** How many new members joined each week, and how many were returning (already joined in a previous week)?
- **Events hosted per region:** How many events were hosted per region (Fylke for Norway, State for the U.S., etc.)?

## Final result should consist of:

- Source code with instructions on how to run it in a Git repository we can access (Github, Bitbucket etc.).
- Extra points for highlighting any identifiable data quality issues, and potential solutions.
- Extra points for test coverage.
- We encourage you to add a description of improvements to your solution that you think would be natural next steps.
