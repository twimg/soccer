import random

# 各能力の重みを使って総合値を計算
def calculate_overall(stats: dict) -> int:
    """能力辞書から総合値を計算"""
    weights = {
        'speed': 1.0,
        'pass': 1.0,
        'shoot': 1.1,
        'power': 1.1,
        'stamina': 1.0,
        'defense': 1.0,
        'technique': 1.1,
        'mental': 1.0
    }
    total = sum(stats[k] * weights.get(k, 1.0) for k in stats)
    return int(total / sum(weights.values()))

# レーダーチャート用のデータを整形
def get_radar_data(player: dict) -> dict:
    """選手辞書からレーダーチャート用データを作成"""
    return {
        "Speed": player.get("speed", 0),
        "Pass": player.get("pass", 0),
        "Shoot": player.get("shoot", 0),
        "Power": player.get("power", 0),
        "Stamina": player.get("stamina", 0),
        "Defense": player.get("defense", 0),
        "Technique": player.get("technique", 0),
        "Mental": player.get("mental", 0),
    }

# 国籍に応じた国旗画像パスを取得
def get_flag_image(nationality: str) -> str:
    """国籍に対応する国旗画像のファイルパスを返す"""
    flag_paths = {
        "日本": "flags/japan.png",
        "イングランド": "flags/england.png",
        "ドイツ": "flags/germany.png",
        "スペイン": "flags/spain.png",
        "フランス": "flags/france.png",
        "ブラジル": "flags/brazil.png",
        "アルゼンチン": "flags/argentina.png",
    }
    return flag_paths.get(nationality, "flags/default.png")

# 試合スケジュール（総当たり）の自動生成
def generate_league_schedule(teams: list) -> list:
    """チーム名リストから総当たりスケジュールを生成"""
    schedule = []
    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            schedule.append((teams[i], teams[j]))
    random.shuffle(schedule)
    return schedule

# 年齢に応じてユースかシニアかを返す
def is_youth(age: int) -> bool:
    """14〜18歳をユース判定"""
    return age < 19

# 年俸を国籍や能力から推定（万円単位）
def estimate_salary(overall: int, nationality: str) -> int:
    base = 300 + overall * 5
    if nationality in ["日本", "韓国", "タイ"]:
        return int(base * 0.8)
    elif nationality in ["ブラジル", "アルゼンチン"]:
        return int(base * 0.9)
    else:
        return int(base)

# スカウト候補を自動生成
def generate_scout_candidates(n: int = 6) -> list:
    """スカウトリストをランダムに生成"""
    names = ["アレックス", "マルコ", "タカシ", "リュウジ", "ジョアン", "パブロ", "カリム", "サンティ", "アミル"]
    nationalities = ["ブラジル", "アルゼンチン", "日本", "ドイツ", "イングランド", "フランス", "スペイン"]
    candidates = []
    for _ in range(n):
        name = random.choice(names)
        nationality = random.choice(nationalities)
        age = random.randint(17, 22)
        stats = {
            "speed": random.randint(50, 85),
            "pass": random.randint(50, 85),
            "shoot": random.randint(50, 85),
            "power": random.randint(50, 85),
            "stamina": random.randint(50, 85),
            "defense": random.randint(50, 85),
            "technique": random.randint(50, 85),
            "mental": random.randint(50, 85),
        }
        overall = calculate_overall(stats)
        candidates.append({
            "name": name,
            "nationality": nationality,
            "age": age,
            "stats": stats,
            "overall": overall,
        })
    return candidates
