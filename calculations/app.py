from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict, List

from flask import Flask, render_template_string, request

teams = [
    {
        'id': 'ARI',
        'name': 'Arizona Cardinals',
        'abbreviation': 'ARI',
        'conference': 'NFC',
        'division': 'West',
        'stadium': 'State Farm Stadium',
        'location': 'Glendale, AZ',
        'primaryColor': '#97233F',
        'secondaryColor': '#000000',
    },
    {
        'id': 'ATL',
        'name': 'Atlanta Falcons',
        'abbreviation': 'ATL',
        'conference': 'NFC',
        'division': 'South',
        'stadium': 'Mercedes-Benz Stadium',
        'location': 'Atlanta, GA',
        'primaryColor': '#A71930',
        'secondaryColor': '#000000',
    },
    {
        'id': 'BAL',
        'name': 'Baltimore Ravens',
        'abbreviation': 'BAL',
        'conference': 'AFC',
        'division': 'North',
        'stadium': 'M&T Bank Stadium',
        'location': 'Baltimore, MD',
        'primaryColor': '#241773',
        'secondaryColor': '#000000',
    },
    {
        'id': 'BUF',
        'name': 'Buffalo Bills',
        'abbreviation': 'BUF',
        'conference': 'AFC',
        'division': 'East',
        'stadium': 'Highmark Stadium',
        'location': 'Orchard Park, NY',
        'primaryColor': '#00338D',
        'secondaryColor': '#C60C30',
    },
    {
        'id': 'CAR',
        'name': 'Carolina Panthers',
        'abbreviation': 'CAR',
        'conference': 'NFC',
        'division': 'South',
        'stadium': 'Bank of America Stadium',
        'location': 'Charlotte, NC',
        'primaryColor': '#0085CA',
        'secondaryColor': '#101820',
    },
    {
        'id': 'CHI',
        'name': 'Chicago Bears',
        'abbreviation': 'CHI',
        'conference': 'NFC',
        'division': 'North',
        'stadium': 'Soldier Field',
        'location': 'Chicago, IL',
        'primaryColor': '#0B162A',
        'secondaryColor': '#C83803',
    },
    {
        'id': 'CIN',
        'name': 'Cincinnati Bengals',
        'abbreviation': 'CIN',
        'conference': 'AFC',
        'division': 'North',
        'stadium': 'Paycor Stadium',
        'location': 'Cincinnati, OH',
        'primaryColor': '#FB4F14',
        'secondaryColor': '#000000',
    },
    {
        'id': 'CLE',
        'name': 'Cleveland Browns',
        'abbreviation': 'CLE',
        'conference': 'AFC',
        'division': 'North',
        'stadium': 'Cleveland Browns Stadium',
        'location': 'Cleveland, OH',
        'primaryColor': '#FF3C00',
        'secondaryColor': '#311D00',
    },
    {
        'id': 'DAL',
        'name': 'Dallas Cowboys',
        'abbreviation': 'DAL',
        'conference': 'NFC',
        'division': 'East',
        'stadium': 'AT&T Stadium',
        'location': 'Arlington, TX',
        'primaryColor': '#041E42',
        'secondaryColor': '#869397',
    },
    {
        'id': 'DEN',
        'name': 'Denver Broncos',
        'abbreviation': 'DEN',
        'conference': 'AFC',
        'division': 'West',
        'stadium': 'Empower Field at Mile High',
        'location': 'Denver, CO',
        'primaryColor': '#FB4F14',
        'secondaryColor': '#002244',
    },
    {
        'id': 'DET',
        'name': 'Detroit Lions',
        'abbreviation': 'DET',
        'conference': 'NFC',
        'division': 'North',
        'stadium': 'Ford Field',
        'location': 'Detroit, MI',
        'primaryColor': '#0076B6',
        'secondaryColor': '#B0B7BC',
    },
    {
        'id': 'GB',
        'name': 'Green Bay Packers',
        'abbreviation': 'GB',
        'conference': 'NFC',
        'division': 'North',
        'stadium': 'Lambeau Field',
        'location': 'Green Bay, WI',
        'primaryColor': '#203731',
        'secondaryColor': '#FFB612',
    },
    {
        'id': 'HOU',
        'name': 'Houston Texans',
        'abbreviation': 'HOU',
        'conference': 'AFC',
        'division': 'South',
        'stadium': 'NRG Stadium',
        'location': 'Houston, TX',
        'primaryColor': '#03202F',
        'secondaryColor': '#A71930',
    },
    {
        'id': 'IND',
        'name': 'Indianapolis Colts',
        'abbreviation': 'IND',
        'conference': 'AFC',
        'division': 'South',
        'stadium': 'Lucas Oil Stadium',
        'location': 'Indianapolis, IN',
        'primaryColor': '#002C5F',
        'secondaryColor': '#A2AAAD',
    },
    {
        'id': 'JAX',
        'name': 'Jacksonville Jaguars',
        'abbreviation': 'JAX',
        'conference': 'AFC',
        'division': 'South',
        'stadium': 'EverBank Stadium',
        'location': 'Jacksonville, FL',
        'primaryColor': '#006778',
        'secondaryColor': '#D7A22A',
    },
    {
        'id': 'KC',
        'name': 'Kansas City Chiefs',
        'abbreviation': 'KC',
        'conference': 'AFC',
        'division': 'West',
        'stadium': 'GEHA Field at Arrowhead Stadium',
        'location': 'Kansas City, MO',
        'primaryColor': '#E31837',
        'secondaryColor': '#FFB81C',
    },
    {
        'id': 'LV',
        'name': 'Las Vegas Raiders',
        'abbreviation': 'LV',
        'conference': 'AFC',
        'division': 'West',
        'stadium': 'Allegiant Stadium',
        'location': 'Las Vegas, NV',
        'primaryColor': '#000000',
        'secondaryColor': '#A5ACAF',
    },
    {
        'id': 'LAC',
        'name': 'Los Angeles Chargers',
        'abbreviation': 'LAC',
        'conference': 'AFC',
        'division': 'West',
        'stadium': 'SoFi Stadium',
        'location': 'Inglewood, CA',
        'primaryColor': '#0080C6',
        'secondaryColor': '#FFC20E',
    },
    {
        'id': 'LAR',
        'name': 'Los Angeles Rams',
        'abbreviation': 'LAR',
        'conference': 'NFC',
        'division': 'West',
        'stadium': 'SoFi Stadium',
        'location': 'Inglewood, CA',
        'primaryColor': '#003594',
        'secondaryColor': '#FFA300',
    },
    {
        'id': 'MIA',
        'name': 'Miami Dolphins',
        'abbreviation': 'MIA',
        'conference': 'AFC',
        'division': 'East',
        'stadium': 'Hard Rock Stadium',
        'location': 'Miami Gardens, FL',
        'primaryColor': '#008E97',
        'secondaryColor': '#F26A24',
    },
    {
        'id': 'MIN',
        'name': 'Minnesota Vikings',
        'abbreviation': 'MIN',
        'conference': 'NFC',
        'division': 'North',
        'stadium': 'U.S. Bank Stadium',
        'location': 'Minneapolis, MN',
        'primaryColor': '#4F2683',
        'secondaryColor': '#FFC62F',
    },
    {
        'id': 'NE',
        'name': 'New England Patriots',
        'abbreviation': 'NE',
        'conference': 'AFC',
        'division': 'East',
        'stadium': 'Gillette Stadium',
        'location': 'Foxborough, MA',
        'primaryColor': '#002244',
        'secondaryColor': '#C60C30',
    },
    {
        'id': 'NO',
        'name': 'New Orleans Saints',
        'abbreviation': 'NO',
        'conference': 'NFC',
        'division': 'South',
        'stadium': 'Caesars Superdome',
        'location': 'New Orleans, LA',
        'primaryColor': '#D3BC8D',
        'secondaryColor': '#101820',
    },
    {
        'id': 'NYG',
        'name': 'New York Giants',
        'abbreviation': 'NYG',
        'conference': 'NFC',
        'division': 'East',
        'stadium': 'MetLife Stadium',
        'location': 'East Rutherford, NJ',
        'primaryColor': '#0B2265',
        'secondaryColor': '#A71930',
    },
    {
        'id': 'NYJ',
        'name': 'New York Jets',
        'abbreviation': 'NYJ',
        'conference': 'AFC',
        'division': 'East',
        'stadium': 'MetLife Stadium',
        'location': 'East Rutherford, NJ',
        'primaryColor': '#125740',
        'secondaryColor': '#FFFFFF',
    },
    {
        'id': 'PHI',
        'name': 'Philadelphia Eagles',
        'abbreviation': 'PHI',
        'conference': 'NFC',
        'division': 'East',
        'stadium': 'Lincoln Financial Field',
        'location': 'Philadelphia, PA',
        'primaryColor': '#004C54',
        'secondaryColor': '#A5ACAF',
    },
    {
        'id': 'PIT',
        'name': 'Pittsburgh Steelers',
        'abbreviation': 'PIT',
        'conference': 'AFC',
        'division': 'North',
        'stadium': 'Acrisure Stadium',
        'location': 'Pittsburgh, PA',
        'primaryColor': '#FFB612',
        'secondaryColor': '#101820',
    },
    {
        'id': 'SF',
        'name': 'San Francisco 49ers',
        'abbreviation': 'SF',
        'conference': 'NFC',
        'division': 'West',
        'stadium': "Levi's Stadium",
        'location': 'Santa Clara, CA',
        'primaryColor': '#AA0000',
        'secondaryColor': '#B3995D',
    },
    {
        'id': 'SEA',
        'name': 'Seattle Seahawks',
        'abbreviation': 'SEA',
        'conference': 'NFC',
        'division': 'West',
        'stadium': 'Lumen Field',
        'location': 'Seattle, WA',
        'primaryColor': '#002244',
        'secondaryColor': '#69BE28',
    },
    {
        'id': 'TB',
        'name': 'Tampa Bay Buccaneers',
        'abbreviation': 'TB',
        'conference': 'NFC',
        'division': 'South',
        'stadium': 'Raymond James Stadium',
        'location': 'Tampa, FL',
        'primaryColor': '#D50A0A',
        'secondaryColor': '#34302B',
    },
    {
        'id': 'TEN',
        'name': 'Tennessee Titans',
        'abbreviation': 'TEN',
        'conference': 'AFC',
        'division': 'South',
        'stadium': 'Nissan Stadium',
        'location': 'Nashville, TN',
        'primaryColor': '#4B92DB',
        'secondaryColor': '#0C2340',
    },
    {
        'id': 'WAS',
        'name': 'Washington Commanders',
        'abbreviation': 'WAS',
        'conference': 'NFC',
        'division': 'East',
        'stadium': 'Commanders Field',
        'location': 'Landover, MD',
        'primaryColor': '#5A1414',
        'secondaryColor': '#FFB612',
    },
]

KICKOFF_WINDOWS = [
    "1:00 PM ET",
    "4:05 PM ET",
    "4:25 PM ET",
    "8:20 PM ET",
    "8:15 PM ET",
]

NETWORKS = [
    "CBS",
    "FOX",
    "NBC",
    "ESPN",
    "Prime Video",
]

BASE_DATE = datetime(2025, 9, 7, 13, 0)

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>2025 NFL Schedule Explorer</title>
    <style>
        :root {
            color-scheme: light dark;
        }
        body {
            font-family: \"Segoe UI\", system-ui, -apple-system, sans-serif;
            margin: 0;
            padding: 0;
            background: #0c1622;
            color: #f1f5f9;
        }
        header,
        footer {
            padding: 1.5rem 1rem;
            text-align: center;
            background: #111c2b;
        }
        main {
            max-width: 960px;
            margin: 0 auto;
            padding: 2rem 1rem 3rem;
        }
        h1 {
            margin-bottom: 0.5rem;
        }
        .card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 18px 60px rgba(15, 23, 42, 0.35);
            backdrop-filter: blur(12px);
        }
        form {
            display: grid;
            gap: 1rem;
        }
        label {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            font-weight: 600;
            text-align: left;
        }
        select,
        button {
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.35);
            padding: 0.75rem 1.25rem;
            font-size: 1rem;
            font-weight: 600;
        }
        select {
            background: rgba(15, 23, 42, 0.8);
            color: inherit;
        }
        button {
            justify-self: start;
            background: linear-gradient(135deg, #22d3ee, #818cf8);
            color: #0f172a;
            border: none;
            cursor: pointer;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        button:hover,
        button:focus {
            transform: translateY(-1px);
            box-shadow: 0 12px 24px rgba(129, 140, 248, 0.35);
            outline: none;
        }
        .schedule-card {
            margin-top: 2rem;
            display: grid;
            gap: 1.25rem;
        }
        .team-meta {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .team-swatch {
            width: 64px;
            height: 64px;
            border-radius: 18px;
            border: 1px solid rgba(15, 23, 42, 0.6);
            box-shadow: inset 0 0 0 1px rgba(15, 23, 42, 0.45);
        }
        .team-meta h2 {
            margin: 0;
            font-size: 1.8rem;
        }
        .team-meta p {
            margin: 0.25rem 0 0;
            color: rgba(226, 232, 240, 0.75);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            overflow: hidden;
            border-radius: 12px;
            background: rgba(15, 23, 42, 0.65);
        }
        thead {
            background: rgba(148, 163, 184, 0.12);
        }
        th,
        td {
            padding: 0.85rem 1rem;
            text-align: left;
        }
        tbody tr:nth-child(odd) {
            background: rgba(15, 23, 42, 0.45);
        }
        tbody tr.primetime {
            background: linear-gradient(135deg, rgba(234, 179, 8, 0.18), rgba(59, 130, 246, 0.18));
        }
        tbody tr.primetime td {
            border-bottom: 1px solid rgba(250, 204, 21, 0.35);
        }
        tbody tr + tr td {
            border-top: 1px solid rgba(148, 163, 184, 0.08);
        }
        caption {
            text-align: left;
            padding: 0 0 0.75rem;
            font-weight: 600;
            color: rgba(226, 232, 240, 0.75);
        }
        @media (max-width: 640px) {
            table,
            thead,
            tbody,
            th,
            td,
            tr {
                display: block;
            }
            thead {
                display: none;
            }
            tbody tr {
                margin-bottom: 1rem;
                border: 1px solid rgba(148, 163, 184, 0.15);
                border-radius: 12px;
                overflow: hidden;
            }
            tbody tr td {
                display: flex;
                justify-content: space-between;
                padding: 0.75rem 0.85rem;
                border: none;
            }
            tbody tr td::before {
                content: attr(data-label);
                font-weight: 600;
                color: rgba(226, 232, 240, 0.75);
            }
            tbody tr td:last-child {
                border-bottom: none;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>2025 NFL Schedule Explorer</h1>
        <p>Select a franchise to view its mock 2025 slate.</p>
    </header>
    <main>
        <section class=\"card\" aria-labelledby=\"team-select-label\">
            <form method=\"get\">
                <label id=\"team-select-label\" for=\"team\">
                    NFL Team
                    <select id=\"team\" name=\"team\" required>
                        <option value=\"\" disabled {{ '' == selected_id and 'selected' or '' }}>Pick a team…</option>
                        {% for team in teams %}
                        <option value=\"{{ team.id }}\" {{ 'selected' if team.id == selected_id else '' }}>
                            {{ team.name }} ({{ team.abbreviation }})
                        </option>
                        {% endfor %}
                    </select>
                </label>
                <button type=\"submit\">View schedule</button>
                <p style=\"margin:0;color:rgba(226,232,240,0.65);\">
                    Update the data in <code>app.py</code> when the official schedule is published.
                </p>
            </form>
        </section>

        {% if selected_team %}
        <section class=\"card schedule-card\" aria-live=\"polite\">
            <div class=\"team-meta\">
                <div class=\"team-swatch\" style=\"background: linear-gradient(135deg, {{ selected_team.primaryColor }}, {{ selected_team.secondaryColor }});\"></div>
                <div>
                    <h2>{{ selected_team.name }} 2025 Schedule</h2>
                    <p>{{ selected_team.conference }} {{ selected_team.division }} • Home games at {{ selected_team.stadium }} ({{ selected_team.location }})</p>
                </div>
            </div>
            <table>
                <caption>Mock matchup rotation generated for planning purposes.</caption>
                <thead>
                    <tr>
                        <th scope=\"col\">Week</th>
                        <th scope=\"col\">Date</th>
                        <th scope=\"col\">Opponent</th>
                        <th scope=\"col\">Location</th>
                        <th scope=\"col\">Kickoff</th>
                        <th scope=\"col\">Network</th>
                    </tr>
                </thead>
                <tbody>
                    {% for game in schedule %}
                    <tr class=\"{{ 'primetime' if game.is_primetime else '' }}\">
                        <td data-label=\"Week\">{{ game.week }}</td>
                        <td data-label=\"Date\">{{ game.date }}</td>
                        <td data-label=\"Opponent\">{{ game.venue_prefix }} {{ game.opponent_name }}</td>
                        <td data-label=\"Location\">{{ game.location }}</td>
                        <td data-label=\"Kickoff\">{{ game.time }}</td>
                        <td data-label=\"Network\">{{ game.network }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </section>
        {% else %}
        <section class=\"card schedule-card\" aria-live=\"polite\">
            <p style=\"margin:0; color: rgba(226,232,240,0.75);\">Choose a team to see its 2025 matchups.</p>
        </section>
        {% endif %}
    </main>
    <footer>
        <p>Mock data provided for exploration only.</p>
    </footer>
</body>
</html>
"""


def format_date(date: datetime) -> str:
    return f"{date.strftime('%a, %b')} {date.day}"


def build_schedules(data: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    schedules: Dict[str, List[Dict[str, str]]] = {}

    for team_index, team in enumerate(data):
        games: List[Dict[str, str]] = []
        offset = 1

        while len(games) < 17:
            opponent_index = (team_index + offset) % len(data)

            if opponent_index == team_index:
                offset += 1
                continue

            opponent = data[opponent_index]
            week = len(games) + 1
            is_home = week % 2 == 1
            date = BASE_DATE + timedelta(days=7 * (week - 1))
            time = KICKOFF_WINDOWS[(week + team_index) % len(KICKOFF_WINDOWS)]
            network = NETWORKS[(week + opponent_index) % len(NETWORKS)]
            location = (
                f"{team['stadium']} ({team['location']})"
                if is_home
                else f"{opponent['stadium']} ({opponent['location']})"
            )

            games.append(
                {
                    "week": week,
                    "date": format_date(date),
                    "opponent_name": opponent["name"],
                    "venue_prefix": "vs." if is_home else "@",
                    "location": location,
                    "time": time,
                    "network": network,
                    "is_primetime": time.startswith("8:"),
                }
            )

            offset += 1

        schedules[team["id"]] = games

    return schedules


schedule_by_team = build_schedules(teams)
sorted_teams = sorted(teams, key=lambda team: team["name"])


@app.get("/")
def index():
    team_id = request.args.get("team", "")
    selected_team = next((team for team in sorted_teams if team["id"] == team_id), None)
    schedule = schedule_by_team.get(team_id, []) if selected_team else []

    return render_template_string(
        HTML_TEMPLATE,
        teams=sorted_teams,
        selected_team=selected_team,
        selected_id=team_id,
        schedule=schedule,
    )


if __name__ == "__main__":
    app.run(debug=True)
