import random
import tkinter as tk

# 🃏 Карты с эликсиром
cards = {
    "Knight": 3, "Archers": 3, "Bomber": 2, "Giant": 5, "Hog Rider": 4, "Wizard": 5, "Musketeer": 4,
    "Mini P.E.K.K.A": 4, "Balloon": 5, "Baby Dragon": 4, "Skeleton Army": 3, "Goblin Barrel": 3,
    "X-bow": 6, "Mortar": 4, "Cannon": 3, "Tesla": 4, "Fire Spirits": 2, "Ice Wizard": 3,
    "Electro Wizard": 4, "Mega Minion": 3, "Royal Giant": 6, "Goblin Gang": 3, "Prince": 5,
    "Dark Prince": 4, "Valkyrie": 4, "Golem": 8, "P.E.K.K.A": 7, "Freeze": 4, "Fireball": 4,
    "Arrows": 3, "Zap": 2, "Poison": 4, "Tornado": 3, "Lightning": 6, "Rage": 2, "Rocket": 6,
}

# 🔥 Особые карты — одна обязана быть выбрана
special_cards = {
    "Повар": 4,
    "Графиня": 5,
    "Канонир": 4,
    "Принцесса": 3
}

# Добавляем специальные карты в общий список
all_cards = {**cards, **special_cards}

def generate_deck():
    main_choice = random.choice(list(special_cards.keys()))        # 1 персонаж обязателен
    remaining_cards = list(all_cards.keys())
    remaining_cards.remove(main_choice)

    deck = [main_choice] + random.sample(remaining_cards, 7)       # 1 обязательная + 7 случайных

    avg_elixir = sum(all_cards[c] for c in deck) / len(deck)       # Средний эликсир
    formatted = "\n".join([f"{c} — {all_cards[c]}💧" for c in deck])

    result_label.config(text=f"{formatted}\n\n⭐ Обязательный персонаж: {main_choice}\n"
                             f"Средний эликсир: {avg_elixir:.1f}💧")

# ---- UI ----
root = tk.Tk()
root.title("Clash Royale Deck Generator")
root.geometry("430x680")
root.config(bg="#111827")

title = tk.Label(root, text="🎮 Clash Royale Deck Generator", font=("Arial", 18, "bold"), bg="#111827", fg="cyan")
title.pack(pady=15)

generate_btn = tk.Button(root, text="Сгенерировать колоду", font=("Arial", 14, "bold"),
                         command=generate_deck, width=25, height=2, bg="#00ffbf")
generate_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#111827", fg="white", justify="center")
result_label.pack(pady=10)

root.mainloop()
