def securities(symbols):
    if isinstance(symbols, str):
        symbols = [symbols]
    symbols = ",".join(symbols)
    return f"https://api.tornado.com/api/v1/securities?symbols={symbols}&platform=ios"


def securities_by_id(security_ids):
    if isinstance(security_ids, str):
        security_ids = [security_ids]
    security_ids = ",".join(security_ids)
    return f"https://api.tornado.com/api/v1/securities?security_ids={security_ids}&platform=ios"


class Endpoints:
    # Checks if the market is open
    market_open = "https://api.tornado.com/api/v1/util/market_open"
    # Gets the current user's portfolio
    user_portfolio = "https://api.tornado.com/api/v1/current_user/portfolio"
    # Gets information about the current user account
    user_profile = "https://api.tornado.com/api/v1/current_user"
    # Gets some detailed platform config/info that you probably don't need for anything
    user_platform_info = "https://api.tornado.com/api/v1/current_user/session"
    # Gets all lessons on the platform
    lessons = "https://api.tornado.com/api/v1/lessons"
    # Gets current user's lesson stats
    lesson_stats = "https://api.tornado.com/api/v1/lessons/stats"
    # Gets availability of next lesson / next lesson if available
    next_lesson = "https://api.tornado.com/api/v1/lessons/next"
    # Gets lessons completed by current user
    lessons_completed = "https://api.tornado.com/api/v1/completed_lessons"
    # Gets balance availability info
    withdrawal_info = "https://api.tornado.com/api/v1_1/bank_accounts/amount_available"
    # Gets linked bank account info
    linked_bank_account_info = "https://api.tornado.com/api/v1_1/bank_accounts"
    # Gets linked bank account info and withdrawal info (because older API is better?)
    bank_info_v1 = "https://api.tornado.com/api/v1/bank_accounts"
    # Gets monetary transaction history
    transaction_history = "https://api.tornado.com/api/v1/history/transactions"
    # Gets upcoming earnings announcements
    upcoming_earnings = "https://api.tornado.com/api/v1/securities/upcoming_earnings_announcements"
    # Gets pending connections
    pending_connections = 'https://api.tornado.com/api/v1/connections/pending'
    # Gets news subscriptions
    news_subscriptions = 'https://api.tornado.com/api/v1/news_content_subscriptions'
    # POST to create order
    place_order = 'https://api.tornado.com/api/v1/order/place'
    # gets orders
    orders = 'https://api.tornado.com/api/v1/orders'
