from flask import Flask, render_template, jsonify

app = Flask(__name__)

fighters = [
    {
        "id": 1,
        "name": "Marcus 'The Predator' Steel",
        "record": "24-2-0",
        "weight_class": "Heavyweight",
        "nationality": "🇺🇸 USA",
        "rank": "#1",
        "specialty": "Muay Thai / Wrestling",
        "image_placeholder": "MS",
        "accent": "#e63946"
    },
    {
        "id": 2,
        "name": "Jin 'Shadow' Nakamura",
        "record": "19-1-0",
        "weight_class": "Lightweight",
        "nationality": "🇯🇵 Japan",
        "rank": "#2",
        "specialty": "Brazilian Jiu-Jitsu",
        "image_placeholder": "JN",
        "accent": "#f4a261"
    },
    {
        "id": 3,
        "name": "Carlos 'El Toro' Reyes",
        "record": "21-3-1",
        "weight_class": "Welterweight",
        "nationality": "🇲🇽 Mexico",
        "rank": "#3",
        "specialty": "Boxing / Kickboxing",
        "image_placeholder": "CR",
        "accent": "#2a9d8f"
    },
]

events = [
    {
        "id": 1,
        "title": "APEX COMBAT 47",
        "subtitle": "Steel vs. Nakamura II",
        "date": "JUNE 14, 2026",
        "venue": "Madison Square Garden",
        "location": "New York, USA",
        "status": "UPCOMING",
        "main_event": "Heavyweight Championship",
        "tickets": "$89 – $2,500"
    },
    {
        "id": 2,
        "title": "IRON NIGHT 12",
        "subtitle": "Reyes vs. Thompson",
        "date": "JULY 5, 2026",
        "venue": "O2 Arena",
        "location": "London, UK",
        "status": "UPCOMING",
        "main_event": "Welterweight Contender Bout",
        "tickets": "$65 – $1,800"
    },
    {
        "id": 3,
        "title": "APEX COMBAT 46",
        "subtitle": "Ramos vs. Lee",
        "date": "MAY 10, 2026",
        "venue": "T-Mobile Arena",
        "location": "Las Vegas, USA",
        "status": "COMPLETED",
        "main_event": "Middleweight Title Defense",
        "tickets": "Event Ended"
    },
]

news = [
    {
        "category": "BREAKING",
        "headline": "Steel Signs Historic $50M Multi-Fight Deal",
        "summary": "Marcus Steel inks the largest contract in Apex Combat history, setting the stage for three blockbuster heavyweight title defenses.",
        "date": "May 27, 2026",
        "read_time": "3 min read"
    },
    {
        "category": "TRAINING",
        "headline": "Nakamura's New Camp Reveals Revolutionary BJJ System",
        "summary": "Exclusive footage from Shadow's training camp shows a groundbreaking submission system developed with world-renowned coach Hélio Gracie Jr.",
        "date": "May 25, 2026",
        "read_time": "5 min read"
    },
    {
        "category": "RANKINGS",
        "headline": "Updated P4P Rankings: Reyes Climbs to Top 5",
        "summary": "Following his stunning first-round KO of former champion Diaz, El Toro earns his highest pound-for-pound ranking ever.",
        "date": "May 22, 2026",
        "read_time": "2 min read"
    },
]

stats = [
    {"label": "Active Fighters", "value": "487"},
    {"label": "Events Worldwide", "value": "1,200+"},
    {"label": "Countries", "value": "63"},
    {"label": "Years of Combat", "value": "18"},
]

@app.route('/')
def index():
    return render_template('index.html', fighters=fighters, events=events, news=news, stats=stats)

@app.route('/api/fighters')
def api_fighters():
    return jsonify(fighters)

@app.route('/api/events')
def api_events():
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
