import sys
sys.stdout.reconfigure(encoding='utf-8')

print("👋 Hello, I’m CryptoBuddy — your AI-powered financial sidekick! 🌟")
print("Ask me about crypto trends, sustainability, or long-term advice!")
print("💡 I can help you with:")


crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}


def chatbot():
    while True:
        user_query = input("\nYou: ").lower()

        if "exit" in user_query:
            print("CryptoBuddy: 👋 Stay smart, invest wisely! Bye!")
            break

        elif "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: 🌱 Try {recommend}! It's eco-friendly with a strong long-term outlook.")

        elif "trending" in user_query or "rising" in user_query:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            print(f"CryptoBuddy: 🚀 These cryptos are trending up: {', '.join(trending)}.")

        elif "long-term" in user_query or "should i buy" in user_query:
            for name, info in crypto_db.items():
                if info["price_trend"] == "rising" and info["sustainability_score"] > 0.7:
                    print(f"CryptoBuddy: 🛡️ {name} is rising and has great sustainability! Great for long-term growth.")
                    break

        else:
            print("CryptoBuddy: 🤔 I'm not sure about that. Ask me about crypto trends or sustainability!")

chatbot()
