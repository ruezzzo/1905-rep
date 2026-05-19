"""Мок-данные для дашборда — Инновационный Технический колледж."""
from datetime import datetime, timedelta
import random

random.seed(42)

COLLEGE = "Инновационный Технический колледж"
COMPETITORS = [
    "Технологический колледж №1",
    "Колледж Информатики",
    "Политехнический колледж",
    "Колледж Цифровых Технологий",
]


def _months(n=12):
    today = datetime.today().replace(day=1)
    out = []
    for i in range(n - 1, -1, -1):
        m = today - timedelta(days=30 * i)
        out.append(m.strftime("%b %Y"))
    return out


def get_dashboard_data():
    months = _months(12)

    # Динамика отзывов 2GIS
    pos = [random.randint(40, 90) for _ in months]
    neg = [random.randint(5, 30) for _ in months]
    neu = [random.randint(10, 25) for _ in months]

    # Распределение рейтингов 2GIS
    rating_dist = {
        "5★": 412,
        "4★": 187,
        "3★": 64,
        "2★": 28,
        "1★": 41,
    }
    total = sum(rating_dist.values())
    avg_rating = round(
        sum(int(k[0]) * v for k, v in rating_dist.items()) / total, 2
    )

    # Сравнение с конкурентами
    all_colleges = [COLLEGE] + COMPETITORS
    comparison = []
    for i, c in enumerate(all_colleges):
        comparison.append({
            "name": c,
            "rating": round(random.uniform(3.6, 4.8), 2) if i != 0 else avg_rating,
            "reviews": random.randint(300, 900) if i != 0 else total,
            "followers": random.randint(1500, 9000) if i != 0 else 7820,
            "engagement": round(random.uniform(1.2, 5.6), 2) if i != 0 else 4.1,
        })

    # Темы негативных отзывов
    negative_topics = {
        "Качество преподавания": 38,
        "Расписание": 27,
        "Состояние аудиторий": 21,
        "Бюрократия": 34,
        "Питание": 18,
        "Общежитие": 25,
    }

    # Темы позитивных отзывов
    positive_topics = {
        "Преподаватели": 142,
        "Практика": 118,
        "Современное оборудование": 96,
        "Атмосфера": 87,
        "Трудоустройство": 134,
        "Студенческая жизнь": 73,
    }

    # Instagram метрики
    ig_metrics = {
        "followers": 7820,
        "followers_growth_pct": 4.7,
        "posts_total": 312,
        "avg_likes": 287,
        "avg_comments": 19,
        "engagement_rate": 4.1,
        "reach_30d": 48230,
    }

    # Динамика подписчиков IG
    ig_followers_series = []
    base = 7000
    for m in months:
        base += random.randint(20, 120)
        ig_followers_series.append(base)
    ig_metrics["followers"] = ig_followers_series[-1]

    # Популярные публикации IG
    top_posts = [
        {
            "title": "День открытых дверей — итоги",
            "type": "Reels",
            "likes": 1240,
            "comments": 87,
            "reach": 9820,
            "date": "2025-04-12",
        },
        {
            "title": "Выпускной 2025: лучшие моменты",
            "type": "Carousel",
            "likes": 982,
            "comments": 64,
            "reach": 7110,
            "date": "2025-04-02",
        },
        {
            "title": "Хакатон по робототехнике",
            "type": "Reels",
            "likes": 874,
            "comments": 52,
            "reach": 6540,
            "date": "2025-03-21",
        },
        {
            "title": "Интервью с преподавателем года",
            "type": "Post",
            "likes": 612,
            "comments": 41,
            "reach": 4820,
            "date": "2025-03-08",
        },
        {
            "title": "Новая IT-лаборатория",
            "type": "Carousel",
            "likes": 547,
            "comments": 33,
            "reach": 4210,
            "date": "2025-02-27",
        },
    ]

    # Соотношение типов контента
    content_mix = {"Reels": 42, "Carousel": 28, "Post": 22, "Stories": 58}

    return {
        "college": COLLEGE,
        "competitors": COMPETITORS,
        "months": months,
        "reviews_dynamics": {"positive": pos, "negative": neg, "neutral": neu},
        "rating_distribution": rating_dist,
        "avg_rating": avg_rating,
        "total_reviews": total,
        "comparison": comparison,
        "negative_topics": negative_topics,
        "positive_topics": positive_topics,
        "instagram": ig_metrics,
        "ig_followers_series": ig_followers_series,
        "top_posts": top_posts,
        "content_mix": content_mix,
    }


def get_recommendations(data):
    """Автоматически сформированные выводы и рекомендации."""
    recs = {"instagram": [], "twogis": [], "general": []}

    ig = data["instagram"]
    if ig["engagement_rate"] < 5:
        recs["instagram"].append(
            f"Engagement rate {ig['engagement_rate']}% ниже отраслевой нормы (5–7%). "
            "Увеличить долю Reels и интерактивных Stories (опросы, вопросы)."
        )
    reels = data["content_mix"].get("Reels", 0)
    posts = data["content_mix"].get("Post", 0)
    if reels < posts * 2:
        recs["instagram"].append(
            "Reels приносят в среднем в 3–4 раза больше охвата, чем обычные посты. "
            "Поднять долю Reels минимум до 60% выходящего контента."
        )
    recs["instagram"].append(
        "Сделать постоянные рубрики: «Студент недели», «За кадром у преподавателя», "
        "«История одного выпускника» — это повышает удержание подписчиков."
    )
    recs["instagram"].append(
        "Анализ топ-публикаций показывает: события (день открытых дверей, хакатоны, "
        "выпускной) дают в 2–3 раза больше реакций — планировать минимум 2 ивент-публикации в месяц."
    )

    neg = data["negative_topics"]
    top_neg = sorted(neg.items(), key=lambda x: -x[1])[:3]
    recs["twogis"].append(
        "Главные источники негатива в 2GIS: "
        + ", ".join(f"«{k}» ({v} упоминаний)" for k, v in top_neg)
        + ". Сформировать рабочие группы по каждому направлению."
    )
    recs["twogis"].append(
        f"Средний рейтинг {data['avg_rating']} при {data['total_reviews']} отзывах. "
        "Запустить программу мотивации довольных студентов оставлять отзывы — "
        "цель: +150 отзывов за квартал и рейтинг ≥ 4.5."
    )
    recs["twogis"].append(
        "Отвечать на 100% отзывов в течение 48 часов, особенно на негативные — "
        "это повышает доверие и снижает влияние одиночного негатива."
    )

    comp = data["comparison"]
    leader = max(comp, key=lambda x: x["rating"])
    if leader["name"] != data["college"]:
        recs["general"].append(
            f"Лидер по рейтингу в нише — «{leader['name']}» ({leader['rating']}). "
            f"Изучить их контент-стратегию и работу с отзывами."
        )
    recs["general"].append(
        "Внедрить ежемесячный отчёт по метрикам: рейтинг 2GIS, ER в Instagram, "
        "доля позитивных отзывов, прирост подписчиков. KPI для PR-отдела."
    )
    recs["general"].append(
        "Связать офлайн-события и онлайн-контент: каждое мероприятие — это минимум "
        "1 Reels, 1 карусель и 5 Stories. Это повышает оба канала одновременно."
    )

    return recs
