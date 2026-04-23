# Project 1

**CS178: Cloud and Database Systems — Project #1**
**Author:** [Ezri  Lopez]
**GitHub:** [ChubEzi]

---

## Overview

This project allows for a user to add, delete, update and display entites from a movie database. This website is mainly for people who want to know the genre of the movie.

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for [describe what you stored]
- **AWS DynamoDB** — non-relational database for [describe what you stored]
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page
│   ├── [other].html     # Add descriptions for your other templates
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/ChubEzi/cs178-flask-app.git
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://44.213.104.169:8080
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "cs178-chinook.cn9nbw41gsla.us-east-1.rds.amazonaws.com"
user = "admin"
password = "password"
db = "movies"
```

---

## Database Design

### SQL (MySQL on RDS)

I did not used my own RDS, but Professor's Moore RDS. 

**Example:**

- `[TableName]` — stores [description]; primary key is `[key]`
- `[TableName]` — stores [description]; foreign key links to `[other table]`

The JOIN query used in this project: The Join query of this project is displaying the movie title and the movie genre.

### DynamoDB


- **Table name:** `[movie]`
- **Partition key:** `[Title]`
- **Used for:** `[Shows the top 5 longest run time of the movies]`

---

## CRUD Operations

| Operation | Route      | Description                                  |
| --------- | ---------- | ---------------------------------------------|
| Create    | `/add-movie` | [Adds a movie]                             |
| Read      | `/display-movie` | [sShows movies and the genre]          |
| Update    | `/update-movie` | [updates a movie that is already added] |
| Delete    | `/delete-movie` | [Deletes a movie]                       |

---

## Challenges and Insights

The hardest part of this project was staying organized. There was so many tasked that crossed over with each other that I often lost myself on if I had completed a task already or not.

---

## AI Assistance

I had used chatGPT to find any inconsistances since I was altering the code instead of building it from scratch.
