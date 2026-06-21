# story_data.py

GRAPH = {
    "Primary_School_Graduation": {
        "connections": [
            {"edge": "Akari Move to Tochigi", "target": "Akari at Tochigi", "c": 15, "p": 1.0}
        ]
    },
    "Akari at Tochigi": {
        "connections": [
            {"edge": "Contact with Letter Writing", "target": "Junior_High_Contact", "c": 10, "p": 0.5},
            {"edge": "No Letter Writing", "target": "Early_Drift", "c": 5, "p": 0.5}
        ]
    },
    "Early_Drift": {
        "connections": [
            {"edge": "Move to Kagoshima", "target": "Kagoshima_Arrival_Detached", "c": 30, "p": 1.0}
        ]
    },
    "Junior_High_Contact": {
        "connections": [
            {"edge": "Punctual Train", "target": "Station_Meetup_On_Time", "c": 10, "p": 0.7},
            {"edge": "Snowstorm Train Delay", "target": "Station_Meetup_Delayed", "c": 80, "p": 0.3}
        ]
    },
    "Station_Meetup_On_Time": {
        "connections": [
            {"edge": "Exchange Vows and Feelings", "target": "High_School_Long_Distance_Contact", "c": 5, "p": 1.0}
        ]
    },
    "High_School_Long_Distance_Contact": {
        "connections": [
            {"edge": "Move to Kagoshima", "target": "Kagoshima_Arrival_Hopeful", "c": 30, "p": 1.0}
        ]
    },
    "Station_Meetup_Delayed": {
        "connections": [
            {"edge": "Move to Kagoshima", "target": "Kagoshima_Arrival_Sad", "c": 30, "p": 1.0}
        ]
    },
    "Kagoshima_Arrival_Sad": {
        "connections": [
            {"edge": "Stop Letter Writing and Grow Distant", "target": "Unhealthy_Akari_Fixation", "c": 50, "p": 0.8},
            {"edge": "Long Distance Reach Out Effort", "target": "Kagoshima_Arrival_Hopeful", "c": 40, "p": 0.2}
        ]
    },
    "Kagoshima_Arrival_Hopeful": {
        "connections": [
            {"edge": "Stay in Contact while Growing Up", "target": "Adult_Reunion", "c": 30, "p": 0.4},
            {"edge": "Fading Communication due to Time", "target": "Unhealthy_Akari_Fixation", "c": 25, "p": 0.6}
        ]
    },
    "Unhealthy_Akari_Fixation": {
        "connections": [
            {"edge": "Stay Emotionally Stuck", "target": "Depressed_Adult_Life", "c": 60, "p": 0.7},
            {"edge": "Break Out of Isolation", "target": "High_School_Present_Awareness", "c": 30, "p": 0.3}
        ]
    },
    "Kagoshima_Arrival_Detached": {
        "connections": [
            {"edge": "Openness to Present Reality", "target": "High_School_Present_Awareness", "c": 15, "p": 0.4},
            {"edge": "Be Stuck on Akari", "target": "High_School_Isolation", "c": 20, "p": 0.6}
        ]
    },
    "High_School_Isolation": {
        "connections": [
            {"edge": "Awakening to Present", "target": "High_School_Present_Awareness", "c": 15, "p": 0.8},
            {"edge": "Stay Emotionally Stuck", "target": "Melancholic_Adult_Life", "c": 20, "p": 0.2}
        ]
    },
    "High_School_Present_Awareness": {
        "connections": [
            {"edge": "Commit to the Present", "target": "Happier_Adult_Life", "c": 5, "p": 1.0}
        ]
    },
    "Adult_Reunion": {
        "connections": [
            {"edge": "Rebuild Life with Akari", "target": "Happy_Adult_Life_with_Akari", "c": 15, "p": 0.5},
            {"edge": "Grew Different despite Reunion", "target": "Bittersweet_Adult_Closure", "c": 20, "p": 0.5}
        ]
    },
    "Bittersweet_Adult_Closure": {
        "connections": [
            {"edge": "Accepting Change", "target": "Adult_Acceptance_Resolution", "c": 10, "p": 1.0}
        ]
    },
    "Depressed_Adult_Life": {
        "connections": [
            {"edge": "Crossroads Realization/Will to Change", "target": "Adult_Acceptance_Resolution", "c": 15, "p": 0.2},
            {"edge": "Overwork and Refuse to Change", "target": "Depressed_Adult_Life", "c": 50, "p": 0.8}
        ]
    },
    
    "Happy_Adult_Life_with_Akari": {"connections": []},
    "Adult_Acceptance_Resolution": {"connections": []},
    "Happier_Adult_Life": {"connections": []},
    "Melancholic_Adult_Life": {"connections": []}
}