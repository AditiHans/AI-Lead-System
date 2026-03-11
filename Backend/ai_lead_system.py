import requests
import pandas as pd
from ddgs import DDGS
from urllib.parse import urlparse
import sqlite3

requests.packages.urllib3.disable_warnings()

# ===============================
# DATABASE (SQLITE FOR RENDER)
# ===============================

DB_FILE = "database.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS seen_merchants (
            canonical TEXT PRIMARY KEY
        )
    """)

    conn.commit()
    conn.close()


def load_seen_domains():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT canonical FROM seen_merchants")
    rows = cur.fetchall()

    conn.close()

    return set([r[0] for r in rows])


def save_seen_domains(domains):

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    for d in domains:
        try:
            cur.execute(
                "INSERT OR IGNORE INTO seen_merchants (canonical) VALUES (?)",
                (d,)
            )
        except:
            pass

    conn.commit()
    conn.close()


# ===============================
# DESIGNER SEED MERCHANTS
# ===============================

DESIGNER_SEEDS = [
    "shantanu & nikhil",
    "dhruv kapoor",
    "abraham & thakore",
    "rajesh pratap singh",
    "rohit gandhi rahul khanna",
    "wendell rodricks",
    "anju modi",
    "tarun tahiliani",
    "anamika khanna",
    "jayanti reddy",
    "eka",
    "pero",
    "suket dhir",
    "bodice"
]

# ===============================
# SEGMENTS
# ===============================

SEGMENTS = {

    "travel": {
        "queries": [
            "Indian destination management company international clients",
            "Indian tour operator inbound travel India",
            "India holidays tour company overseas customers"
        ],
        "keywords": [
            "tour packages", "holiday packages",
            "custom itinerary", "inbound travel",
            "destination management", "bespoke travel"
        ],
        "negatives": [
            "visa consultancy",
            "blog",
            "news"
        ]
    },

    "edtech": {
        "queries": [
            "Indian online learning platform international students",
            "Indian edtech company global learners"
        ],
        "keywords": [
            "online class",
            "course",
            "learning",
            "certification"
        ],
        "negatives": [
            "jobs",
            "media",
            "review"
        ]
    },

    "ecommerce": {
        "queries": [
            "Indian designer fashion brand international shipping",
            "Indian luxury ethnic wear designer global customers"
        ],
        "keywords": [
            "designer wear",
            "luxury fashion",
            "lehenga",
            "saree",
            "shop online"
        ],
        "negatives": [
            "marketplace",
            "directory"
        ]
    }
}


# ===============================
# DOMAIN CLEANING
# ===============================

def canonical_domain(url):

    netloc = urlparse(url).netloc.lower()
    netloc = netloc.replace("www.", "")

    parts = netloc.split(".")

    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return netloc


# ===============================
# FETCH TEXT
# ===============================

def fetch_text(url):

    try:
        return requests.get(url, timeout=3).text[:200000].lower()
    except:
        return ""


# ===============================
# SIGNALS
# ===============================

INTL_PAYMENT_PHRASES = ["$", "usd", "eur", "gbp", "international"]

def indian_signal(domain, text):

    score = 0

    if domain.endswith((".in", ".co.in")):
        score += 30

    if "+91" in text or "india" in text:
        score += 20

    if "gst" in text:
        score += 20

    return score


def international_signal(text):

    return min(sum(k in text for k in INTL_PAYMENT_PHRASES) * 15, 60)


def segment_signal(config, text):

    score = 0

    for k in config["keywords"]:
        if k in text:
            score += 6

    return min(score, 40)


# ===============================
# DISCOVERY ENGINE
# ===============================

def discover_leads(segment="travel"):

    config = SEGMENTS[segment]

    rows = []

    with DDGS(verify=False) as ddgs:

        for query in config["queries"]:

            for r in ddgs.text(query, region="in-en", max_results=6):

                url = r.get("href")

                if url:

                    domain = canonical_domain(url)

                    rows.append({
                        "domain": domain,
                        "website": url
                    })

    df = pd.DataFrame(rows).drop_duplicates()

    return df


# ===============================
# LEAD PIPELINE
# ===============================

def run_pipeline(segment="travel"):

    init_db()

    df = discover_leads(segment)

    seen = load_seen_domains()

    df = df[~df["domain"].isin(seen)]

    if df.empty:
        return []

    config = SEGMENTS[segment]

    df["text"] = df["website"].apply(fetch_text)

    df["indian_score"] = df.apply(
        lambda r: indian_signal(r["domain"], r["text"]), axis=1
    )

    df["intl_score"] = df["text"].apply(international_signal)

    df["segment_score"] = df["text"].apply(
        lambda t: segment_signal(config, t)
    )

    df["priority_score"] = (
        df["indian_score"] +
        df["intl_score"] +
        df["segment_score"]
    )

    df = df.sort_values("priority_score", ascending=False)

    save_seen_domains(set(df["domain"]))

    return df[["domain", "website", "priority_score"]].to_dict(orient="records")