import random

# ポジション別・総合評価計算
def calculate_total_score(player):
    """ポジション別で重みづけし、現実的な総合評価を算出"""
    weights = {
        "GK": {"フィジカル":0.2, "ディフェンス":0.4, "メンタル":0.4},
        "DF": {"フィジカル":0.3, "ディフェンス":0.4, "スピード":0.2, "メンタル":0.1},
        "MF": {"パス":0.3, "テクニック":0.3, "スタミナ":0.2, "メンタル":0.2},
        "FW": {"シュート":0.4, "スピード":0.3, "テクニック":0.2, "パワー":0.1}
    }
    pos = player["ポジション"]
    total = 0
    for key, weight in weights.get(pos, {}).items():
        total += player.get(key, 0) * weight
    return int(total)

# スカウト候補の自動生成（定期入れ替え）
def generate_scout_candidates(period, last_update_period, n=6):
    """n人のスカウト候補をperiod（例:3）ごとに自動生成"""
    if period % 3 != 1 and period != last_update_period:
        return None  # まだ更新しない

    names = ["アレックス", "マルコ", "リカルド", "タカシ", "ジョアン", "ミゲル", "ダビド", "ロレンツォ", "レオン", "ソウタ"]
    nationalities = ["ブラジル", "アルゼンチン", "日本", "ドイツ", "イングランド", "フランス", "スペイン", "イタリア"]
    candidates = []
    for _ in range(n):
        name = random.choice(names)
        nationality = random.choice(nationalities)
        age = random.randint(17, 22)
        stats = {
            "スピード": random.randint(50, 85),
            "パス": random.randint(50, 85),
            "フィジカル": random.randint(50, 85),
            "スタミナ": random.randint(50, 85),
            "ディフェンス": random.randint(50, 85),
            "テクニック": random.randint(50, 85),
            "メンタル": random.randint(50, 85),
            "シュート": random.randint(50, 85),
            "パワー": random.randint(50, 85),
        }
        pos = random.choice(["GK", "DF", "MF", "FW"])
        candidate = {
            "名前": name,
            "国籍": nationality,
            "年齢": age,
            "ポジション": pos,
            **stats
        }
        candidate["総合評価"] = calculate_total_score({**candidate, **stats, "ポジション": pos})
        candidates.append(candidate)
    return candidates

# 移籍金計算
def estimate_transfer_fee(player):
    """年齢・能力・潜在値で移籍金を算出（万円単位）"""
    age_factor = max(1, (30 - player["年齢"]) / 10)
    total_score = calculate_total_score(player)
    # 潜在能力を平均化
    potential = 0
    count = 0
    for key in player:
        if key.endswith("_潜在"):
            potential += player[key]
            count += 1
    if count > 0:
        potential = potential / count
    else:
        potential = total_score
    fee = int((total_score + potential) * 2000 * age_factor)
    return fee

# 既存のユーティリティ関数（省略せず統合する場合、前のutils.pyも追記可）
