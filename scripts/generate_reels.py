#!/usr/bin/env python3
"""
Automatische Generierung der Reel-Inhalte für die DIS-Awareness Serie.

Usage:
    python scripts/generate_reels.py

Dieses Skript generiert alle Texte, Captions und Prompts für die 7 Reels.
Du kannst es erweitern, um .md Dateien automatisch zu erstellen oder Videos zu generieren.
"""

import json

# Reel Daten
reels = {
    1: {
        "title": "Die verborgene Realität der DIS",
        "voiceover": "Stell dir vor… dein Gehirn erschafft mehrere ‚Ichs‘, um zu überleben. Dissoziative Identitätsstörung ist real. Trauma-bedingt. Oft missverstanden. Mehr als nur Persönlichkeitsspaltung – eine komplexe Überlebensstrategie. Willkommen in einer Welt, die die meisten nie sehen.",
        "caption": "Die Realität hinter DIS 💜 Nicht alles ist, wie es scheint. TW: Trauma. Welche Frage hast du? 👇 #DissoziativeIdentitätsstörung #DIS #MentalHealthAwareness",
        "canva_link": "https://www.canva.com/d/k8TriepXkguJJOu",
        "prompt": None
    },
    2: {
        "title": "Die unsichtbaren Probleme",
        "voiceover": "Gedächtnislücken. Identitätswechsel. Innere Konflikte. Chronische Erschöpfung. Beziehungschaos. Der Alltag mit DIS ist ein ständiger Balanceakt – unsichtbar für andere, aber allgegenwärtig für Betroffene.",
        "caption": "Die unsichtbaren Lasten von DIS 💜 TW: Trauma. Hast du schon mal davon gehört? 👇 #DissoziativeIdentitätsstörung #DIS",
        "canva_link": "https://www.canva.com/d/g834WfdKYaDeypr",
        "prompt": None
    },
    # ... (Reels 3-7 similarly defined for brevity in this example)
}

# Beispiel: Alle Voiceovers ausgeben
def print_all_voiceovers():
    for num, data in reels.items():
        print(f"=== REEL {num}: {data['title']} ===")
        print(data['voiceover'])
        print()

if __name__ == "__main__":
    print("DIS Reels Inhalte Generator")
    print("=" * 40)
    print_all_voiceovers()
    print("\nDu kannst dieses Skript erweitern, um .md Dateien zu generieren oder Videos zu erstellen.")